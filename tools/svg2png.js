// Rasterize an SVG to PNG at a given pixel width using resvg (handles CSS classes and <use>, which cairosvg does not).
// usage: node svg2png.js in.svg out.png width
const { Resvg } = require('@resvg/resvg-js'); const fs = require('fs');
const [svgPath, outPath, width] = process.argv.slice(2);
const svg = fs.readFileSync(svgPath, 'utf8');
const r = new Resvg(svg, { fitTo: { mode: 'width', value: parseInt(width, 10) }, background: 'rgba(0,0,0,0)' });
fs.writeFileSync(outPath, r.render().asPng());
