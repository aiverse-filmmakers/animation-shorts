# Hermes Course Website Systems Note

Status: internal architecture note for Hermes. Do not link this file from the public website navigation.
Last updated: 2026-09-04

## Why this file exists

This is not merely a changelog. It records the product reasoning behind the AI Animation Shorts restructure so the same logic can improve future AI-enabled course websites and the Hermes course-building skill.

## Core product correction

A course website that embeds reusable AI intelligence should not force beginners to manually repeat the cognitive work already encoded in the AI brains.

Research should become **compiled intelligence**.

The visitor supplies:

- intent;
- taste;
- constraints the AI cannot know;
- approvals;
- access to external generation/editing tools.

The AI should handle, wherever reliable:

- story development;
- script structure;
- continuity extraction;
- deciding which elements deserve references;
- storyboard-method selection;
- shot and generation packaging;
- prompt construction;
- handoffs;
- QC;
- persistence instructions.

This means the question for every lesson is not only “what should we teach?” but also:

> Can the AI reliably perform this step for the beginner instead of making the beginner learn it first?

If yes, automation should normally become the default production route and the educational explanation should remain optional.

## Website versus AI responsibilities

The website is a navigator and download hub, **not the AI runtime**.

The public website must make the physical workflow obvious:

1. user visits website;
2. user downloads the correct Brain;
3. user opens an external general-purpose AI chat such as ChatGPT, Gemini, Claude or Hermes;
4. user attaches/pastes the Brain there;
5. user sends the starter message there;
6. AI chat performs reasoning and produces decisions/prompts;
7. user moves into image/video/audio/editing tools only when explicitly instructed;
8. user returns outputs to the AI chat for selection, continuity and QC;
9. durable project files are saved outside the chat.

The external general-purpose AI chat is the reasoning engine.
Image/video/audio tools are execution engines.
The user's project folder is persistent memory.

Never imply the static website contains a chat when it does not.

## Primary UX hierarchy implemented

The old public entry point made the 30-lesson course the default route.

The new hierarchy is:

### Primary

**Start a new film or series** with the Master Director.

### Secondary

**Continue an existing project** from saved continuity files.

### Optional education

**Learn why it works** through the preserved 30-lesson course.

The original course was preserved as `course.html` before replacing the root experience.

This is deliberate: existing education is not deleted, but it is no longer a prerequisite to obtaining the benefit of the AI intelligence.

## Main design principle preserved

Do not redesign a product visually when the real problem is information architecture.

The new root page intentionally preserves the existing AI-Verse design DNA:

- neutral white/black backgrounds;
- restrained green accent;
- large editorial typography;
- rounded cards;
- subtle borders;
- light/dark mode;
- generous spacing;
- minimal premium feel.

The change is structural, not cosmetic.

## Master Director behavior implemented

`assets/brains/master/MASTER-AI-ANIMATION-DIRECTOR.md` was upgraded to v2.0.

The central rule is:

> The AI handles craft. The user handles intent, taste, approval and media-tool execution.

The Master must not turn known research into beginner homework.

Examples:

If the user says:

`Give me three ideas for a six-episode anime series, two minutes each.`

The AI should use the story intelligence and create the directions.

If the user says:

`Write a five-minute anime about a samurai protecting a girl through a deadly valley.`

The AI should write the story/script instead of asking the beginner to first learn screenwriting.

The AI still asks questions when an answer genuinely changes the current deliverable, such as an ambiguous runtime or whether episodes are connected.

## Mandatory save logic implemented

A chat is not the archive.

Every artifact that matters later must be accompanied by this contract:

```text
SAVE THIS
FILE NAME:
WHAT IT CONTAINS:
WHY YOU NEED IT:
WHEN YOU WILL NEED IT AGAIN:
HOW TO SAVE IT:
```

Do not reduce this to “remember to save your work.”

The `HOW TO SAVE IT` field matters because beginners may not know how to turn an AI response into a persistent `.md` file.

If the AI can provide a downloadable file, it may do so.
Otherwise it should provide one complete copyable Markdown block and tell the user to save it under the exact filename.

## Mandatory tool-handoff logic implemented

At every transition out of the AI chat, the user must know exactly what happens next.

Required structure:

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

This pattern is reusable far beyond filmmaking.

Whenever a course workflow crosses apps, every handoff should explicitly define:

- source artifact;
- destination tool;
- action;
- expected output;
- acceptance criteria;
- saved output identity;
- return path.

This turns a collection of tutorials into a stateful production system.

## Persistence model implemented

### 1. Active Project State

`PROJECT-STATE-TEMPLATE.md`

This is the compact working state of the film or current episode.

It now distinguishes:

- standalone vs series episode;
- series title;
- episode ID;
- active story/visual/production/audio/edit state.

### 2. Series Bible

`SERIES-BIBLE-TEMPLATE.md`

Purpose: permanent canon across connected episodes.

Contains:

- series premise;
- long-term dramatic question;
- character canon;
- world rules;
- recurring props;
- visual language;
- audio language;
- episode map;
- permanent canon added after release.

Only permanent canon belongs here.

### 3. Episode End State

`EPISODE-END-STATE-TEMPLATE.md`

Purpose: capture what became true at the exact end of one episode.

Contains:

- physical states;
- emotional states;
- what each character now knows;
- what they still do not know;
- relationship changes;
- items lost/broken/gained;
- location/world changes;
- resolved/open threads;
- exact next-episode start state.

This prevents Episode 2 from resetting Episode 1.

### 4. Asset Manifest

`ASSET-MANIFEST-TEMPLATE.md`

Purpose: map stable semantic IDs to the exact approved files that act as authority.

A text description alone is not enough when the actual approved image is the visual source of truth.

Record both:

- stable ID;
- exact filename;
- status/authority.

## Identity logic implemented

Recurring assets keep global IDs when appropriate:

- `CHAR-01`
- `PROP-01`
- `WORLD-01`
- `AUDIO-01`

Episode editorial material uses episode namespaces:

- `E01-SHOT-01`
- `E01-GB-01`
- `E01-TAKE-01`
- `E02-SHOT-01`

Never conflate:

- grid panel number;
- editorial shot ID;
- generation block ID;
- generation take ID.

This matters because AI workflows frequently collapse all four concepts into “shot,” which creates continuity and packaging errors.

## Research logic

Award-winning animation research should be used internally to strengthen:

- ideas;
- scripts;
- turns;
- endings;
- story diagnosis.

Do not send the user away to repeat that research unless they explicitly want to learn it.

Also do not overclaim the research.

Short-film award research supports transferable short-story principles. It does **not automatically validate every episodic-series heuristic**.

Keep separate:

1. source-supported research;
2. stable general story principles;
3. workflow architecture chosen for production control;
4. changing tool/model facts.

## Beginner abstraction rule

Do not expose professional taxonomy before it changes the user's action.

A beginner does not need to know whether they need a premise, synopsis, beat sheet, shot package or continuity ledger before starting.

The system should decide internally and surface:

- the useful result;
- the decision requiring approval;
- the next concrete action.

Explain terminology only when it helps the next action or when the user asks to learn it.

## Preserve human control at meaningful gates

Automation is not the same as silently deciding everything.

The user should still control:

- which idea they prefer;
- whether a story direction feels right;
- whether a character design is approved;
- which media generation becomes the keeper;
- whether an intentional canon change is accepted.

Use explicit states:

- `PROPOSED`
- `APPROVED`
- `LOCKED`

Never silently convert a failed model output into new canon.

## Public routes implemented

Root `index.html` now provides:

- Start a new film or series;
- Continue an existing project;
- Learn why it works;
- exact starter message;
- exact continuation message;
- direct Master download;
- direct continuity-template downloads;
- explanation of website vs AI vs generator vs editor roles;
- explicit persistence philosophy.

`course.html` preserves the previous 30-lesson course experience.

`assets/brains/START-HERE.md` mirrors the real external-AI workflow in more detail.

`tests/guided-external-ai-flow-contract.md` records the regression rules so future edits do not accidentally restore the old course-first logic.

## What was intentionally NOT done

1. The 30 lessons were not deleted.
2. The specialist Brain library was not discarded.
3. The visual brand was not replaced.
4. Series workflow logic was not falsely presented as award-research proof.
5. The website was not turned into an embedded AI chat.

## Current known maintenance item

The pre-existing `assets/ai-animation-shorts-brain-library.zip` was built before Master v2 and the new persistence templates.

Until rebuilt, it must not be treated as the authoritative current package. Prefer direct downloads from the root site / Brain guide.

Future Hermes maintenance should either rebuild that archive from canonical current files or remove stale public claims that it is the complete current package.

## Course-site skill lesson

For future AI-enabled course websites, use this decision tree:

### Question 1

Is the step fundamentally educational, or is it work the AI can already perform reliably?

If AI can perform it, make AI execution the default and education optional.

### Question 2

Does the workflow cross tools?

If yes, define an explicit handoff contract.

### Question 3

Will the result matter in another chat/session/month?

If yes, define a persistent artifact, stable filename and authority rule.

### Question 4

Can several concepts be confused as one object?

If yes, create stable typed IDs and preserve layer boundaries.

### Question 5

Is the user being asked for knowledge they do not need in order to make the next decision?

If yes, move that complexity into the AI's internal reasoning and surface only the useful output.

### Question 6

Is the site visually weak, or structurally weak?

Do not solve an information-architecture problem by redesigning the aesthetic.

## General reusable architecture

```text
USER INTENT
    ↓
WEBSITE ROUTER
brain + starter message + required files
    ↓
EXTERNAL AI REASONING
create / decide / plan / prompt / QC
    ↓
EXPLICIT HANDOFF
source → destination → instruction → success criteria
    ↓
MEDIA / EXTERNAL TOOL EXECUTION
    ↓
RETURN + SELECT + LOCK
    ↓
PERSISTENT ARTIFACTS
    ↓
NEXT STAGE OR FUTURE SESSION
```

This logic should inform Hermes when it updates or creates future AI-assisted course websites.
