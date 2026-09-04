from pathlib import Path
from zipfile import ZipFile
import json,re

ROOT=Path(__file__).resolve().parents[1]
B=ROOT/'assets'/'brains'
canonical=[
 'story/00-AWARD-WINNING-ANIMATION-STORY-BRAIN.md','story/01-IDEA-STORY-ARCHITECT.md','story/02-SYNOPSIS-ARCHITECT.md','story/03-ANIMATION-SCREENWRITER.md',
 'preproduction/04-CONSISTENCY-REFERENCE-DIRECTOR.md','preproduction/05-STORYBOARD-DIRECTOR.md','preproduction/06-SHOT-SEQUENCE-PACKAGER.md','preproduction/07-KEYFRAME-FRAME-DIRECTOR.md',
 'production/08-MOTION-ANIMATION-DIRECTOR.md','production/09-AUDIO-DIALOGUE-CONTINUITY-DIRECTOR.md','post/10-EDIT-PACING-DIRECTOR.md','post/11-FINAL-FILM-CRITIC-QC.md','master/MASTER-AI-ANIMATION-DIRECTOR.md']
for rel in canonical:
 p=B/rel; assert p.exists(), rel
 s=p.read_text()
 for marker in ['NAME:','VERSION:','LAST REVIEWED:','MODEL DEPENDENCY:','CAN RUN ALONE: YES','## Story DNA','## Standalone operating kernel','## Output contract','LOCKS USED:','NEW DECISIONS:','OPEN QUESTIONS:','NEXT HANDOFF:']:
  assert marker in s, f'{rel}: missing {marker}'
 assert 'MUST PRODUCE:' in s and 'ESCALATE WHEN:' in s
assert len({p.read_text() for p in [B/x for x in canonical]})==len(canonical)

s=(ROOT/'index.html').read_text()
m=re.search(r'<script id="course-data" type="application/json">(.*?)</script>',s,re.S); assert m
D=json.loads(m.group(1)); assert len(D['lessons'])==30
for l in D['lessons']:
 assert l.get('brain'), l['number']
 assert (B/l['brain']).exists(), l['brain']
assert 'og:title' in s and 'twitter:card' in s and 'rel="canonical"' in s
assert 'real-estate' not in s.lower()
for asset in ['assets/favicon.svg','robots.txt','sitemap.xml','assets/ai-animation-shorts-brain-library.zip']:
 assert (ROOT/asset).exists(), asset

z=ROOT/'assets/ai-animation-shorts-brain-library.zip'
with ZipFile(z) as f:
 names=set(f.namelist())
 for rel in canonical: assert 'brains/'+rel in names, rel
 for rel in ['brains/README.md','research/sprint-2-methodology-and-brain-architecture.md','tests/last-drop-end-to-end.md']:
  assert rel in names, rel
 assert len(names)>=40

sample=(ROOT/'tests/last-drop-end-to-end.md').read_text()
for x in ['The Last Drop','CHARACTER LOCK','PROP LOCK','WORLD LOCK','STORYBOARD','GENERATION BLOCKS','Audio: no music','S9','final image']:
 assert x.lower() in sample.lower(), x
print({'status':'PASS','canonical_brains':len(canonical),'lessons':len(D['lessons']),'zip_entries':len(names),'sample':'PASS','metadata':'PASS'})
