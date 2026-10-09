"""Build report.html from the chapter files with pandoc.

Joins report/00-chapter.md to report/04-chapter.md, adjusts the image paths to the repository
root, places every Bounded Context Canvas (with its heading and caption) on its own landscape
page, and renders the result with the print stylesheet in assets/styles/report.css.

Usage, from the repository root:
    python3 scripts/build_html.py
"""
import re
import subprocess

chapters = [open(f'report/0{n}-chapter.md', encoding='utf-8').read().strip() + '\n' for n in '01234']
body = '\n\n'.join(chapters)
body = re.sub(r'(\]\(<?|src=")\.\./assets/', r'\1assets/', body)

# wrap each canvas, from its heading to the end of its table, in a landscape page
parts = []
pos = 0
for match in re.finditer(r'<table class="canvas"', body):
    start = body.rindex('\n##### ', 0, match.start()) + 1
    end = body.index('\n</table>\n\n', match.start()) + len('\n</table>')
    parts += [body[pos:start], '<div class="canvas-page">\n\n', body[start:end], '\n\n</div>']
    pos = end
parts.append(body[pos:])
body = ''.join(parts)

page = subprocess.run(['pandoc', '-f', 'gfm', '-t', 'html5', '--standalone',
                       '--css', 'assets/styles/report.css',
                       '--metadata', 'pagetitle=Guardian+ - Informe del Trabajo Final',
                       '--metadata', 'lang=es'],
                      input=body, capture_output=True, text=True, check=True).stdout


# rows are kept on a single page, except those too long to fit in one, which may split
def mark_long_row(match):
    cells = re.findall(r'<t[dh]\b[^>]*>(.*?)</t[dh]>', match.group(0), re.S)
    longest = max((len(re.sub(r'<[^>]+>', '', c)) for c in cells), default=0)
    return match.group(0).replace('<tr>', '<tr class="long-row">', 1) if longest > 1500 else match.group(0)


page = re.sub(r'<tr>(?:(?!<tr\b).)*?</tr>', mark_long_row, page, flags=re.S)
open('report.html', 'w', encoding='utf-8').write(page)
print(f'report.html | Canvases: {page.count("class=\"canvas-page\"")} | Long rows: {page.count("long-row")}')
