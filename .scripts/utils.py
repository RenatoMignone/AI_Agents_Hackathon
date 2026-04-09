import json
import csv
from pathlib import Path
from typing import Dict, List, Any

# Adjust logic/types based on the Sandbox_2026_V3.pdf schema details
def load_level_data(base_path: str, level: int) -> Dict[str, Any]:
    """
    Loads users.json, locations.json, status.csv, and personas.md for a given level.
    Returns a unified dictionary mapping citizen_id to all their data.
    """
    level_dir = Path(base_path) / f"public_lev_{level}" / f"public_lev_{level}"
    if not level_dir.exists():
        raise FileNotFoundError(f"Data directory not found: {level_dir}")

    data: Dict[str, Any] = {}

    # 1. Load static user profiles
    users_path = level_dir / "users.json"
    with open(users_path, "r", encoding="utf-8") as f:
        users = json.load(f)
        for u in users:
            cid = u["user_id"]
            data[cid] = {
                "profile": u,
                "persona": "",
                "status_events": [],
                "locations": []
            }

    # 2. Load personas (parse markdown)
    # The persona markdown typically has headers for each user or relies on filename.
    # Below assumes a simplistic split by user name/id header.
    # Adjust according to the actual format of personas.md
    personas_path = level_dir / "personas.md"
    current_citizen = None
    if personas_path.exists():
        with open(personas_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("## ") or line.startswith("# "):
                    # Basic heuristic: try to find user ID or name in header.
                    # This might need refinement based on exact formatting.
                    for cid in data.keys():
                        if cid in line:
                            current_citizen = cid
                            break
                    else:
                        current_citizen = None
                elif current_citizen:
                    data[current_citizen]["persona"] += line

    # 3. Load locations
    locations_path = level_dir / "locations.json"
    if locations_path.exists():
        with open(locations_path, "r", encoding="utf-8") as f:
            locations = json.load(f)
            for loc in locations:
                cid = loc["user_id"]
                if cid in data:
                    data[cid]["locations"].append(loc)

    # 4. Load status events
    status_path = level_dir / "status.csv"
    if status_path.exists():
        with open(status_path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Based on the README schema: CitizenID column
                cid = row.get("CitizenID") or row.get("user_id")
                if cid and cid in data:
                    data[cid]["status_events"].append(row)

    return data
