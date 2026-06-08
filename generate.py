#!/usr/bin/env python3
"""Generate a themed index.html from CHANGELOG.md.
Run:  python3 generate.py   (reads ./CHANGELOG.md, writes ./index.html)
"""
import re, html, pathlib

src = pathlib.Path('CHANGELOG.md').read_text()

versions = []
cur = None
sec = None
for raw in src.splitlines():
    line = raw.rstrip()
    m = re.match(r'## \[(.+?)\]\s*[—-]+\s*(.*)', line)
    if m:
        cur = {'version': m.group(1), 'date': m.group(2).strip(), 'sections': []}
        versions.append(cur); sec = None
        continue
    if line.startswith('### '):
        sec = {'title': line[4:].strip(), 'items': []}
        if cur: cur['sections'].append(sec)
        continue
    bm = re.match(r'(\s*)-\s+(.*)', line)
    if bm and cur is not None:
        level = 1 if len(bm.group(1)) >= 2 else 0
        if sec is None:
            sec = {'title': '', 'items': []}; cur['sections'].append(sec)
        sec['items'].append({'text': bm.group(2), 'level': level})

def inline(t):
    t = html.escape(t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    return t

blocks = []
for i, v in enumerate(versions):
    latest = ' latest' if i == 0 else ''
    pill = '<span class="pill">LATEST</span>' if i == 0 else ''
    secs = []
    for s in v['sections']:
        title = f'<h3>{inline(s["title"])}</h3>' if s['title'] else ''
        lis = ''.join(
            f'<li class="{"sub" if it["level"] else ""}">{inline(it["text"])}</li>'
            for it in s['items']
        )
        secs.append(f'{title}<ul>{lis}</ul>')
    blocks.append(f'''
    <section class="ver{latest}">
      <div class="ver-head">
        <span class="num">{html.escape(v["version"])}</span>
        {pill}
        <span class="date">{html.escape(v["date"])}</span>
      </div>
      {''.join(secs)}
    </section>''')

html_out = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Morgue — Changelog</title>
<meta name="description" content="Release notes for Morgue, the local-first design inspiration manager." />
<style>
  :root {{
    --bg:#F2F0EB; --surface:#ffffff; --text:#1A1917; --muted:#6b6862;
    --border:#e2dfd8; --accent:#FF4405; --mono:"Space Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --bg:#161412; --surface:#1f1c1a; --text:#F0EDE8; --muted:#9a958d; --border:#2c2926; }}
  }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--text); line-height:1.6;
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
    -webkit-font-smoothing:antialiased; }}
  .wrap {{ max-width:760px; margin:0 auto; padding:56px 24px 110px; }}
  .badge {{ display:inline-flex; align-items:center; gap:10px; margin-bottom:26px; }}
  .badge .appicon {{ width:32px; height:32px; border-radius:22%; display:block; box-shadow:0 1px 3px rgba(0,0,0,0.2); }}
  .badge .bname {{ font-family:var(--mono); font-weight:700; letter-spacing:0.12em; font-size:13px; text-transform:uppercase; }}
  h1 {{ font-size:32px; letter-spacing:-0.02em; margin:0 0 6px; }}
  .sub {{ color:var(--muted); font-size:14px; margin:0 0 40px; }}
  .ver {{ position:relative; padding:0 0 26px 26px; border-left:2px solid var(--border); }}
  .ver:last-child {{ border-left-color:transparent; }}
  .ver::before {{ content:""; position:absolute; left:-7px; top:4px; width:12px; height:12px; border-radius:50%; background:var(--border); border:2px solid var(--bg); }}
  .ver.latest::before {{ background:var(--accent); }}
  .ver-head {{ display:flex; align-items:center; gap:10px; flex-wrap:wrap; margin-bottom:10px; }}
  .num {{ font-family:var(--mono); font-weight:700; font-size:17px; color:var(--accent); }}
  .date {{ color:var(--muted); font-size:12px; font-family:var(--mono); }}
  .pill {{ font-family:var(--mono); font-size:9px; font-weight:700; letter-spacing:0.08em; color:#fff; background:var(--accent); border-radius:20px; padding:2px 8px; }}
  h3 {{ font-size:13px; margin:16px 0 6px; letter-spacing:-0.01em; }}
  ul {{ margin:0 0 4px; padding-left:18px; }}
  li {{ font-size:14.5px; margin:3px 0; color:var(--text); }}
  li.sub {{ list-style:circle; margin-left:18px; color:var(--muted); font-size:13.5px; }}
  code {{ font-family:var(--mono); font-size:12.5px; background:var(--surface); border:1px solid var(--border); border-radius:4px; padding:1px 5px; }}
  strong {{ font-weight:700; }}
  footer {{ margin-top:48px; color:var(--muted); font-size:13px; border-top:1px solid var(--border); padding-top:20px; }}
  footer a {{ color:var(--accent); text-decoration:none; }}
</style>
</head>
<body>
  <div class="wrap">
    <div class="badge">
      <img class="appicon" src="icon.png" alt="Morgue app icon" />
      <span class="bname">Morgue</span>
    </div>
    <h1>Changelog</h1>
    <p class="sub">Release notes for Morgue — a local-first design inspiration manager.</p>
    {''.join(blocks)}
    <footer>Questions? <a href="mailto:support@morgueapp.com">support@morgueapp.com</a></footer>
  </div>
</body>
</html>
'''

pathlib.Path('index.html').write_text(html_out)
print(f'wrote index.html — {len(versions)} versions')
