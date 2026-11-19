"""Minimal local project scaffold for the MiniMax H3 footage workflow.

This does not call a model or inspect video contents. It creates a JSON project
manifest from the filenames and basic filesystem metadata of local video files.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

VIDEO_EXTENSIONS = {".mp4", ".mov", ".mkv", ".webm", ".m4v"}


@dataclass
class Clip:
    id: str
    path: str
    size_bytes: int
    modified_at: str


@dataclass
class Project:
    name: str
    created_at: str
    media_root: str
    clips: list[Clip]


def scan_media(folder: Path) -> list[Clip]:
    """Return supported video files beneath folder in stable path order."""
    clips = []
    for path in sorted(p for p in folder.rglob("*") if p.is_file() and p.suffix.lower() in VIDEO_EXTENSIONS):
        stat = path.stat()
        clips.append(
            Clip(
                id=f"clip-{len(clips) + 1:04d}",
                path=str(path.resolve()),
                size_bytes=stat.st_size,
                modified_at=datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
            )
        )
    return clips


def create_project(media_folder: Path, output: Path, name: str | None = None) -> Project:
    media_folder = media_folder.expanduser().resolve()
    if not media_folder.is_dir():
        raise ValueError(f"Media folder does not exist: {media_folder}")

    project = Project(
        name=name or media_folder.name or "Untitled project",
        created_at=datetime.now(timezone.utc).isoformat(),
        media_root=str(media_folder),
        clips=scan_media(media_folder),
    )
    output = output.expanduser()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(asdict(project), indent=2) + "\n", encoding="utf-8")
    return project


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a local footage project manifest.")
    parser.add_argument("media_folder", type=Path, help="Folder containing video clips")
    parser.add_argument("-o", "--output", type=Path, default=Path("project.json"))
    parser.add_argument("--name", help="Optional project name")
    args = parser.parse_args()

    try:
        project = create_project(args.media_folder, args.output, args.name)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(f"Created {args.output} with {len(project.clips)} clip(s).")


if __name__ == "__main__":
    main()
