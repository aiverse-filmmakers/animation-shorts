# Hermes Course Website UX Follow-up

Status: internal note. Do not link publicly.
Last updated: 2026-09-04

This note extends `HERMES-COURSE-WEBSITE-ARCHITECTURE.md` with the UX failures discovered after the first guided-system release and the fixes applied.

## Failure observed

The first implementation was structurally correct but several public links opened raw `.md` files directly in the browser. On GitHub Pages this renders as a black/plain-text document view. That is technically functional but poor course UX because the user suddenly leaves the designed experience and sees repository-like source text.

A second failure was affordance: specialist Brain cards visually looked like cards but had no obvious click action. A visitor could read the description but had no clear next move.

A third failure was navigation isolation: the preserved Learn/course experience had its own hash-navigation system, and its logo returned to the course home rather than the new AI Director homepage. Users could enter Learn and feel trapped there.

## UX rule learned

A resource being technically reachable is not enough. Every visible object must communicate its next action.

For downloadable instruction files, provide three distinct actions:

1. `OPEN` — render the document inside the branded site.
2. `COPY` — copy the full instruction text for immediate use.
3. `DOWNLOAD` — save the exact `.md` file for attachment to an external AI chat.

Do not make the user infer whether clicking a filename will preview, download or leave the site.

## On-site reader pattern implemented

`reader.html` now acts as a branded Markdown reader for public Brain, guide, research and test files.

Logic:

- website links point to `reader.html?file=...` for reading;
- reader fetches the canonical Markdown file;
- reader renders headings, lists, code blocks and links in the existing visual system;
- reader offers explicit `Download .md` and `Copy full text` actions;
- internal Markdown links are routed back through the reader when appropriate;
- the user always has a visible path back to the main AI Director page and Brain library.

General lesson: when a course exposes source files, wrap source artifacts in a learner-facing presentation layer rather than exposing storage-format rendering as the primary experience.

## Brain-card affordance implemented

Every Brain card is now actionable.

The whole card opens the styled reader, while each card also exposes explicit `Open`, `Copy`, and `Download` controls.

General lesson: cards describing tools should either be clearly informational or clearly interactive. Avoid the ambiguous middle state where they look clickable but are not.

## Learn navigation fix implemented

`learn.html` is now a persistent wrapper around the preserved `course.html` experience.

It adds a permanent top-level navigation bar with:

- AI-Verse brand/logo returning to the main Director homepage;
- `Back to AI Director`;
- `Brains`;
- theme control.

Because the course runs same-origin inside the wrapper, the wrapper also rewrites the old course logo target to the top-level homepage and intercepts `.md` links so they open in the styled reader rather than raw source.

General lesson: when preserving an old application/page inside a new information architecture, create an explicit parent navigation layer. Do not assume the old page's internal home action represents the new product home.

## Reusable course-site decision logic

Before publishing a resource link, ask:

1. What does the visitor expect this click to do?
2. Does the result stay inside the branded learning experience?
3. Is there an obvious route back?
4. If the object has multiple valid actions (read/copy/download), are those actions explicit?
5. Does the visual affordance match the actual behavior?

A technically correct route that violates these expectations is still a UX bug.
