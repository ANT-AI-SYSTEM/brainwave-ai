import os
import sys
import uvicorn


if __name__ == "__main__":

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