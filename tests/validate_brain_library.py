from pathlib import Path
from zipfile import ZipFile
import json,re

ROOT=Path(__file__).resolve().parents[1]
B=ROOT/'assets'/'brains'
CANONICAL=[
 'story/00-AWARD-WINNING-ANIMATION-STORY-BRAIN.md','story/01-IDEA-STORY-ARCHITECT.md','story/02-SYNOPSIS-ARCHITECT.md','story/03-ANIMATION-SCREENWRITER.md',
 'preproduction/04-CONSISTENCY-REFERENCE-DIRECTOR.md','preproduction/05-STORYBOARD-DIRECTOR.md','preproduction/06-SHOT-SEQUENCE-PACKAGER.md','preproduction/07-KEYFRAME-FRAME-DIRECTOR.md',
 'production/08-MOTION-ANIMATION-DIRECTOR.md','production/09-AUDIO-DIALOGUE-CONTINUITY-DIRECTOR.md','post/10-EDIT-PACING-DIRECTOR.md','post/11-FINAL-FILM-CRITIC-QC.md','master/MASTER-AI-ANIMATION-DIRECTOR.md']
GUIDES=['START-HERE.md','PROJECT-STATE-TEMPLATE.md','README.md']
RESEARCH=sorted(str(p.relative_to(ROOT)) for p in (ROOT/'research').glob('*.md'))
TEST_DOCS=['tests/last-drop-end-to-end.md','tests/standalone-brain-contracts.md','tests/beginner-first-run-contract.md']
EXPECTED={*(f'brains/{x}' for x in GUIDES),*(f'brains/{x}' for x in CANONICAL),*RESEARCH,*TEST_DOCS}

for rel in CANONICAL:
 p=B/rel; assert p.exists(),rel; text=p.read_text()
 for marker in ['NAME:','VERSION: 1.1','LAST REVIEWED:','MODEL DEPENDENCY: GENERAL-PURPOSE','## Read this before using the brain','### Activation','### Capability boundary','CAN RUN WITHOUT ANOTHER BRAIN: YES','## Story DNA','## Standalone operating kernel','## Output contract','SAVE AS:','LOCKS USED:','NEW DECISIONS:','OPEN QUESTIONS:','NEXT BRAIN OR TOOL:','NEXT STARTER MESSAGE:','NEXT HANDOFF:']:
  assert marker in text,f'{rel}: missing {marker}'
 assert 'MUST PRODUCE:' in text and 'ESCALATE WHEN:' in text
 if rel.startswith('master/'):
  assert 'Use only this Master brain' in text
  assert 'Use only this specialist brain' not in text
 else:
  assert 'Use only this specialist brain' in text
assert 'SCENE-01 | STORY TIME' in (B/'story/03-ANIMATION-SCREENWRITER.md').read_text()
assert len({(B/x).read_text() for x in CANONICAL})==len(CANONICAL)

onboarding='\n'.join((B/x).read_text() for x in GUIDES)
for concept in ['plain text','does not run by itself','general-purpose AI chat','image generator','video generator','video editor','paste','new chat','does not automatically remember','privacy','right to use','PROJECT-STATE-TEMPLATE.md','Do not upload all 13 brains']:
 assert concept.lower() in onboarding.lower(),concept

s=(ROOT/'index.html').read_text()
assert s.count('<style>')==s.count('</style>')==1
assert '<style>.brain-library' not in s
m=re.search(r'<script id="course-data" type="application/json">(.*?)</script>',s,re.S);assert m
D=json.loads(m.group(1));assert len(D['lessons'])==30
for lesson in D['lessons']:
 assert lesson.get('brain'),lesson['number'];assert (B/lesson['brain']).exists(),lesson['brain']
for phrase in ['FIRST TIME USING AI?','Four tool jobs','Open the beginner guide','Download Project State','The brain directs. The media tool generates.','Optional AI helpers','Build a simple rough cut']:
 assert phrase in s,phrase
assert 'Build a rough vertical edit' not in s
assert 'real-estate' not in s.lower()

z=ROOT/'assets/ai-animation-shorts-brain-library.zip'
assert z.exists()
with ZipFile(z) as f:
 names=set(f.namelist());assert names==EXPECTED,(sorted(names-EXPECTED),sorted(EXPECTED-names))
 for name in EXPECTED:
  source=ROOT/name if not name.startswith('brains/') else B/name.removeprefix('brains/')
  assert f.read(name)==source.read_bytes(),f'ZIP stale: {name}'
 assert not any('/legacy/' in x for x in names)
 assert not any(re.fullmatch(r'brains/\d{2}-.*\.md',x) for x in names)

sample=(ROOT/'tests/last-drop-end-to-end.md').read_text().lower()
for x in ['the last drop','character lock','prop lock','world lock','storyboard','generation blocks','audio: no music','shot-09','final image']:
 assert x in sample,x
contract=(ROOT/'tests/beginner-first-run-contract.md').read_text()
for x in ['SHOT-##','TOOL / MODEL / DATE','ACTUAL DURATION','first, middle and last screenshots','Final film `PASS`']:
 assert x in contract,x
print({'status':'PASS','canonical_brains':len(CANONICAL),'lessons':len(D['lessons']),'zip_entries':len(EXPECTED),'onboarding':'PASS','beginner_contract':'PASS','metadata':'PASS'})
