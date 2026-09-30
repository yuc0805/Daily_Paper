/**
 * daily-paper like worker (Cloudflare Workers)
 * ------------------------------------------------
 * Receives like/dislike ratings from the Daily Paper site and stores each one
 * as a small JSON file in feedback/inbox/ of the GitHub repo, via the
 * GitHub Contents API. The 6AM GitHub Action (scripts/daily_update.py)
 * picks those files up, adds liked papers to the knowledge graph, and
 * deletes the processed files.
 *
 * Deploy: see README.md in this folder.
 *
 * Required worker secrets / vars:
 *   GITHUB_TOKEN  (secret) fine-grained PAT, Contents: read+write, on the repo
 *   REPO          (var)    e.g. "yuc0805/Daily_Paper"
 *   BRANCH        (var)    e.g. "main"            (optional, defaults to main)
 *   FEEDBACK_SECRET (secret) optional shared secret; if set, requests must
 *                   include the same `secret` field or they are rejected.
 */

const ALLOWED_ACTIONS = new Set(["like", "dislike", "clear"]);

function corsHeaders() {
  return {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
  };
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json", ...corsHeaders() },
  });
}

function b64encodeUnicode(str) {
  const bytes = new TextEncoder().encode(str);
  let bin = "";
  for (const b of bytes) bin += String.fromCharCode(b);
  return btoa(bin);
}

export default {
  async fetch(request, env) {
    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: corsHeaders() });
    }
    if (request.method !== "POST") {
      return json({ error: "POST only" }, 405);
    }

    let body;
    try {
      body = await request.json();
    } catch {
      return json({ error: "invalid JSON" }, 400);
    }

    if (env.FEEDBACK_SECRET && body.secret !== env.FEEDBACK_SECRET) {
      return json({ error: "forbidden" }, 403);
    }

    const { key, action, paper } = body;
    if (!key || typeof key !== "string" || !ALLOWED_ACTIONS.has(action)) {
      return json({ error: "payload needs {key, action: like|dislike|clear}" }, 400);
    }

    const safeKey = key.replace(/[^a-zA-Z0-9.-]/g, "_").slice(0, 80);
    const ts = new Date().toISOString().replace(/[:.]/g, "-");
    const rand = Math.random().toString(36).slice(2, 8);
    const path = `feedback/inbox/${ts}-${rand}-${safeKey}.json`;
    const reason = typeof body.reason === "string" ? body.reason.slice(0, 40) : "";
    const record = {
      key,
      action,
      reason,
      paper: {
        title: (paper && paper.title) || "",
        authors: (paper && paper.authors) || "",
        summary: ((paper && paper.summary) || "").slice(0, 2000),
        area_slug: (paper && paper.area_slug) || "",
        rec_type: (paper && paper.rec_type) || "",
      },
      ts: new Date().toISOString(),
    };

    const url = `https://api.github.com/repos/${env.REPO}/contents/${path}`;
    const gh = await fetch(url, {
      method: "PUT",
      headers: {
        Authorization: `Bearer ${env.GITHUB_TOKEN}`,
        Accept: "application/vnd.github+json",
        "Content-Type": "application/json",
        "User-Agent": "daily-paper-like-worker",
      },
      body: JSON.stringify({
        message: `feedback: ${action} ${key}`,
        content: b64encodeUnicode(JSON.stringify(record, null, 2)),
        branch: env.BRANCH || "main",
      }),
    });

    if (!gh.ok) {
      const detail = (await gh.text()).slice(0, 300);
      return json({ error: "github write failed", detail }, 502);
    }
    return json({ ok: true, path });
  },
};
