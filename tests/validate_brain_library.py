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
COMPAT={
 '00-ai-animation-studio.md':'master/MASTER-AI-ANIMATION-DIRECTOR.md',
 '01-award-story-analyst.md':'story/00-AWARD-WINNING-ANIMATION-STORY-BRAIN.md',
 '02-synopsis-builder.md':'story/02-SYNOPSIS-ARCHITECT.md',
 '03-short-script-builder.md':'story/03-ANIMATION-SCREENWRITER.md',
 '04-30-second-chunk-planner.md':'preproduction/06-SHOT-SEQUENCE-PACKAGER.md',
 '05-character-world-continuity.md':'preproduction/04-CONSISTENCY-REFERENCE-DIRECTOR.md',
 '06-storyboard-shot-planner.md':'preproduction/05-STORYBOARD-DIRECTOR.md',
 '07-ai-animation-director.md':'production/08-MOTION-ANIMATION-DIRECTOR.md',
 '08-sound-and-finish-director.md':'production/09-AUDIO-DIALOGUE-CONTINUITY-DIRECTOR.md',
 '09-originality-and-qc.md':'post/11-FINAL-FILM-CRITIC-QC.md',
 '10-portfolio-film-review.md':'post/11-FINAL-FILM-CRITIC-QC.md',
 '11-visual-metaphor-builder.md':'master/MASTER-AI-ANIMATION-DIRECTOR.md',
 '12-ai-suitability-and-shot-budget.md':'preproduction/06-SHOT-SEQUENCE-PACKAGER.md',
 '13-festival-readiness-and-director-statement.md':'post/11-FINAL-FILM-CRITIC-QC.md'}

for rel in CANONICAL:
 p=B/rel; assert p.exists(),rel; text=p.read_text()
 for marker in ['NAME:','VERSION: 1.1','LAST REVIEWED:','MODEL DEPENDENCY: GENERAL-PURPOSE','## Read this before using the brain','### Activation','### Capability boundary','### Rights and privacy boundary','CAN RUN WITHOUT ANOTHER BRAIN: YES','## Story DNA','## Standalone operating kernel','## Output contract','SAVE AS:','LOCKS USED:','NEW DECISIONS:','OPEN QUESTIONS:','NEXT BRAIN OR TOOL:','NEXT STARTER MESSAGE:','NEXT HANDOFF:','### Minimum-input fallback','### Stable identity','### Evidence and route honesty']:
  assert marker in text,f'{rel}: missing {marker}'
 assert 'MUST PRODUCE:' in text and 'ESCALATE WHEN:' in text
 assert 'confidential client work' in text and 'likenesses' in text and 'TO VERIFY' in text
 if rel.startswith('master/'):
  assert 'Use only this Master brain' in text
  assert 'Use only this specialist brain' not in text
 else:
  assert 'Use only this specialist brain' in text
assert 'SCENE-01 | STORY TIME' in (B/'story/03-ANIMATION-SCREENWRITER.md').read_text()
assert len({(B/x).read_text() for x in CANONICAL})==len(CANONICAL)

def text_block(text): return re.search(r'```text\n(.*?)\n```',text,re.S).group(1)
template_schema=text_block((B/'PROJECT-STATE-TEMPLATE.md').read_text())
master=(B/'master/MASTER-AI-ANIMATION-DIRECTOR.md').read_text()
master_state=re.search(r'## Project memory\n(.*?)\n## Progressive route',master,re.S).group(1)
assert text_block(master_state)==template_schema,'Master Project State differs from template'

onboarding='\n'.join((B/x).read_text() for x in GUIDES)
for concept in ['plain text','does not run by itself','general-purpose AI chat','image generator','video generator','video editor','paste','new chat','does not automatically remember','privacy','right to use','PROJECT-STATE-TEMPLATE.md','Do not upload all 13 brains']:
 assert concept.lower() in onboarding.lower(),concept

for old,target in COMPAT.items():
 text=(B/old).read_text();assert '# Previous-version compatibility file' in text,old
 assert target in text and (B/target).exists(),(old,target)
 legacy=B/'legacy'/old
 if legacy.exists():
  ltext=legacy.read_text();assert '# Compatibility link only' in ltext,old
  assert f'https://aiverse-filmmakers.github.io/animation-shorts/assets/brains/{target}' in ltext,old
assert {p.name for p in (B/'legacy').glob('*.md')}==set(list(COMPAT)[:11])

s=(ROOT/'index.html').read_text()
assert s.count('<style>')==s.count('</style>')==1
assert '<style>.brain-library' not in s
for meta in ['<link rel="canonical" href="https://aiverse-filmmakers.github.io/animation-shorts/">','<meta property="og:title" content="AI Animation Shorts | Story-First AI Filmmaking Course">','<meta name="twitter:card" content="summary_large_image">']:
 assert meta in s,meta
m=re.search(r'<script id="course-data" type="application/json">(.*?)</script>',s,re.S);assert m
D=json.loads(m.group(1));assert len(D['lessons'])==30
for lesson in D['lessons']:
 assert lesson.get('brain'),lesson['number'];assert (B/lesson['brain']).exists(),lesson['brain']
 assert lesson['status'] in {'practice','research','tested'},lesson['number']
 assert '**Status:' not in lesson['body'],f"lesson {lesson['number']} duplicates/contradicts rendered status"
for phrase in ['FIRST TIME USING AI?','Four tool jobs','Open the beginner guide','Download Project State','The brain directs. The media tool generates.','Optional AI helpers','Build a simple rough cut','Optional specialist for this lesson','Beginners can continue without downloading it.']:
 assert phrase in s,phrase
for stale in ['Build a rough vertical edit','Use this brain with the lesson','Shot 01 reference map.','Shot 02 reference map.','Shot 03 reference map.','Story turn and Shot 04 reference map.','20-shot-animated.mp4','21-reaction-clip.mp4','22-story-transition.mp4','23-final-moment.mp4']:
 assert stale not in s,stale
assert 'real-estate' not in s.lower()

z=ROOT/'assets/ai-animation-shorts-brain-library.zip';assert z.exists()
with ZipFile(z) as f:
 names=set(f.namelist());assert names==EXPECTED,(sorted(names-EXPECTED),sorted(EXPECTED-names))
 for name in EXPECTED:
  source=ROOT/name if not name.startswith('brains/') else B/name.removeprefix('brains/')
  assert f.read(name)==source.read_bytes(),f'ZIP stale: {name}'
 assert not any('/legacy/' in x for x in names)
 assert not any(re.fullmatch(r'brains/\d{2}-.*\.md',x) for x in names)

sample=(ROOT/'tests/last-drop-end-to-end.md').read_text().lower()
for x in ['manually authored static example','intended continuity invariants','the last drop','character lock','prop lock','world lock','storyboard','generation blocks','audio: no music','shot-09','final image']:
 assert x in sample,x
contract=(ROOT/'tests/beginner-first-run-contract.md').read_text()
for x in ['SHOT-##','TOOL / MODEL / DATE','ACTUAL DURATION','first, middle and last screenshots','Final film `PASS`']:
 assert x in contract,x
print({'status':'PASS','canonical_brains':len(CANONICAL),'lessons':len(D['lessons']),'zip_entries':len(EXPECTED),'onboarding':'PASS','beginner_contract':'PASS','metadata':'PASS','compatibility':'PASS','project_state':'PASS'})
