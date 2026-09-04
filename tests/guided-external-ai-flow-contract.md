# Guided External-AI Flow Contract

DATE: 2026-09-04
STATUS: PRODUCT / UX CONTRACT

This document defines the behavior the public website and Master Director must preserve.

## Primary product rule

The website is a navigator and download hub. It is not the filmmaking chat.

A beginner should be able to start with one ordinary sentence in an external general-purpose AI chat after attaching the Master Director.

## The website must not regress to these defaults

1. Do not make Lesson 1 the primary starting route.
2. Do not require users to study award-winning shorts before receiving story help.
3. Do not require users to write their own premise, synopsis, screenplay, recurring-element list, storyboard method choice, shot package or generation prompts when the Master can reliably create them.
4. Do not hide where the actual conversation happens.
5. Do not assume a chat is persistent project storage.
6. Do not tell users merely to “save your work” without a filename and reason.
7. Do not tell users merely to “go generate this” without an explicit tool handoff.

## Required public routes

1. Start a new film or series.
2. Continue an existing project.
3. Learn why it works: optional 30-lesson course.

## Required first-run clarity

The site must make clear:

- download the Master Director;
- open ChatGPT, Gemini, Claude, Hermes or another capable general-purpose AI chat;
- attach/paste the Master there;
- paste the starter message there;
- media generation happens in image/video/audio tools;
- outputs return to the AI chat for selection/continuity/QC;
- persistent project files are saved outside the chat.

## Required Master behavior

The Master should maximize useful automation while preserving user approval at meaningful creative gates.

At persistence points it must output:

```text
SAVE THIS
FILE NAME:
WHAT IT CONTAINS:
WHY YOU NEED IT:
WHEN YOU WILL NEED IT AGAIN:
HOW TO SAVE IT:
```

At external-tool handoffs it must output:

```text
NEXT TOOL:
WHY YOU ARE GOING THERE:
WHAT TO UPLOAD:
WHAT TO PASTE:
HOW MANY VERSIONS / ATTEMPTS:
WHAT SUCCESS LOOKS LIKE:
WHAT TO SAVE THE WINNER AS:
WHAT TO BRING BACK TO THIS AI CHAT:
```

## Series continuity contract

Connected series use:

- `SERIES-BIBLE-v##.md` for permanent canon;
- `E##-END-STATE.md` for the latest narrative state after an episode;
- `ASSET-MANIFEST-v##.md` for exact approved file authorities;
- real locked reference media alongside those text files.

Editorial IDs must be episode-safe, for example `E01-SHOT-01` and `E02-SHOT-01`.

## Research contract

Award-winning animation research becomes internal quality intelligence. It is optional education, not mandatory homework.

Short-film research must not be presented as proof of every episodic-series heuristic. Stable principles, workflow decisions and changing tool facts must remain distinguishable.

## Preserved learning layer

The existing 30-lesson course remains available as `course.html` for users who want to understand the craft. It is not the required entrance to production.

## Current known limitation

The pre-existing downloadable ZIP was created before Master v2 and the new persistence templates. Do not present that archive as the authoritative current package until it is rebuilt.
