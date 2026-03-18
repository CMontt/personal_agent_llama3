import json
from pathlib import Path
    
def load_prompts(prompt_dict: Path) -> dict:
    prompts = {}

    for file in prompt_dict.glob("*.txt"):
        prompts[file.stem] = file.read_text(encoding="utf-8")

    return prompts

def load_contacts(contacts_path: Path) -> dict:
    with open(contacts_path, "r", encoding="utf-8") as f:
        return json.load(f)