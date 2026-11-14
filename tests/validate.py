"""Valida el paquete y ensaya la topología Git sin red ni repositorios reales."""
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
skill = ROOT / 'gitflow-es' / 'SKILL.md'
body = skill.read_text(encoding='utf-8')
assert body.startswith('---\nname: gitflow-es\ndescription: ')
assert '\n---\n' in body
for doc in ROOT.rglob('*.md'):
    text = doc.read_text(encoding='utf-8')
    for link in re.findall(r'\]\(([^)]+)\)', text):
        if '://' not in link and not link.startswith('#'):
            assert (doc.parent / link.split('#')[0]).exists(), (doc, link)
print('OK: entrada y referencias locales del paquete')

with tempfile.TemporaryDirectory(prefix='gitflow-es-') as folder:
    cwd = Path(folder)

    def git(*args):
        result = subprocess.run(['git', *args], cwd=cwd, text=True,
                                capture_output=True, check=True)
        return result.stdout.strip()

    def commit(name, text, message):
        (cwd / name).write_text(text, encoding='utf-8')
        git('add', name)
        git('commit', '-m', message)
        return git('rev-parse', 'HEAD')

    git('init', '-b', 'main')
    git('config', 'user.name', 'Prueba local')
    git('config', 'user.email', 'prueba@example.invalid')
    commit('base.txt', 'base\n', 'chore: iniciar entorno temporal')
    git('branch', 'dev')
    git('branch', 'qa')
    git('switch', '-c', 'feat/pagos-parciales', 'dev')
    feature = commit('pagos.txt', 'pagos parciales\n', 'feat(pagos): agregar pagos parciales')
    for target, source in [('dev', 'feat/pagos-parciales'), ('qa', 'dev'), ('main', 'qa')]:
        git('switch', target)
        git('merge', '--no-ff', source, '-m', f'chore: integrar cambios en {target}')
        assert len(git('rev-list', '--parents', '-n', '1', 'HEAD').split()) == 3
        git('merge-base', '--is-ancestor', feature, target)
    print('OK: funcionalidad y promociones con historial conservado')

    git('switch', '-c', 'hotfix/error-de-acceso', 'main')
    hotfix = commit('acceso.txt', 'acceso corregido\n', 'fix(sesion): corregir el acceso')
    git('switch', 'main')
    git('merge', '--no-ff', 'hotfix/error-de-acceso', '-m', 'fix: integrar corrección urgente')
    commit('solo-produccion.txt', 'no propagar\n', 'chore: representar otro cambio en producción')
    for target in ['dev', 'qa']:
        branch = f'fix/propagar-acceso-a-{target}'
        git('switch', '-c', branch, target)
        git('cherry-pick', '-x', hotfix)
        assert (cwd / 'acceso.txt').read_text(encoding='utf-8') == 'acceso corregido\n'
        assert not (cwd / 'solo-produccion.txt').exists()
        assert hotfix in git('log', '-1', '--format=%B')
    print('OK: propagación selectiva de hotfix a dev y qa')

print('Las fusiones locales anteriores ensayan Git; no simulan aprobaciones de GitHub ni decisiones de los agentes.')
