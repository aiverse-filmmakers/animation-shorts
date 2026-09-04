# Official AI Filmmaking Workflow Reference

**Research cutoff:** 4 September 2026

This is a dated reference note for the AI Animation Shorts brain library. It records first-party capability patterns found in official documentation. Availability, model names, limits, plans and regional access can change.

## OpenAI Sora

OpenAI documents text-to-video and image-to-video workflows, storyboard cards placed at timestamps, clip trimming, reordering, stitching, extension, remixing and synchronized audio. The storyboard guidance recommends leaving space between cards so scenes have room to connect. OpenAI also documents account, country, watermark, character and rights caveats, and states that Sora has no public API in the referenced help documentation.[1][2][3]

**Workflow lesson:** use storyboard cards and short clips as planning and generation units. Keep the cast small, write timing clearly and verify the current account and export conditions before promising a route.

## Google Flow with Veo

Google describes Flow as a scene-based creative workspace using reusable ingredients, prompts, clips and scenes. Its official help pages document text-to-video, text-to-image, visual ingredients, start and end frames, camera controls, extension and scene building. Google also distinguishes the Flow interface from Gemini API and Vertex AI capabilities.[4][5][6]

**Workflow lesson:** prepare clean character, object, location and style references, reuse them across shots, save useful frames and build the film from selected clips rather than expecting one prompt to create the whole short.

## Runway Gen-4 and Gen-4.5

Runway documents image-to-video generation from an input image and a motion-focused text prompt. Its guidance recommends treating a generation as one scene, starting with simple motion, then adding subject, camera and environmental motion incrementally. Runway also documents reusable references for characters, environments, objects and styles, with model-specific duration, frame-rate, plan and export conditions.[7][8][9]

**Workflow lesson:** let the still image carry appearance and use the text prompt mainly to direct motion. Test the simplest motion first, then build complexity through controlled iterations.

## Adobe Firefly

Adobe documents Firefly Boards for ideation, mood boards and storyboards, image-to-video with first and last frames, camera-motion controls, a browser video editor and generated sound effects. Partner-model controls vary by model, and Adobe labels some editor capabilities as beta or plan-dependent.[10][11][12]

**Workflow lesson:** use boards for planning, keyframes for controlled transitions, and a separate sound pass after the visual structure is understandable.

## Luma Dream Machine

Luma documents start and end image keyframes, extension, style reference and video-to-video modification. Its Ray3 Modify guidance describes character reference, scene-aware transformation and using the original performance as timing and motion guidance. Input duration, crop, subscription and resolution limitations apply.[13][14][15]

**Workflow lesson:** when motion is difficult to invent, start from a simple performance or motion reference, then change the world, material or character treatment in a controlled way.

## Cross-platform workflow derived from the documentation

1. Start with a story question, ending image and beat plan.
2. Build a visual bible before generating motion.
3. Separate character continuity from environment continuity.
4. Create still anchors before animating important shots.
5. Give each generation one main action and one clear dramatic job.
6. Use short iterative generations and review every keeper before continuing.
7. Build longer sequences through extension, stitching or timeline assembly.
8. Treat generated audio as a draft that still needs timing and clarity review.
9. Record the exact tool, model, plan, date, settings and reference assets for each shot.
10. Distinguish a feature available in a web UI from a feature available through an API.
11. Keep a human selection and rejection step between every major pass.

## What these sources don't prove

A documented feature isn't a guarantee of perfect identity, physics, continuity, audio or story quality. A platform's UI access doesn't prove API access. A longer scene assembled by extension isn't the same as one uninterrupted generation. The brains use these tools as examples and keep the production method portable.

## Sources

[1] OpenAI Help, “Creating videos with Sora”: https://help.openai.com/en/articles/12460853-creating-videos-with-sora

[2] OpenAI Help, “How to access Sora”: https://help.openai.com/en/articles/8958981-how-to-access-sora

[3] OpenAI Help, “Getting started with the Sora app”: https://help.openai.com/en/articles/12456897-getting-started-with-the-sora-app

[4] Google, “Introducing Flow: Google’s AI filmmaking tool designed for Veo”: https://blog.google/innovation-and-ai/products/google-flow-veo-ai-filmmaking-tool/

[5] Google Flow Help, “Create videos in Google Flow”: https://support.google.com/labs/answer/16353334

[6] Google Flow Help, “Edit videos & build scenes in Google Flow”: https://support.google.com/flow/answer/16935718

[7] Runway Help, “Gen-4 Video Prompting Guide”: https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide

[8] Runway Help, “Creating with Gen-4 Image References”: https://help.runwayml.com/hc/en-us/articles/40042718905875-Creating-with-Gen-4-Image-References

[9] Runway Help, “Creating with Gen-4.5”: https://help.runwayml.com/hc/en-us/articles/46974685288467-Creating-with-Gen-4-5

[10] Adobe Help, “About Firefly Boards”: https://helpx.adobe.com/my_ms/firefly/web/create-mood-boards/firefly-boards/about-firefly-boards.html

[11] Adobe Help, “Generate videos using images”: https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-images.html

[12] Adobe Help, “Generate sound effects”: https://helpx.adobe.com/firefly/web/firefly-video-editor/generate-audio/generate-sound-effects.html

[13] Luma Labs, “Ray3 Modify”: https://lumalabs.ai/news/ray3-modify

[14] Luma Labs, “Ray3 Modify User Guide”: https://lumalabs.ai/learning-hub/ray3-modify-user-guide

[15] Luma Labs, “How to use keyframes”: https://lumalabs.ai/learning-hub/how-to-use-keyframes
