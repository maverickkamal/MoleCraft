import json
from pathlib import Path
from copy import deepcopy

SAVE_DIR = Path.home() / ".molecraft"
SAVE_FILE = SAVE_DIR / "save.json"

DEFAULT_SAVE = {
    "high_score": 0,
    "last_difficulty": "easy",
    "completed_puzzles": {"easy": [], "medium": [], "hard": []},
    "total_solved": 0,
    "best_streak": 0,
    "fastest_solve": None,
}


def load_save() -> dict:
    if SAVE_FILE.exists():
        try:
            data = json.loads(SAVE_FILE.read_text(encoding="utf-8"))
            merged = deepcopy(DEFAULT_SAVE)
            merged.update(data)
            return merged
        except (json.JSONDecodeError, KeyError):
            return deepcopy(DEFAULT_SAVE)
    return deepcopy(DEFAULT_SAVE)


def write_save(data: dict) -> None:
    SAVE_DIR.mkdir(parents=True, exist_ok=True)
    SAVE_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
