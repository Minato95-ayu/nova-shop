import sys
import os
import subprocess

COMPILER_DIR = ".aayu-compiler"

if not os.path.exists(COMPILER_DIR):
    print("=> Downloading AAYU Compiler...")
    subprocess.check_call(["git", "clone", "https://github.com/Minato95-ayu/INTENT-TO-SILICON.git", COMPILER_DIR])

# Add compiler directory to path so python can find 'compiler' and 'runtime' packages
sys.path.insert(0, os.path.abspath(COMPILER_DIR))

try:
    import serve_app
except ImportError:
    print("Error: Could not load AAYU compiler. Ensure the repository was cloned correctly.")
    sys.exit(1)

if __name__ == "__main__":
    print("=> Starting Nova Shop using AAYU Engine...")
    # Inject our source file into argv so serve_app.main() picks it up
    sys.argv = ["serve_app.py", "src/main.aayu"]
    serve_app.main()
