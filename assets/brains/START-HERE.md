# Start Here: Create With the AI Animation Director

If you have never written a script, directed a film or used AI filmmaking tools, start here.

## The most important thing to understand

**This website does not contain the filmmaking chat.**

The website gives you the Brain files, the steps and the continuity templates. The actual conversation happens in a general-purpose AI chat such as ChatGPT, Claude, Gemini, Hermes or another capable model.

Think of the workflow like this:

```text
WEBSITE
Download the Brain and see what to do next.

GENERAL AI CHAT
The Brain does the reasoning: ideas, story, script, continuity, storyboard decisions, shot plans, prompts and QC.

IMAGE / VIDEO / AUDIO TOOLS
You execute the prompts and create media.

GENERAL AI CHAT
You bring the results back. The AI checks them and directs the next step.

YOUR PROJECT FOLDER
You keep the files that let the project survive a new chat, a new month or a new episode.
```

## What an AI Brain is

An AI Brain is a Markdown file ending in `.md`. Markdown is plain text with headings. The file contains working instructions for an AI chat.

It is not:

- an app;
- an image or video generator;
- a plugin you install;
- a finished media prompt;
- the website itself.

You attach or paste the Brain into a capable AI chat. The AI then takes on the filmmaking role described by the file.

## The easiest route

For a new film or series, use only:

`master/MASTER-AI-ANIMATION-DIRECTOR.md`

Do not upload all specialist brains together. The Master can guide the whole project. Specialist brains are optional when you want one focused job in a separate chat.

## Step 1: make one project folder

Before starting, create a folder on your computer or cloud drive for the project.

Example:

```text
SAMURAI-SERIES/
```

This folder is your real long-term memory. A chat is not your production archive.

## Step 2: open a general-purpose AI chat

Examples include ChatGPT, Claude, Gemini and Hermes.

Start a new chat. Attach:

`MASTER-AI-ANIMATION-DIRECTOR.md`

If the app does not accept `.md`, open the file in a text editor, copy all of it and paste it into the chat before the starter message.

## Step 3: send this starter message

Copy this into the AI chat, then replace the last line with your own idea.

```text
Read the attached Master AI Animation Director Markdown file as the working instructions for this chat.

I am a beginner. I may not know screenwriting, directing, story structure or AI filmmaking terminology.

Do as much of the filmmaking thinking as you reasonably can using the knowledge inside the Brain. Do not make me manually perform or study a filmmaking task when you can reliably perform it for me.

Guide me one useful step at a time. Ask only questions whose answers materially change what you are about to create.

Whenever we create something I will need later, clearly tell me:
SAVE THIS
FILE NAME
WHAT IT CONTAINS
WHY I NEED IT
WHEN I WILL NEED IT AGAIN
HOW TO SAVE IT

Whenever I need to leave this chat and use an image generator, video generator, audio tool or editor, clearly tell me:
NEXT TOOL
WHAT TO UPLOAD
WHAT TO PASTE
HOW MANY VERSIONS TO MAKE
WHAT SUCCESS LOOKS LIKE
WHAT TO SAVE THE WINNER AS
WHAT TO BRING BACK HERE

Do not claim you can inspect a file, image, audio track or video unless you can actually inspect it.

My project idea is: [WRITE ONE ORDINARY SENTENCE HERE]
```

You can write something as simple as:

```text
My project idea is: I want a five-minute anime where a samurai protects a girl crossing a dangerous valley.
```

or:

```text
My project idea is: Give me three ideas for a six-episode anime series, two minutes per episode.
```

You do not need to arrive with a synopsis, screenplay, shot list or character sheet.

## What the AI should do for you

The Master should use the embedded research and workflow knowledge internally. It can:

- propose story directions;
- build and repair story logic;
- write the script or episode script;
- read that script and identify what actually needs continuity references;
- decide which storyboard method fits;
- break the film into editorial shots and generation blocks;
- decide when start/end/keyframes are useful;
- write image and motion prompts;
- tell you exactly which approved references to upload;
- plan audio and editing;
- review continuity and story clarity;
- tell you what to save for the next episode or a future chat.

The AI should not send you away to repeat award-winning-animation research that is already compiled into the Brain unless you explicitly want to study it.

## Your job

You still make the creative choices that matter.

You normally need to:

1. describe what you want;
2. choose or approve the directions you like;
3. run image/video/audio generation when instructed;
4. bring candidate results back;
5. approve the keeper;
6. save the exact files the AI tells you to preserve.

## When the AI tells you to SAVE THIS

If your AI chat can create downloadable files, ask it to provide the complete artifact as that file.

If not, ask:

```text
Give me the complete contents for that file in one copyable Markdown block.
```

Copy it into any plain-text editor and save it with the exact filename the AI gave you.

Do not casually rename locked reference images after they enter the Asset Manifest.

## For a standalone film

Use `PROJECT-STATE-TEMPLATE.md` as the active memory record.

The Master should update it as the project moves from story to references, storyboard, shots, motion, audio, edit and QC.

## For a connected series

The Master should additionally create and maintain three durable files.

### 1. Series Bible

Template: `SERIES-BIBLE-TEMPLATE.md`

Typical saved file:

`SERIES-BIBLE-v01.md`

This contains permanent story, character, world, visual and audio canon.

### 2. Episode End State

Template: `EPISODE-END-STATE-TEMPLATE.md`

Typical file:

`E01-END-STATE.md`

This records what became true by the end of the episode so Episode 2 starts from the correct state.

### 3. Asset Manifest

Template: `ASSET-MANIFEST-TEMPLATE.md`

Typical file:

`ASSET-MANIFEST-v02.md`

This maps stable IDs such as `CHAR-01`, `PROP-01`, `WORLD-01` and `E01-SHOT-01` to the exact approved filenames.

## How media handoffs should work

The AI chat should never simply say “go animate it.”

For an image generation it should tell you, for example:

```text
NEXT TOOL: IMAGE GENERATOR
WHAT TO UPLOAD:
CHAR-01-SAMURAI-v01.png
WORLD-01-MOUNTAIN-v01.png

WHAT TO PASTE:
[exact prompt]

HOW MANY VERSIONS:
3

WHAT SUCCESS LOOKS LIKE:
Same face, wardrobe and sword; correct environment; readable action.

WHAT TO SAVE THE WINNER AS:
E01-SHOT-03-START-v01.png

WHAT TO BRING BACK HERE:
The candidates or the selected image plus its filename.
```

The same principle applies to video generation, audio and editing.

## Episode-safe names

For series work, editorial material should include the episode number.

Use:

`E01-SHOT-01`

not merely:

`SHOT-01`

because Episode 2 will have its own Shot 1.

Recurring character, prop and world IDs can remain global when they truly persist across episodes.

## How to continue next month

Return to the website and choose **Continue Existing Project**.

Open a new general-purpose AI chat and attach:

1. the latest Master Director;
2. the latest `SERIES-BIBLE-v##.md`;
3. the latest episode end state such as `E01-END-STATE.md`;
4. the latest `ASSET-MANIFEST-v##.md`;
5. the actual locked reference images named by the manifest.

Then send:

```text
Read the Master Director as the working instructions. I am continuing an existing series. Read all attached continuity files and visual references. Do not redesign or contradict anything marked LOCKED. Tell me what canon, story state and visual assets you can actually access, then continue with the next episode from the exact ending state of the previous one. Ask only the first question that materially changes the next episode.
```

A new chat does not automatically remember an old one. The saved continuity package is what makes continuation reliable.

## What the words mean

- **Proposed:** the AI suggested it, but you have not accepted it.
- **Approved:** you chose it for the current stage.
- **Locked:** future stages must preserve it unless you deliberately unlock it.
- **Reference:** an approved image or description used to preserve identity or design.
- **Keyframe:** an approved still that anchors a shot or motion change.
- **Shot:** one continuous editorial view in the final film.
- **Generation:** one attempt in a media model. One shot may need several attempts.
- **Asset Manifest:** the list that maps stable project IDs to exact approved files.
- **Series Bible:** permanent canon for connected episodes.
- **Episode End State:** what is true at the exact end of one episode.
- **QC:** quality control before moving forward or calling the film finished.

## Important limits

- AI can sound confident while being wrong. Changing model features, prices, limits and access must be verified when they matter.
- A prompt is not proof that media was successfully generated.
- A still image does not prove motion.
- A chat may be unable to inspect a supplied media type. It must state that honestly.
- Upload only material you have the right and permission to use.
- Do not copy protected characters, plots, dialogue or a living artist's distinctive style.
- Keep your own copies of approved text, images, clips and audio.

## Your first action

Download `master/MASTER-AI-ANIMATION-DIRECTOR.md`, open your chosen general-purpose AI chat, attach it and send the starter message above with one ordinary sentence describing what you want to make.
