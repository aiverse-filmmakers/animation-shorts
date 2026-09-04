# AI Animation Shorts Brain Library

## New to AI? Start here

Open `START-HERE.md` before using any Brain.

The beginner route is now intentionally simple:

1. download `master/MASTER-AI-ANIMATION-DIRECTOR.md`;
2. open a general-purpose AI chat such as ChatGPT, Claude, Gemini or Hermes;
3. attach the Master Brain;
4. paste the starter message from `START-HERE.md`;
5. describe what you want to make in ordinary language;
6. let the Master do as much of the filmmaking craft as it reliably can;
7. approve creative choices, run media-generation steps when instructed, and save the exact files it tells you to keep.

The website is the navigator and download hub. The general-purpose AI chat is the reasoning workspace. Image/video/audio tools execute media prompts. The user's own project folder is persistent memory.

## What these files are

Each Brain is a plain-text `.md` instruction file for a capable general-purpose AI chat.

They are not plugins, apps, image models or video models. They help an AI chat reason, write, plan, construct prompts, protect continuity and perform quality control.

Do not upload all specialist Brains together. Use the Master for the guided route, or one specialist alone for one focused job.

## Master Director

`master/MASTER-AI-ANIMATION-DIRECTOR.md`

The Master is the default route. It can begin from:

- one rough idea;
- a request for story ideas;
- an existing script;
- a partial project;
- or saved continuity files from an earlier episode.

It is designed to ask only for decisions that materially change the current deliverable. It should not make a beginner manually repeat research or filmmaking work that it can reasonably perform itself.

## Persistence files

### Active Project State

`PROJECT-STATE-TEMPLATE.md`

Use this for the current film or episode's active production state.

### Series Bible

`SERIES-BIBLE-TEMPLATE.md`

Use this for connected episodic work. It stores permanent canon: series premise, world rules, recurring character facts, visual language, audio rules and long-term story information.

### Episode End State

`EPISODE-END-STATE-TEMPLATE.md`

Create one after each completed episode. It records what is true now so the next episode does not reset character knowledge, relationships, injuries, props, locations or unresolved threads.

### Asset Manifest

`ASSET-MANIFEST-TEMPLATE.md`

Maps stable IDs such as `CHAR-01`, `PROP-01`, `WORLD-01` and `E01-SHOT-01` to the exact approved filenames that act as visual or production authority.

## Stable IDs

Recurring series assets can keep global IDs:

- `CHAR-01`
- `PROP-01`
- `WORLD-01`
- `AUDIO-01`

Episode editorial material should be namespaced:

- `E01-SHOT-01`
- `E01-GB-01`
- `E02-SHOT-01`

Grid panel numbers, editorial shot IDs, generation blocks and takes are different layers and must not be treated as interchangeable.

## Canonical specialist Brains

### Story

1. `story/00-AWARD-WINNING-ANIMATION-STORY-BRAIN.md` evaluates or repairs story logic without copying existing films.
2. `story/01-IDEA-STORY-ARCHITECT.md` turns minimal input into original directions.
3. `story/02-SYNOPSIS-ARCHITECT.md` builds or repairs a compact visual synopsis.
4. `story/03-ANIMATION-SCREENWRITER.md` writes an economical, AI-producible screenplay.

### Pre-production

5. `preproduction/04-CONSISTENCY-REFERENCE-DIRECTOR.md` reads the script and identifies only the elements worth visually locking.
6. `preproduction/05-STORYBOARD-DIRECTOR.md` chooses the appropriate AI-Verse storyboard method and creates the plan.
7. `preproduction/06-SHOT-SEQUENCE-PACKAGER.md` separates scenes/sequences, editorial shots and AI generation blocks.
8. `preproduction/07-KEYFRAME-FRAME-DIRECTOR.md` plans approved reference, start, end and key frames.

### Production

9. `production/08-MOTION-ANIMATION-DIRECTOR.md` turns an approved shot into a route-aware video-generation instruction.
10. `production/09-AUDIO-DIALOGUE-CONTINUITY-DIRECTOR.md` protects dialogue, voice, ambience, effects, silence and music continuity.

### Post-production

11. `post/10-EDIT-PACING-DIRECTOR.md` plans and diagnoses the rough cut, rhythm and emotional pacing.
12. `post/11-FINAL-FILM-CRITIC-QC.md` checks story, originality, continuity, motion, audio, evidence and delivery.

## How the tools connect

```text
WEBSITE
Choose route → download Brain → see what to attach and paste

GENERAL AI CHAT
Develop story → write script → extract continuity → plan boards/shots → write prompts → QC

IMAGE / VIDEO / AUDIO TOOL
Upload exact approved references → paste exact prompt → create versions

GENERAL AI CHAT
Bring result back → inspect what is accessible → compare → select → lock → plan next action

VIDEO EDITOR
Assemble → sound → review → export

PROJECT FOLDER
Keep the continuity files and approved media that allow future chats or episodes to resume
```

At every external-tool handoff, the Master should state:

- next tool;
- what to upload;
- what to paste;
- how many attempts;
- what success looks like;
- what to save the winner as;
- what to bring back to the AI chat.

At every important persistence point, it should state:

- `SAVE THIS`;
- filename;
- what it contains;
- why it is needed;
- when it is needed again;
- how to save it.

## AI-Verse methods preserved

The toolkit keeps the AI-Verse order: protect important recurring elements with references, establish approved visual anchors, think visually with grids, select/extract approved frames, then animate.

It preserves Scene Imagination, Freeze Multi-Angle, Story Progression, A → B Bridge and Commercial / Production Ready storyboard logic; keeps editorial shots separate from model generations; uses simple motion language when sufficient; supports start-frame and start/end workflows; uses generate → compare → select → lock; and keeps `Audio: no music` as a reasoned continuity safeguard when continuous music will be built later in the edit.

## Research boundary

Award-winning animation research is intended to become internal story intelligence, not mandatory beginner homework. It supports transferable mechanisms such as emotional clarity, visible wants/obstacles, turns, choices, setup/payoff and earned endings. It does not justify copying protected characters, plots, dialogue, shots or distinctive artist styles.

Short-film award research also does not by itself prove every episodic-series heuristic. The Master separates stable story principles from series workflow logic and from changing tool/model facts.

## Research and tests

- `research/sprint-2-methodology-and-brain-architecture.md`
- `research/official-ai-film-workflows-2026-09-04.md`
- `research/current-2026-capability-addendum-2026-09-04.md`
- `research/creator-ai-film-case-studies-2026-09-04.md`
- `tests/last-drop-end-to-end.md`
- `tests/standalone-brain-contracts.md`

The manually authored continuity fixture illustrates the intended handoff logic. It is not recorded proof that every Brain has been run end-to-end through every external AI and media tool.
