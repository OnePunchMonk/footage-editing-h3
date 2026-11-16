<div align="center">

![MiniMax H3 — footage × image workflow concept](assets/minimax-h3-banner.png)

# MiniMax H3 · Footage × Image Workflow 

**An idea for bringing MiniMax H3 and MiniMax H3 Image into a thoughtful, human-directed footage workflow.**

*Concept only — this repository does not contain a working editor or model integration yet.*

</div>

## The idea

What if a footage editor could help turn a folder of clips into a clear first cut, then use image generation to explore visual direction around it? This prototype concept pairs **MiniMax H3** with **MiniMax H3 Image** in one reviewable workflow: organize footage, shape a rough cut, and explore still-image references while keeping the editor in control.

The goal is not to automate authorship. It is to reduce the busywork between collecting footage and finding a story worth refining.

## A possible workflow

1. **Bring in footage.** Create a local project from a folder of clips and surface useful details such as duration, dimensions, and capture time.
2. **Find the story.** Explore an H3-assisted way to group or describe moments and propose a rough sequence. Every suggestion stays editable and optional.
3. **Explore the look.** Use H3 Image to create still-image references for mood, framing, or transitions. Treat these as visual development material, not silently inserted footage.
4. **Edit and review.** Arrange, trim, and preview the selected clips on a simple timeline; compare the cut with the visual references.
5. **Export when ready.** Save a recoverable project and render a conventional video, with progress and errors visible.

This is a product hypothesis, not a claim about current MiniMax model capabilities or an implemented integration. Model access, supported inputs and outputs, and safe handling of local media all need to be researched before implementation.

## First experiment

Start with one short, consented footage set and one editing task. Sketch the import → review → rough cut → image-reference → export journey, then test whether the H3/H3 Image pairing helps an editor move faster without making the edit harder to control.

Questions to answer:

- Which moments are useful to surface, and what evidence should accompany a suggestion?
- Where do image references help: mood boards, shot planning, or another part of the workflow?
- How should generated references stay distinct from source footage and final timeline media?
- What must remain local, and what can be sent to a model service?
- Does the assisted workflow improve the time to a reviewable first cut while preserving user control?

## Prototype boundary

| Explore first | Leave for later |
| --- | --- |
| Local clip bin and a single-track timeline | Multi-camera editing and collaboration |
| Basic trim, reorder, preview, save, and export | Advanced effects, grading, and compositing |
| Optional, reviewable H3 suggestions | Automatic edits applied without approval |
| Separate H3 Image reference board | Generated images presented as captured footage |

## Project status

This repository is currently a planning concept. It contains a proposed workflow diagram and this README; it does not yet include an application, model/API calls, benchmarks, or validated user research.

- [Prototype plan](docs/prototype-plan.excalidraw)

## Naming

Here, **H3** refers to **MiniMax H3** and **MiniMax H3 Image**. The repository explores a possible product idea around those models; it is not affiliated with MiniMax and does not imply official support.
