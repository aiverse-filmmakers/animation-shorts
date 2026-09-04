# Hermes Course Website Systems Note

Status: internal architecture note for Hermes. Do not link this file from the public website navigation.

## Core product correction

A course website that embeds reusable AI intelligence should not force beginners to manually repeat the cognitive work already encoded in the AI brains. Research should become compiled intelligence. The visitor supplies intent, taste, approvals and media-generation choices; the AI handles story craft, script structure, continuity extraction, storyboard-method selection, shot packaging, prompt construction, handoffs and QC wherever it can do so reliably.

## Website versus AI responsibilities

The website is a navigator and download hub, not the AI runtime. It must tell the user exactly which brain to download, which external AI chat to open, what to attach, what starter message to paste, which external media tool to use next, what files to upload there, what result to bring back, and what to save locally.

The external general-purpose AI chat is the reasoning engine. Image/video/audio tools are execution engines. The user's project folder is persistent memory.

## Primary UX logic

Primary route: Start a new film or series with the Master Director.
Secondary route: Continue an existing project from saved continuity files.
Optional route: Learn the underlying craft in the 30-lesson course.

Never make the educational course a prerequisite when the Brain already knows the required craft.

## Persistence model

For standalone films, Project State remains useful. For episodic work, add three durable layers:

1. SERIES-BIBLE.md: permanent story/world/character/visual/audio canon.
2. EPISODE-END-STATE.md: what became true by the end of the latest episode, including knowledge, injuries, relationships, objects, locations and unresolved threads.
3. ASSET-MANIFEST.md: stable IDs mapped to exact approved visual/audio asset filenames and their authority status.

A chat is not the archive. Every approved artifact that matters later must be accompanied by: SAVE THIS, FILE NAME, WHY I NEED IT, WHEN I WILL NEED IT AGAIN, HOW TO SAVE IT.

## Identity logic

Use project-safe stable IDs. For episodic editorial material use episode namespaces such as E01-SHOT-01 and E02-SHOT-01. Character/world/prop IDs remain global when their identity persists across episodes.

Grid panel numbers, editorial shot IDs, generation block IDs and generation take IDs are different layers and must never be conflated.

## Handoff logic

At every change of tool, state explicitly:
NEXT TOOL
WHAT TO UPLOAD
WHAT TO PASTE
HOW MANY VERSIONS TO GENERATE
WHAT TO CHECK
WHAT TO SAVE THE WINNER AS
WHAT TO BRING BACK TO THE AI CHAT

This converts a complex cross-tool workflow into a beginner-safe sequence.

## Research logic

Award-winning animation research should be used internally to strengthen ideas, scripts, turns, endings and diagnoses. Do not send the user away to repeat that research unless they explicitly want to learn it. Do not pretend short-film award research proves episodic-series heuristics; separate verified research, general story principles and proposed series workflow logic.

## Design logic

Preserve the existing AI-Verse visual system: neutral background, restrained green accent, large editorial typography, rounded cards, light/dark mode, minimal premium spacing. Change information architecture, not brand identity.

## Course-site skill lesson

When building future AI-enabled course websites, first ask: is this knowledge meant to teach the user to perform a task, or can the supplied AI brain perform that task for them? If the AI can reliably do it, make automation the default route and education the optional explanation layer. The website should expose the user's next decision and hide unnecessary professional taxonomy until it becomes useful.
