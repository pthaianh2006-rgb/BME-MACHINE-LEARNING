"""Execute every tutorial code cell as Python; never write a notebook."""
from pathlib import Path
import ast, contextlib, io, json, random, sys, platform
import numpy as np

ROOT = Path(__file__).resolve().parent
random.seed(42)
np.random.seed(42)
nb = json.loads((ROOT / 'source/python_source.json').read_text(encoding='utf-8-sig'))
namespace = {'__name__': '__main__'}
records, script = [], ['# Python and NumPy tutorial — executable source adapted from aim-lab/mlh-course-material\nimport random\nimport numpy as np\nrandom.seed(42)\nnp.random.seed(42)\n']
section = ''
for index, cell in enumerate(nb['cells']):
    source = ''.join(cell['source'])
    if cell['cell_type'] == 'markdown':
        if source.startswith('#'):
            section = source.splitlines()[0].lstrip('# ').replace('**', '')
        continue
    changes = []
    if index == 9:
        source = '\n'.join(line for line in source.splitlines() if not line.startswith(('from IPython.core.display', 'display(HTML')))
        changes.append('Removed notebook-only display styling for standalone Python.')
    if 'dtype=np.int)' in source:
        source = source.replace('dtype=np.int)', 'dtype=int)')
        changes.append('Replaced removed NumPy alias np.int with int.')
    tree = ast.parse(source)
    if tree.body and isinstance(tree.body[-1], ast.Expr):
        expr = tree.body[-1].value
        if not (isinstance(expr, ast.Call) and isinstance(expr.func, ast.Name) and expr.func.id == 'print'):
            tree.body[-1] = ast.Expr(ast.Call(ast.Name('_show', ast.Load()), [expr], []))
    ast.fix_missing_locations(tree)
    output = io.StringIO()
    def show(value):
        if value is not None:
            print(repr(value))
    namespace['_show'] = show
    with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
        exec(compile(tree, f'tutorial_cell_{index}', 'exec'), namespace)
    records.append(dict(cell=index, section=section, code=source, output=output.getvalue(), changes=changes))
    script.extend([f'\n# %% Cell {index}: {section}\n', ast.unparse(tree) + '\n'])
assert namespace['quicksort']([3,6,8,0,1,2,1]) == [0,1,1,2,3,6,8]
assert [x for x in [3,6,8,0,1,2,1] if x < 3] == [0,1,2,1]
np.testing.assert_array_equal(namespace['y'], [[2,2,4],[5,5,7],[8,8,10],[11,11,13]])
header = 'def _show(value):\n    if value is not None:\n        print(repr(value))\n\n'
(ROOT / 'python_tutorial.py').write_text(header + ''.join(script), encoding='utf-8')
result = dict(python=platform.python_version(), numpy=np.__version__, cells=len(records), assertions='3 passed', records=records)
(ROOT / 'python_results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
(ROOT / 'python_results.txt').write_text('\n'.join(f"CELL {r['cell']} | {r['section']}\n{r['code']}\nOUTPUT:\n{r['output']}" for r in records), encoding='utf-8')
print(f"Executed {len(records)} code cells; 3 result assertions passed. Python {platform.python_version()}, NumPy {np.__version__}.")
