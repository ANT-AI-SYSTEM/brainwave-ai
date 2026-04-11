import os
import subprocess
import sys
from pathlib import Path

import uvicorn


if __name__ == "__main__":

    _ensure_thinking_audio()

    try:
        port = int(os.environ.get("PORT", 10000))

        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",
            port=port,
            reload=False,  
        )

    except Exception as e:
        print(f"[ERROR] Server failed: {e}")
        sys.exit(1)