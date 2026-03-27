import json
import os
from pathlib import Path
from typing import List

MEMORY_FILE = Path("database/user_memory.json")

class MemoryService:

    def __init__(self):
        MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
        if not MEMORY_FILE.exists():
            MEMORY_FILE.write_text("[]")

    def load_memory(self) -> List[str]:
        try:
            return json.loads(MEMORY_FILE.read_text())
        except Exception:
            return []

    def save_memory(self, memory: str):
        memories = self.load_memory()
        memories.append(memory)
        MEMORY_FILE.write_text(json.dumps(memories, indent=2))

    def get_memory_context(self) -> str:
        memories = self.load_memory()
        if not memories:
            return ""
        return "\n".join([f"- {m}" for m in memories])