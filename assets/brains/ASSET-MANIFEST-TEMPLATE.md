# Asset Manifest Template

Use this to map stable project IDs to the exact approved files that future chats and episodes must reuse.

```text
PROJECT / SERIES TITLE:
MANIFEST VERSION:
LAST UPDATED:

CHARACTERS
CHAR-01
NAME:
FILE:
STATUS: PROPOSED / APPROVED / LOCKED
USED IN:
NOTES:

PROPS / OBJECTS
PROP-01
NAME:
FILE:
STATUS:
USED IN:
NOTES:

WORLDS / LOCATIONS
WORLD-01
NAME:
FILE:
STATUS:
USED IN:
NOTES:

STORYBOARDS
E01-STORYBOARD
FILE:
STATUS:

KEYFRAMES
E01-SHOT-01-START
FILE:
STATUS:

VIDEO SHOTS
E01-SHOT-01
SELECTED FILE:
SOURCE FRAME(S):
MODEL / TOOL / DATE:
STATUS:

AUDIO
AUDIO-01
NAME:
FILE:
SOURCE / RIGHTS:
STATUS:

SUPERSEDED ASSETS
ID:
OLD FILE:
REPLACED BY:
REASON:
```

## Rules

1. Global recurring assets keep global IDs such as `CHAR-01`, `PROP-01`, `WORLD-01`.
2. Episode editorial assets use episode-safe IDs such as `E01-SHOT-01`, `E02-SHOT-01`.
3. Grid panel numbers, editorial shot IDs, generation blocks and takes are different things.
4. Never silently point a locked ID at a failed generation.
5. When a locked asset is intentionally redesigned, record the superseded file and approval reason.
