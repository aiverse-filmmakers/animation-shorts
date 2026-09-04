# Standalone Brain Contract Test Report

DATE: 2026-09-04
STATUS: PASS for static structural contracts; model behaviour not proven

`tests/validate_brain_library.py` checks deterministic marker presence, Master-versus-specialist activation wording, the shared rights/privacy section, the canonical Project State schema, exact ZIP membership and bytes, lesson status consistency, public metadata, compatibility targets and selected fixture markers. This is static text validation, not execution inside external AI accounts or proof that an LLM will follow every instruction.

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

`tests/last-drop-end-to-end.md` is a manually authored continuity example for the fictional short `The Last Drop`. It illustrates the intended story, reference, storyboard, packaging, keyframe, motion, audio, edit and QC handoffs. It is not a record of outputs produced by running every brain and does not claim that a final video was generated.

## Boundary

These are contract and handoff tests, not proof that every brain's prose is optimal in every LLM. Actual model output and video routes remain subject to the tool, input, plan and date, and must be reviewed honestly.
