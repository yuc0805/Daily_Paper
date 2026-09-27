# Like worker — one-time setup (~10 minutes)

This tiny Cloudflare Worker is the bridge between the Like buttons on
https://yuc0805.github.io/Daily_Paper/ and the repo. Each rating is saved
instantly as a file in `feedback/inbox/`; the 6AM GitHub Action reads those
files, updates the knowledge graph, and publishes the next day's papers.
No manual exporting ever again.

## 1. Create a fine-grained token (minimal scope)

1. GitHub → Settings → Developer settings → Personal access tokens →
   **Fine-grained tokens** → **Generate new token**
2. Token name: `daily-paper-likes`
3. **Repository access** → *Only select repositories* → pick `Daily_Paper`
4. **Repository permissions** → **Contents** → **Read and write**
5. Generate and copy the token (starts with `github_pat_`).

This token can only read/write file contents in this one repo — nothing else.

## 2. Deploy the worker

1. Sign up / log in at https://dash.cloudflare.com (free plan is fine).
2. Left sidebar → **Workers & Pages** → **Create** → **Create Worker**.
3. Name it e.g. `daily-paper-likes`, deploy once with the starter code,
   then **Edit code**, delete everything, and paste in `worker.js` from
   this folder. **Save and deploy**.
4. Go to the worker's **Settings** → **Variables and Secrets**:
   - Add variable `REPO` = `yuc0805/Daily_Paper`
   - Add variable `BRANCH` = `main`
   - Add **secret** `GITHUB_TOKEN` = the token from step 1 (paste, encrypt)
   - (Optional) Add **secret** `FEEDBACK_SECRET` = any random string —
     if set, the site must send the same value (see step 3).
5. Copy the worker's public URL, e.g.
   `https://daily-paper-likes.YOURNAME.workers.dev`

## 3. Point the site at the worker

In `docs/index.html`, find this line near the top of the feedback script:

```js
window.FEEDBACK_ENDPOINT = ''; // <-- paste your Cloudflare Worker URL here
```

Paste your worker URL between the quotes, commit, and push. (Or tell Muse
the URL and it will do it.)

If you set `FEEDBACK_SECRET`, also set in the same place:

```js
window.FEEDBACK_SECRET = 'the-same-random-string';
```

## 4. Test

1. Open the site, click 👍 on any paper.
2. Within seconds, a new file should appear in
   `feedback/inbox/` on GitHub.
3. The next 6AM run consumes it: liked papers get added to the knowledge
   graph under the right category, and the inbox file is deleted.

If a rating ever fails to send (offline, worker down), it stays in the
browser's localStorage and is retried on the next click; the **Export
likes** button remains as a manual backup.
