"""Rebuild README.md from the chapter files.

Keeps the README front matter (cover, version registry, insights, contents, student outcome
and SMART objectives) and the closing sections (conclusions and bibliography), regenerates the
table and figure indexes from the captions in each chapter, and inserts the chapters with their
image paths adjusted to the repository root.

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

body = '\n'.join([front] + chapters + [closing])
body = re.sub(r'(\]\(<?|src=")\.\./assets/', r'\1assets/', body)
open('README.md', 'w', encoding='utf-8').write(body)
print(f"Tablas: {indexes.count('](#tabla-')} | Figuras: {indexes.count('](#figura-')}")
