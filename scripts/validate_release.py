#!/usr/bin/env python3
from pathlib import Path
import re, sys, yaml

root=Path(__file__).resolve().parents[1]; errors=[]
version=(root/'VERSION').read_text().strip()
if not re.fullmatch(r'\d+\.\d+\.\d+',version): errors.append(f'VERSION is not semantic: {version}')
required=[
 'scripts/validate_release_integrity.py','scripts/validate_v1_stable_controls.py','scripts/validate_v1_readiness.py',
 'PROJECT-STATUS.yaml','CITATION.cff',f'model/releases/v{version}.yaml',
 f'release/RELEASE-NOTES-v{version}.md',f'release/MANIFEST-v{version}.md',f'release/CHECKLIST-v{version}.md',
 f'release/EVIDENCE-INVENTORY-v{version}.md',f'release/REQUIREMENTS-INVENTORY-v{version}.md',
 f'release/CONFORMANCE-COVERAGE-v{version}.md',f'release/VALIDATION-NOTES-v{version}.md']
for p in required:
 if not (root/p).exists(): errors.append(f'Missing {p}')
for p in ['PROJECT-STATUS.yaml','CITATION.cff',f'model/releases/v{version}.yaml']:
 try: yaml.safe_load((root/p).read_text())
 except Exception as e: errors.append(f'Invalid YAML {p}: {e}')
readme=(root/'README.md').read_text()
if f'v{version}' not in readme: errors.append('README release version not updated')
status=yaml.safe_load((root/'PROJECT-STATUS.yaml').read_text()) or {}
if str(status.get('version'))!=version: errors.append('PROJECT-STATUS.yaml version does not match VERSION')
if version.startswith('1.') and status.get('project',{}).get('maturity')!='stable': errors.append('v1.x release must declare stable project maturity')
model=yaml.safe_load((root/f'model/releases/v{version}.yaml').read_text()) or {}
if str(model.get('framework_version'))!=version: errors.append('release model framework_version does not match VERSION')
if model.get('evidence_maturity')!='E1': errors.append('v1.0.0 must preserve current E1 evidence boundary')
if errors:
 print('Release validation failed:'); [print('- '+e) for e in errors]; sys.exit(1)
print(f'Release validation passed: v{version} Stable Framework Specification payload is internally coherent')
