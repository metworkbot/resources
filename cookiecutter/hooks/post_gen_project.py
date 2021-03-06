#!/usr/bin/env python3

import os

def test_empty(path):
    try:
        with open(path, 'rb') as f:
            content = f.read().strip()
            if len(content) == 0:
                return True
    except Exception:
        pass
    return False


paths_to_delete = []
for path in [os.path.join(x[0], y) for x in os.walk('.') for y in x[2]]:
    if test_empty(path):
        paths_to_delete.append(path)
    if path.endswith('.delete'):
        if not test_empty(path):
            paths_to_delete.append(path.replace('.delete', ''))
            paths_to_delete.append(path)


for path in paths_to_delete:
    if os.path.basename(path) in ['__init__.py']:
        continue
    try:
        os.unlink(path)
    except Exception:
        pass
