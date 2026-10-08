"""Rebuild the Context Map figures of chapter II from their Context Mapper sources.

Runs the Context Mapper CLI on every *-context-map.cml file, replaces the CML identifiers with
the Bounded Context names used in the report, draws external systems with a dashed outline,
joins edges that share the same upstream label so it is drawn once per context, and renders
the resulting Graphviz source to PNG.

Requires the Context Mapper CLI (https://contextmapper.org/docs/cli/), given by the
CONTEXT_MAPPER_CLI environment variable or available as `cm` on the PATH, and Graphviz `dot`.

Usage, from the repository root:
    python3 scripts/build_context_maps.py
"""
import glob
import os
import re
import subprocess
import tempfile
from collections import defaultdict

FOLDER = 'assets/images/chapterII/context-mapping'
NAMES = {
    'EmergencyAlerting': 'Emergency & Alerting',
    'HealthMonitoring': 'Health Monitoring',
    'CareRoutinesWellness': 'Care Routines & Wellness',
    'MobilityGeofencing': 'Mobility & Geofencing',
    'Profile': 'Profile',
    'Subscriptions': 'Subscriptions',
    'IAM': 'IAM',
    'WearableDevice': 'Wearable Device',
    'Stripe': 'Stripe',
    'NotificationProviders': 'Notification Providers',
}
GRAPH = 'graph ["pad"="0.3","nodesep"="0.7","ranksep"="1.1","dpi"="150"]'
# per-map layout adjustments that keep each figure readable at page width
LAYOUT = {
    'global-context-map': ['{ rank=same; "WearableDevice"; "IAM"; "Stripe" }',
                           '{ rank=same; "NotificationProviders"; "EmergencyAlerting" }'],
    'identity-external-context-map': ['graph ["rankdir"="LR","ranksep"="2.2","nodesep"="0.35"]'],
}

cm = os.environ.get('CONTEXT_MAPPER_CLI', 'cm')
# without headless mode the AWT shutdown thread keeps the CLI's JVM alive on macOS
env = dict(os.environ, JAVA_OPTS=(os.environ.get('JAVA_OPTS', '') + ' -Djava.awt.headless=true').strip())

# classification shown under each name: the domain for Bounded Contexts, "External System" otherwise
contexts = open(f'{FOLDER}/bounded-contexts.cml', encoding='utf-8').read()
kinds = {}
for name, body in re.findall(r'BoundedContext (\w+) \{(.*?)\}', contexts):
    vision = re.search(r'domainVisionStatement = "([^"]+)"', body)
    kinds[name] = vision.group(1) if vision else 'External System'


def label(match):
    name = match.group(1)
    text = NAMES[name].replace('&', '&amp;')
    style = '"bold,dashed"' if kinds[name] == 'External System' else '"bold"'
    return (f'"label"=<{text}<BR/><FONT POINT-SIZE="11">{kinds[name]}</FONT>>,"style"={style}')


for source in sorted(glob.glob(f'{FOLDER}/*-context-map.cml')):
    base = os.path.basename(source)[:-len('.cml')]
    with tempfile.TemporaryDirectory() as out:
        # imports in CML files are resolved from the working directory
        subprocess.run([cm, 'generate', '-i', os.path.basename(source), '-g', 'context-map', '-o', out],
                       check=True, capture_output=True, cwd=FOLDER, env=env, timeout=300)
        dot = open(f'{out}/{base}_ContextMap.gv', encoding='utf-8').read()

    dot = re.sub(r'graph \["imagepath"=[^\]]*\]', GRAPH, dot)
    # node attributes: the generator writes the style before the label
    dot = re.sub(r'"style"="bold","label"="(\w+)\\n"', lambda m: label(m), dot)

    # edges whose upstream end carries the same label start from a single point of the context
    edges = re.findall(r'^"(\w+)" -> "\w+" \[.*?"taillabel"=(<<.*?>>)', dot, re.M | re.S)
    tails = defaultdict(set)
    for tail, tail_label in edges:
        tails[tail].add(tail_label)
    for tail, labels in tails.items():
        if len(labels) == 1 and sum(1 for t, _ in edges if t == tail) > 1:
            dot = re.sub(rf'^("{tail}" -> "\w+" \[)', rf'\1"sametail"="{tail}",', dot, flags=re.M)

    dot = dot.rstrip()[:-1] + ''.join(f'{line}\n' for line in LAYOUT.get(base, [])) + '}\n'
    open(f'{FOLDER}/{base}.dot', 'w', encoding='utf-8').write(dot)
    subprocess.run(['dot', '-Tpng', f'{FOLDER}/{base}.dot', '-o', f'{FOLDER}/{base}.png'], check=True)
    print(f'{FOLDER}/{base}.png')
