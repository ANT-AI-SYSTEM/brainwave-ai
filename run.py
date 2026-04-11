import os
import sys
import uvicorn


import os
import sys
import uvicorn

if __name__ == "__main__":
    try:
        port = int(os.environ.get("PORT", 10000))

        print("🚀 Starting server...")
        print(f"PORT: {port}")

        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",
            port=port,
            reload=False,
            log_level="debug",   # 🔥 ADD THIS
        )

    except Exception as e:
        print(f"[ERROR] Server failed: {e}")
        import traceback
        traceback.print_exc()   # 🔥 ADD THIS
        sys.exit(1)