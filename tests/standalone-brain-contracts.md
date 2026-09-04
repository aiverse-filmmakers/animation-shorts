# Standalone Brain Contract Test Report

DATE: 2026-09-04
STATUS: PASS for static structural contracts; model behaviour not proven

Each canonical file was read and checked independently by `tests/validate_brain_library.py`. This is deterministic text validation, not execution inside external AI accounts. No test supplied another brain file or hidden project memory. Each file contained its own role, Story DNA, minimum-input fallback, job boundary, output contract, stable-ID rules, lock-state language, evidence labels, failure recovery and handoff fields.

## Individual checks

1. Award-Winning Animation Story Brain: PASS. Accepts an idea, synopsis, script or cut and returns story diagnosis or development.
2. Idea Story Architect: PASS. Accepts a sentence, image, object, feeling or unfinished concept and returns 2-3 directions.
3. Synopsis Architect: PASS. Accepts an idea or existing synopsis and returns a compact visual synopsis.
4. Animation Screenwriter: PASS. Accepts a synopsis or short brief and returns visible scenes, dialogue and production risks.
5. Consistency and Reference Director: PASS. Accepts a script and identifies ranked recurring or critical references.
6. Storyboard Director: PASS. Accepts a scene, script, locks or references and chooses among the five storyboard methods.
7. Shot and Sequence Packager: PASS. Accepts a script, storyboard, runtime and route and separates story units, shots and takes.
8. Keyframe and Frame Director: PASS. Accepts a grid, frame or visual brief and returns extraction, start, end or keyframe instructions.
9. Motion and Animation Director: PASS. Accepts one approved shot and returns a concise route-aware generation prompt.
10. Audio and Dialogue Continuity Director: PASS. Accepts script and shot audio requirements and returns explicit music, source and sync decisions.
11. Edit and Pacing Director: PASS. Accepts shots, durations and story goals and returns an edit and pacing plan.
12. Final Film Critic and QC: PASS. Accepts a film, plan or notes and returns story, technical, originality, audio and evidence gates.
13. Master AI Animation Director: PASS. Accepts a rough idea or current project document and returns only the next progressive stage with project memory.

## End-to-end fixture

`tests/last-drop-end-to-end.md` passes the fictional short `The Last Drop` through story, synopsis, script, reference extraction, storyboard, packaging, keyframes, motion, audio, edit and QC. Stable character, prop, world, medium, shot and audio decisions remain explicit. The fixture does not claim that a final video was generated.

## Boundary

These are contract and handoff tests, not proof that every brain's prose is optimal in every LLM. Actual model output and video routes remain subject to the tool, input, plan and date, and must be reviewed honestly.
