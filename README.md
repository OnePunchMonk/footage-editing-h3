<div align="center">

![MiniMax H3 — footage × image workflow concept](assets/minimax-h3-banner.png)

# MiniMax H3 · Footage × Image Workflow

**A concept for a human-directed footage workflow pairing MiniMax H3 with MiniMax H3 Image.**

*Early prototype — local footage indexing only; no model integration or editor UI yet.*

</div>

## The idea

What if an editor could turn a folder of clips into a clear first cut, then use image generation to explore its visual direction? This concept brings **MiniMax H3** and **MiniMax H3 Image** into one reviewable workflow: organize footage, shape a rough cut, and explore still-image references while keeping the editor in control.

The goal is to reduce the busywork between collecting footage and finding a story worth refining.

## Workflow overview

![High-level H3 footage editing workflow](assets/h3-workflow.svg)

*Conceptual flow: local footage ingestion → parallel H3 rough-cut suggestions and H3 Image visual references → human review and editing → save/export. Only local manifest generation is implemented today.*

## A possible workflow

1. **Bring in footage.** Create a local project from a folder of clips and surface details such as duration, dimensions, and capture time.
2. **Find the story.** Explore ways for H3 to group or describe moments and propose a rough sequence. Keep every suggestion editable and optional.
3. **Explore the look.** Use H3 Image to create still-image references for mood, framing, or transitions. Keep them as visual development material, separate from footage.
4. **Edit and review.** Arrange, trim, and preview clips on a simple timeline; compare the cut with the visual references.
5. **Export when ready.** Save a recoverable project and render a conventional video, with progress and errors visible.

This is a product hypothesis, not a claim about current MiniMax model capabilities. Model access, supported inputs and outputs, and safe handling of local media need research before integration.

## Try the scaffold

The first code step creates a JSON project manifest from supported video files found in a folder. It records each file's absolute path, size, and filesystem modification time. It does not copy or upload media, inspect video metadata, or call a model.

```bash
python prototype.py ./path/to/footage --output ./project.json --name "Weekend edit"
```

Requires Python 3.10 or newer and has no third-party dependencies. The output is a local JSON manifest, not an edited video or a generated timeline.

## First experiment

Start with one short, consented footage set and one editing task. Sketch the import → review → rough cut → image-reference → export journey. Then test whether pairing H3 and H3 Image helps an editor reach a reviewable first cut faster while keeping the edit easy to control.

Questions to answer:

- Which moments are useful to surface, and what evidence should accompany a suggestion?
- Where do image references help: mood boards, shot planning, or another part of the workflow?
- How should generated references stay distinct from source footage and timeline media?
- What must remain local, and what can be sent to a model service?
- Does the assisted workflow improve time to a reviewable first cut while preserving user control?

## Prototype boundary

| Explore first | Leave for later |
| --- | --- |
| Local clip bin and a single-track timeline | Multi-camera editing and collaboration |
| Basic trim, reorder, preview, save, and export | Advanced effects, grading, and compositing |
| Optional, reviewable H3 suggestions | Automatic edits applied without approval |
| Separate H3 Image reference board | Generated images presented as captured footage |

## Project status

The repository now includes a small local manifest generator in `prototype.py`, plus the proposed workflow diagram. It does not yet include an editor UI, media probing, model/API calls, benchmarks, or validated user research.

- [Prototype plan](docs/prototype-plan.excalidraw)

## Naming

Here, **H3** refers to **MiniMax H3** and **MiniMax H3 Image**. This repository explores a possible product idea around those models; it is not affiliated with MiniMax and does not imply official support.
