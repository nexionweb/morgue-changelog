#!/usr/bin/env python3
"""Generate a themed index.html from CHANGELOG.md.
Run:  python3 generate.py   (reads ./CHANGELOG.md, writes ./index.html)

Layout: a featured "Latest" panel + legend on the left, a timeline of prior
releases on the right. Bullets are color-dotted by category — lead a bullet with
"New:", "Improvement:", "Fix:", or "Breaking:" (or put it in a "### Fix: ..."
section) to set the dot; anything else defaults to Feature.
"""
import re, html, pathlib, datetime

src = pathlib.Path('CHANGELOG.md').read_text()

# ── Parse ───────────────────────────────────────────────────────────────────────
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

# ── Categorize (for the colored dots) ───────────────────────────────────────────
CATS = [
    ('breaking',    ['breaking', 'break', 'removed', 'remove', 'deprecated']),
    ('fix',         ['fix', 'fixed', 'bugfix', 'bug', 'hotfix']),
    ('improvement', ['improvement', 'improved', 'improve', 'changed', 'change',
                     'update', 'updated', 'tweak', 'polish', 'refined', 'better']),
    ('feature',     ['new', 'feature', 'added', 'add']),
]

def cat_of_word(word):
    if not word:
        return None
    w = word.strip().lower().rstrip(':')
    for cat, words in CATS:
        if w in words:
            return cat
    return None

def lead_word(text):
    m = re.match(r'\*\*([A-Za-z][A-Za-z ]*?):?\*\*', text)   # **Fix:** / **Fix**
    if m:
        return m.group(1)
    m = re.match(r'([A-Za-z]+):\s', text)                    # Fix: ...
    if m:
        return m.group(1)
    return None

def fmt_date(d):
    try:
        return datetime.datetime.strptime(d, '%Y-%m-%d').strftime('%B %d, %Y').upper()
    except ValueError:
        return d.upper()

def inline(t):
    t = html.escape(t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    return t

def render_items(section):
    first_word = section['title'].split()[0] if section['title'] else ''
    sec_cat = cat_of_word(lead_word(section['title'] + ' ')) or cat_of_word(first_word)
    out = []
    for it in section['items']:
        cat = cat_of_word(lead_word(it['text'])) or sec_cat or 'feature'
        sub = ' sub' if it['level'] else ''
        out.append(
            f'<li class="item{sub}" data-cat="{cat}">'
            f'<span class="dot {cat}"></span>'
            f'<span class="itext">{inline(it["text"])}</span></li>'
        )
    return ''.join(out)

def render_sections(v):
    parts = []
    for s in v['sections']:
        if s['title']:
            parts.append(f'<h3 class="sectitle">{inline(s["title"])}</h3>')
        parts.append(f'<ul class="items">{render_items(s)}</ul>')
    return ''.join(parts)

# ── Featured (latest) + timeline (rest) ─────────────────────────────────────────
featured_html = ''
if versions:
    v = versions[0]
    featured_html = f'''
      <div class="feat-card">
        <div class="feat-date">{html.escape(fmt_date(v["date"]))}</div>
        <h2 class="feat-title">Latest — {html.escape(v["version"])}</h2>
        {render_sections(v)}
      </div>
      <div class="legend">
        <span class="legend-title">Legend</span>
        <span class="chip"><span class="dot feature"></span>Feature</span>
        <span class="chip"><span class="dot improvement"></span>Improvement</span>
        <span class="chip"><span class="dot fix"></span>Fix</span>
        <span class="chip"><span class="dot breaking"></span>Breaking</span>
      </div>'''

timeline_html = ''
for v in versions[1:]:
    timeline_html += f'''
      <section class="entry">
        <div class="entry-date">{html.escape(fmt_date(v["date"]))}</div>
        <div class="entry-num">{html.escape(v["version"])}</div>
        {render_sections(v)}
      </section>'''

html_out = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Morgue Changelog — What's New</title>
<meta name="description" content="Every Morgue update in one place: new features, improvements, and fixes for the local-first design reference manager for Mac." />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@700;900&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet" />
<style>
  :root {{
    --bg:#1A1917; --surface:#222120; --card:#2A2927; --text:#F0EDE8;
    --muted:#8A857D; --border:#333130; --accent:#FF4405;
    --feature:#34A866; --improvement:#4C8FBF; --fix:#E0A800; --breaking:#E5484D;
    --mono:"Space Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
    --display:"Inter Tight",-apple-system,BlinkMacSystemFont,sans-serif;
    --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--text); line-height:1.6;
    font-family:var(--sans); -webkit-font-smoothing:antialiased; }}
  /* Film grain overlay — matches the app's texture */
  body::before {{
    content:""; position:fixed; inset:0; z-index:9999; pointer-events:none;
    opacity:0.05; mix-blend-mode:overlay;
    background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  }}
  a {{ color:var(--accent); text-decoration:none; }}
  .wrap {{ max-width:1100px; margin:0 auto; padding:48px 28px 120px; }}

  .pill {{ display:inline-flex; align-items:center; gap:8px; border:1px solid var(--border);
    border-radius:999px; padding:7px 16px; margin-bottom:30px; }}
  .pill .appicon {{ width:18px; height:18px; border-radius:24%; display:block; }}
  .pill .lbl {{ font-family:var(--mono); font-weight:700; font-size:11px; letter-spacing:0.16em;
    text-transform:uppercase; color:var(--accent); }}

  .layout {{ display:grid; grid-template-columns:minmax(0,0.85fr) minmax(0,1.15fr); gap:48px; align-items:start; }}
  @media (max-width:820px) {{ .layout {{ grid-template-columns:1fr; gap:40px; }} }}

  .feat {{ position:sticky; top:32px; }}
  @media (max-width:820px) {{ .feat {{ position:static; }} }}
  .feat-card {{ background:var(--surface); border:1px solid var(--border); border-radius:14px; padding:26px; }}
  .feat-date {{ font-family:var(--mono); font-size:11px; letter-spacing:0.08em; color:var(--muted); margin-bottom:10px; }}
  .feat-title {{ font-family:var(--display); font-weight:900; font-size:38px; line-height:1.02;
    letter-spacing:-0.03em; margin:0 0 14px; }}

  .legend {{ display:flex; flex-wrap:wrap; align-items:center; gap:8px; margin-top:22px; padding-top:20px; border-top:1px solid var(--border); }}
  .legend-title {{ font-family:var(--mono); font-size:10px; letter-spacing:0.1em; text-transform:uppercase; color:var(--muted); width:100%; margin-bottom:2px; }}
  .chip {{ display:inline-flex; align-items:center; gap:7px; border:1px solid var(--border); border-radius:999px;
    padding:4px 11px; font-family:var(--mono); font-size:11px; color:var(--text); }}
  .chip .dot {{ margin-top:0; }}  /* center in the chip (the list-item offset doesn't apply here) */

  .timeline {{ position:relative; }}
  .entry {{ padding:0 0 30px 0; border-bottom:1px solid var(--border); margin-bottom:30px; }}
  .entry:last-child {{ border-bottom:none; }}
  .entry-date {{ font-family:var(--mono); font-size:11px; letter-spacing:0.08em; color:var(--muted); margin-bottom:8px; }}
  .entry-num {{ font-family:var(--display); font-weight:900; font-size:30px; letter-spacing:-0.02em; margin-bottom:10px; }}

  .sectitle {{ font-size:13px; font-weight:600; color:var(--muted); margin:16px 0 8px; }}
  .items {{ list-style:none; margin:0; padding:0; }}
  .item {{ display:flex; gap:11px; align-items:flex-start; padding:7px 0;
    border-bottom:1px solid color-mix(in srgb, var(--border) 55%, transparent); font-size:14.5px; }}
  .item:last-child {{ border-bottom:none; }}
  .item.sub {{ padding-left:22px; color:var(--muted); font-size:13.5px; }}
  .itext {{ flex:1; }}
  .dot {{ flex-shrink:0; width:8px; height:8px; border-radius:50%; margin-top:8px; background:var(--muted); }}
  .dot.feature {{ background:var(--feature); }}
  .dot.improvement {{ background:var(--improvement); }}
  .dot.fix {{ background:var(--fix); }}
  .dot.breaking {{ background:var(--breaking); }}

  code {{ font-family:var(--mono); font-size:12.5px; background:var(--card); border:1px solid var(--border); border-radius:4px; padding:1px 5px; }}
  strong {{ font-weight:700; }}
  footer {{ margin-top:56px; color:var(--muted); font-size:13px; border-top:1px solid var(--border); padding-top:22px; }}
</style>
</head>
<body>
  <div class="wrap">
    <div class="pill"><img class="appicon" src="icon.png" alt="" /><span class="lbl">Changelog</span></div>
    <div class="layout">
      <aside class="feat">{featured_html}</aside>
      <div class="timeline">{timeline_html}</div>
    </div>
    <footer>Morgue — the local-first design reference manager for Mac · <a href="https://www.morgueapp.com">morgueapp.com</a> · <a href="mailto:support@morgueapp.com">support@morgueapp.com</a></footer>
  </div>
</body>
</html>
'''

pathlib.Path('index.html').write_text(html_out)
print(f'wrote index.html — {len(versions)} versions')
