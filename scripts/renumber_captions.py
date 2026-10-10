"""Renumber figure and table captions of every chapter and update their in-text references.

Captions follow the format `<a id="figura-2-5"></a>**Figura 2.5.** Título`. They are renumbered
in order of appearance, per chapter and per kind (Figura / Tabla). References such as
"La Figura 2.5", "las Tablas 2.13 a 2.49" or "las Figuras 3.6 y 3.7" are updated to match.
When a number is duplicated, each reference is resolved to the closest caption that follows it.

Usage, from the repository root:
    python3 scripts/renumber_captions.py
    python3 scripts/build_readme.py
"""
import re

CAPTION = re.compile(r'^<a id="(figura|tabla)-(\d+)-(\d+)"></a>\*\*(Figura|Tabla) \d+\.\d+\.\*\*')
REFERENCE = re.compile(r'\b(Figura|Tabla)(s?) (\d+)\.(\d+)((?:(?: a | y |, )\d+\.\d+)*)')

for chapter in '1234':
    path = f'report/0{chapter}-chapter.md'
    lines = open(path, encoding='utf-8').read().split('\n')

    # caption positions: kind -> old number -> [(line index, new number)]
    captions, counters = {}, {'Figura': 0, 'Tabla': 0}
    for i, line in enumerate(lines):
        m = CAPTION.match(line)
        if m and m.group(2) == chapter:
            kind = m.group(4)
            counters[kind] += 1
            captions.setdefault(kind, {}).setdefault(int(m.group(3)), []).append((i, counters[kind]))

    def resolve(kind, old, at):
        found = captions.get(kind, {}).get(old)
        if not found:
            return old
        after = [new for pos, new in found if pos >= at]
        return after[0] if after else found[-1][1]

    changed = 0
    for i, line in enumerate(lines):
        m = CAPTION.match(line)
        if m and m.group(2) == chapter:
            kind = m.group(4)
            new = resolve(kind, int(m.group(3)), i)
            fixed = re.sub(r'^<a id="[^"]+"></a>\*\*\w+ \d+\.\d+\.\*\*',
                           f'<a id="{kind.lower()}-{chapter}-{new}"></a>**{kind} {chapter}.{new}.**', line)
        else:
            def replace(match, at=i):
                kind, plural, ch, num, rest = match.groups()
                if ch != chapter:
                    return match.group(0)
                rest = re.sub(r'(\d+)\.(\d+)',
                              lambda r: f'{r.group(1)}.{resolve(kind, int(r.group(2)), at)}' if r.group(1) == chapter else r.group(0),
                              rest)
                return f'{kind}{plural} {ch}.{resolve(kind, int(num), at)}{rest}'
            fixed = REFERENCE.sub(replace, line)
        if fixed != line:
            lines[i] = fixed
            changed += 1

    open(path, 'w', encoding='utf-8').write('\n'.join(lines))
    print(f"Capítulo {chapter}: {counters['Figura']} figuras, {counters['Tabla']} tablas, {changed} líneas actualizadas")
