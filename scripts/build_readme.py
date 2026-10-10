"""Rebuild README.md from the chapter files.

Keeps the README front matter (cover, version registry, insights, contents, student outcome
and SMART objectives) and the closing sections (conclusions and bibliography), regenerates the
table and figure indexes from the captions in each chapter, and inserts the chapters with their
image paths adjusted to the repository root. The front matter is also written to
report/00-chapter.md, with its image paths relative to that folder and its links pointing to
the chapter files, so both stay in sync.

Usage, from the repository root:
    python3 scripts/build_readme.py
"""
import re

PB = '<div style="page-break-before: always; break-before: page;"></div>'

readme = open('README.md', encoding='utf-8').read()
front = readme[:readme.index(PB + '\n\n# Capítulo I:')].rstrip() + '\n'
closing = readme[readme.index(PB + '\n\n# Conclusiones y recomendaciones'):].strip() + '\n'
chapters = [open(f'report/0{n}-chapter.md', encoding='utf-8').read().strip() + '\n' for n in '1234']


def index(kind, title):
    out = [PB, '', f'# {title}', '']
    for chapter in chapters:
        name = re.search(r'^# (Capítulo [IV]+: .+)$', chapter, re.M).group(1)
        items = re.findall(rf'<a id="({kind.lower()}-[\d-]+)"></a>\*\*({kind} [\d.]+)\*\* (.+)$', chapter, re.M)
        if not items:
            continue
        out += [f'**{name}**', '']
        out += [f'- [{number} {text.strip()}](#{anchor})' for anchor, number, text in items]
        out.append('')
    return '\n'.join(out)


# replace the previous indexes, placed between the contents and the student outcome
front = re.sub(r'\n' + re.escape(PB) + r'\n\n# Índice de tablas\n.*?(?=\n' + re.escape(PB) + r'\n\n# Student Outcome)',
               '', front, flags=re.S)
indexes = index('Tabla', 'Índice de tablas') + '\n' + index('Figura', 'Índice de figuras')
k = front.index(PB + '\n\n# Student Outcome')
front = front[:k] + indexes + '\n' + front[k:]

if '- [Índice de tablas]' not in front:
    front = front.replace('- [Capítulo I: Presentación]',
                          '- [Índice de tablas](#índice-de-tablas)\n- [Índice de figuras](#índice-de-figuras)\n'
                          '- [Capítulo I: Presentación]', 1)



def anchors(text):
    """Heading slugs (as GitHub builds them) and caption ids defined in a markdown text."""
    found, fence = set(re.findall(r'<a id="([^"]+)"></a>', text)), False
    for line in text.split('\n'):
        if line.startswith(('```', '~~~')):
            fence = not fence
        heading = None if fence else re.match(r'^#{1,6} (.*)', line)
        if heading:
            found.add(re.sub(r'[^\w\- ]', '', heading.group(1).strip().lower()).replace(' ', '-'))
    return found


# in report/00-chapter.md the links point to the file that holds each section
targets = {a: f'0{n}-chapter.md' for n, chapter in zip('1234', chapters) for a in anchors(chapter)}
front_anchors = anchors(front)


def link(match):
    anchor = match.group(1)
    if anchor in front_anchors:
        return match.group(0)
    return f"]({targets.get(anchor, '../README.md')}#{anchor})"


front_file = re.sub(r'(\]\(<?|src=")assets/', r'\1../assets/', front)
open('report/00-chapter.md', 'w', encoding='utf-8').write(re.sub(r'\]\(#([^)]+)\)', link, front_file))

body = '\n'.join([front] + chapters + [closing])
body = re.sub(r'(\]\(<?|src=")\.\./assets/', r'\1assets/', body)
open('README.md', 'w', encoding='utf-8').write(body)
print(f"Tablas: {indexes.count('](#tabla-')} | Figuras: {indexes.count('](#figura-')}")
