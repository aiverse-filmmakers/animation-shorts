# Current 2026 AI Filmmaking Capability Addendum

RESEARCH CUTOFF: 2026-09-04 UTC
STATUS: RESEARCHED, not a claim that every route was run in this project

## Verified current findings

1. Runway's public filmmaking guidance recommends a treatment, shot-by-shot storyboard and prompt notes for camera, lighting, placement, mood and style. It describes generated clips as building blocks and recommends character plates with neutral views to reduce drift. Its Gen-4 guidance describes image-to-video from an input image plus motion-focused text, with 5- and 10-second options documented on the referenced page.
2. Google Flow and Veo documentation describes reusable ingredients for characters, objects and style, scene building, start/end frame workflows, camera controls, extension and native dialogue, effects and ambience on supported routes.
3. Google's Veo 3.1 material describes Frames to Video and Extend. These features are model and interface specific. Longer assembled sequences are not automatically one continuous generation.
4. Adobe Firefly documentation describes first and last keyframes, image-to-video, camera motion and generated sound effects. Partner-model controls vary by selected model and plan.
5. Luma documents start/end keyframes, extension, style reference, video-to-video and performance-guided modification. Input duration, crop, resolution and subscription conditions apply.
6. Public creator case studies show a repeatable pattern: script or outline, character/location development, storyboard or animatic, short replaceable shots, early rough cut, targeted regeneration, sound and hybrid finishing.
7. Google DeepMind's 2026 case study on *Dear Upstairs Neighbors* reports that text-only generation was not enough for controlled movement. The team used animation performance input, fine-tuning, masks, paintovers, dailies and repeated artist critique.
8. OpenAI developer documentation retrieved on this date includes video creation, edits, references, extensions and batch workflows, but the same documentation states that the Sora 2 models and Videos API are deprecated with a scheduled shutdown of 2026-09-24. OpenAI's public Sora launch page also carries an unavailability notice dated 2026-04-26. Sora is therefore historical or transition-sensitive material here, not a dependable default recommendation.

## Teaching decisions derived from the evidence

1. Plan the story and shots before spending on motion.
2. Let an approved image carry appearance and use motion instructions for the action.
3. Use start/end frames when the transition itself matters.
4. Use performance or motion references when dialogue, rhythm or complex movement matters more than text description.
5. Generate a pilot, compare a small number of takes, select and lock the keeper.
6. Assemble a rough edit early and regenerate only the weakest story section.
7. Treat native audio as optional, model-specific and a draft unless sync and continuity are verified.
8. Record tool, model, interface or API, date, settings, references, output and observed limits for every claimed test.

## Sources

1. Runway, longer videos and films: https://help.runwayml.com/hc/en-us/articles/26871350018835-How-to-create-longer-videos-and-films
2. Runway, Gen-4 Video Prompting Guide: https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide
3. Google, Flow and Veo filmmaking: https://blog.google/technology/ai/google-flow-veo-ai-filmmaking-tool
4. Google DeepMind, Veo 3.1: https://deepmind.google/blog/introducing-veo-31-and-advanced-creative-capabilities
5. Adobe, image-to-video: https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-images.html
6. Adobe, partner models: https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-non-adobe-models.html
7. Luma Ray3 Modify: https://lumalabs.ai/news/ray3-modify
8. Google DeepMind, *Dear Upstairs Neighbors*: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/dear-upstairs-neighbors
9. No Film School, hybrid workflow interview: https://nofilmschool.com/dear-upstairs-neighbors-hybrid-ai-short-film
10. Runway, *El Forastero* case study: https://runway.com/customers/behind-the-scenes-of-el-forastero-with-director-javier-de-la-chica
11. OpenAI video-generation documentation: https://developers.openai.com/api/docs/guides/video-generation
12. OpenAI historical Sora launch page: https://openai.com/index/sora-is-here/
