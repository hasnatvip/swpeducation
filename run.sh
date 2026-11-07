#!/usr/bin/env bash

# Resolve project directory
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR" || exit 1

echo "=========================================================="
echo "⚡ Starting EducationSwap on Local Mac (Apple Silicon CoreML)"
echo "=========================================================="

# Select Python runtime (prefer Python 3.10 environment where dependencies are installed)
if [ -x "/Library/Frameworks/Python.framework/Versions/3.10/bin/python3" ]; then
    PYTHON_BIN="/Library/Frameworks/Python.framework/Versions/3.10/bin/python3"
elif command -v python3.10 &>/dev/null; then
    PYTHON_BIN="$(command -v python3.10)"
elif command -v python3 &>/dev/null; then
    PYTHON_BIN="$(command -v python3)"
else
    echo "❌ Error: python3 is not installed or not in PATH."
    exit 1
fi

# Set OpenMP and CoreML optimization environment variables
export OMP_NUM_THREADS=4
export VECLIB_MAXIMUM_THREADS=4

# Run with Apple Neural Engine/CoreML acceleration, multi-threading, and tolerant memory
"$PYTHON_BIN" educationswap.py run \
    --execution-providers coreml cpu \
    --execution-thread-count 4 \
    --video-memory-strategy tolerant \
    --temp-frame-format jpeg \
    --processors face_swapper face_enhancer \
    --face-swapper-model hyperswap_1a_256 \
    --face-enhancer-model codeformer \
    --face-enhancer-blend 70 \
    --face-mask-types box occlusion \
    --open-browser "$@"
