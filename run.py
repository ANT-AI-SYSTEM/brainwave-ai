import os
import subprocess
import sys
from pathlib import Path

import uvicorn


def _ensure_thinking_audio():
    try:
        result = subprocess.run(
            [sys.executable, "-m", "app.generate_thinking_audio"],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=str(Path(__file__).parent),
        )

        if result.returncode != 0 and result.stderr:
            print(f"[startup] Thinking audio: {result.stderr.strip()}")

    except Exception as e:
        print(f"[startup] Thinking audio skipped: {e}")


if __name__ == "__main__":

    _ensure_thinking_audio()

    try:
        port = int(os.environ.get("PORT", 10000))  # 🔥 IMPORTANT

        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",
            port=port,
            reload=False,  # 🔥 disable in production
        )

    except Exception as e:
        print(f"[ERROR] Server failed: {e}")
        sys.exit(1)