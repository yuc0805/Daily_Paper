/* Force-directed per-area lineage graph.
 * Usage in an area page:
 *   <link rel="stylesheet" href="../style.css">
 *   <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
 *   <script src="../area-graph.js"></script>
 *   <div id="area-graph-container"></div>
 *   <script>renderAreaGraph('time-series');</script>
 */

const CLUSTER_COLORS = {
  'transformer-foundations':   '#4e79a7',
  'classical-forecasting':     '#9c755f',
  'foundation-models-ts':      '#f28e2b',
  'llm-time-series':           '#e15759',
  'ssm-mamba':                 '#b07aa1',
  'wearable-har':              '#59a14f',
  'biosignals':                '#76b7b2',
  'self-supervised-pretraining': '#edc948',
  // generic fallback palette for any cluster names introduced later
  '__fallback__': ['#4e79a7','#f28e2b','#e15759','#76b7b2','#59a14f','#edc948','#b07aa1','#ff9da7','#9c755f','#bab0ac']
};

function colorForCluster(cluster, fallbackIdx) {
  if (CLUSTER_COLORS[cluster]) return CLUSTER_COLORS[cluster];
  const pal = CLUSTER_COLORS.__fallback__;
  return pal[fallbackIdx % pal.length];
}

async function renderAreaGraph(areaSlug) {
  const container = document.getElementById('area-graph-container');
  if (!container) return;
  let data;
  try {
    const resp = await fetch(`../data/area_lineage/${areaSlug}.json`);
    if (!resp.ok) throw new Error(resp.status);
    data = await resp.json();
  } catch (e) {
    container.innerHTML = '<p class="placeholder">Lineage graph not yet generated for this area.</p>';
    return;
  }

  // Compute in/out degrees for sizing.
  const inDeg = {}, outDeg = {};
  data.nodes.forEach(n => { inDeg[n.key] = 0; outDeg[n.key] = 0; });
  data.edges.forEach(e => {
    if (e.relation === 'builds_on') {
      inDeg[e.target] = (inDeg[e.target]||0) + 1;
      outDeg[e.source] = (outDeg[e.source]||0) + 1;
    }
  });

  // Cluster legend.
  const clusters = [...new Set(data.nodes.map(n => n.cluster))];
  const clusterIdx = Object.fromEntries(clusters.map((c, i) => [c, i]));

  const W = container.clientWidth || 900;
  const H = 520;
  const MIN_YEAR = Math.min(...data.nodes.map(n => n.year));
  const MAX_YEAR = Math.max(...data.nodes.map(n => n.year));
  const X_PAD = 50;
  const xScale = d => X_PAD + ((d.year - MIN_YEAR) / Math.max(1, (MAX_YEAR - MIN_YEAR))) * (W - 2*X_PAD);

  container.innerHTML = `
    <div class="area-graph-wrap">
      <svg id="area-graph-svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}"></svg>
      <div class="area-graph-legend"></div>
      <div class="area-graph-tooltip" style="opacity:0"></div>
    </div>
  `;

  const svg = d3.select('#area-graph-svg');

  // arrow marker
  svg.append('defs').append('marker')
    .attr('id','arrow')
    .attr('viewBox','0 -4 10 8')
    .attr('refX', 14).attr('refY', 0)
    .attr('markerWidth', 6).attr('markerHeight', 6)
    .attr('orient','auto')
    .append('path').attr('d','M0,-4L10,0L0,4').attr('fill','#999');

  // year axis
  const yearTicks = [];
  for (let y = MIN_YEAR; y <= MAX_YEAR; y++) yearTicks.push(y);
  const axis = svg.append('g').attr('class','area-graph-axis');
  axis.selectAll('line').data(yearTicks).enter().append('line')
    .attr('x1', y => X_PAD + ((y - MIN_YEAR)/Math.max(1,(MAX_YEAR-MIN_YEAR))) * (W - 2*X_PAD))
    .attr('x2', y => X_PAD + ((y - MIN_YEAR)/Math.max(1,(MAX_YEAR-MIN_YEAR))) * (W - 2*X_PAD))
    .attr('y1', H - 24).attr('y2', H - 18)
    .attr('stroke', '#ccc');
  axis.selectAll('text').data(yearTicks.filter((y, i) => yearTicks.length <= 12 || i % 2 === 0)).enter().append('text')
    .attr('x', y => X_PAD + ((y - MIN_YEAR)/Math.max(1,(MAX_YEAR-MIN_YEAR))) * (W - 2*X_PAD))
    .attr('y', H - 6)
    .attr('text-anchor','middle')
    .attr('font-size','10px')
    .attr('font-family','system-ui, sans-serif')
    .attr('fill','#888')
    .text(y => y);

  // Init: x = year-mapped, y = scattered around center
  data.nodes.forEach((n, i) => {
    n.x = xScale(n);
    n.y = H/2 - 80 + (i % 7) * 30;
  });

  const linkData = data.edges.map(e => ({...e}));

  const sim = d3.forceSimulation(data.nodes)
    .force('link', d3.forceLink(linkData).id(d => d.key).distance(60).strength(0.4))
    .force('charge', d3.forceManyBody().strength(-180))
    .force('collide', d3.forceCollide().radius(d => nodeRadius(d) + 6))
    .force('x', d3.forceX(d => xScale(d)).strength(0.6))
    .force('y', d3.forceY(H/2 - 20).strength(0.06));

  function nodeRadius(d) {
    const deg = (inDeg[d.key]||0) + (outDeg[d.key]||0);
    return Math.min(20, 5 + Math.sqrt(deg) * 2.5 + (d.anchor ? 3 : 0));
  }

  // Links
  const link = svg.append('g').attr('class','area-graph-links')
    .selectAll('line').data(linkData).enter().append('line')
    .attr('stroke', d => d.relation === 'sibling' ? '#bbb' : '#888')
    .attr('stroke-width', d => d.relation === 'sibling' ? 1 : 1.5)
    .attr('stroke-dasharray', d => d.relation === 'sibling' ? '3,3' : null)
    .attr('marker-end', d => d.relation === 'sibling' ? null : 'url(#arrow)')
    .attr('opacity', 0.55);

  // Nodes
  const node = svg.append('g').attr('class','area-graph-nodes')
    .selectAll('g').data(data.nodes).enter().append('g')
    .attr('cursor', 'pointer')
    .on('click', (e, d) => { window.location.href = `../papers/${d.key}.html`; })
    .call(d3.drag()
      .on('start', (e, d) => { if (!e.active) sim.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; })
      .on('drag', (e, d) => { d.fx = e.x; d.fy = e.y; })
      .on('end', (e, d) => { if (!e.active) sim.alphaTarget(0); d.fx = null; d.fy = null; })
    );

  node.append('circle')
    .attr('r', nodeRadius)
    .attr('fill', d => colorForCluster(d.cluster, clusterIdx[d.cluster]))
    .attr('stroke', d => d.anchor ? '#111' : 'rgba(0,0,0,0.2)')
    .attr('stroke-width', d => d.anchor ? 2.5 : 1)
    .attr('opacity', 0.92);

  node.append('text')
    .text(d => d.title)
    .attr('dy', d => nodeRadius(d) + 11)
    .attr('text-anchor', 'middle')
    .attr('font-size', '10px')
    .attr('font-family','system-ui, sans-serif')
    .attr('fill', '#333')
    .attr('pointer-events','none');

  const tooltip = d3.select(container).select('.area-graph-tooltip');
  node.on('mouseover', (e, d) => {
    tooltip.html(
      `<strong>${escapeHTML(d.title)}</strong><br>` +
      `${escapeHTML(d.authors_short)} &middot; ${d.year}<br>` +
      `<em>${escapeHTML(d.cluster)}</em>` +
      (d.anchor ? '<br><span style="color:#c00">anchor</span>' : '') +
      `<br>builds_on in: ${inDeg[d.key]||0}, out: ${outDeg[d.key]||0}`
    ).style('opacity', 1)
     .style('left', (e.pageX + 12) + 'px').style('top', (e.pageY - 10) + 'px');
  }).on('mousemove', e => {
    tooltip.style('left', (e.pageX + 12) + 'px').style('top', (e.pageY - 10) + 'px');
  }).on('mouseout', () => tooltip.style('opacity', 0));

  sim.on('tick', () => {
    link.attr('x1', d => d.source.x).attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x).attr('y2', d => d.target.y);
    node.attr('transform', d => `translate(${d.x},${d.y})`);
  });

  // Legend
  const legend = d3.select('.area-graph-legend');
  clusters.forEach(c => {
    const item = legend.append('span').attr('class','area-graph-legend-item');
    item.append('span').attr('class','area-graph-legend-dot').style('background', colorForCluster(c, clusterIdx[c]));
    item.append('span').text(c);
  });
  legend.append('span').attr('class','area-graph-legend-item')
    .html('<span class="area-graph-legend-dot" style="background:transparent;border:2px solid #111"></span>anchor');
  legend.append('span').attr('class','area-graph-legend-item')
    .html('<span class="area-graph-legend-dash"></span>sibling (different methods, same problem)');
}

function escapeHTML(s) {
  return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}