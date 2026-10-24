#!/usr/bin/env bash

# Resolve project directory
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR" || exit 1

echo "=========================================================="
echo "⚡ Starting EducationSwap on Local Mac (Apple Silicon CoreML)"
echo "=========================================================="

# Check Python3 availability
if ! command -v python3 &>/dev/null; then
    echo "❌ Error: python3 is not installed or not in PATH."
    exit 1
fi

# Set OpenMP and CoreML optimization environment variables
export OMP_NUM_THREADS=4
export VECLIB_MAXIMUM_THREADS=4

# Run with Apple Neural Engine/CoreML acceleration, multi-threading, and tolerant memory
python3 educationswap.py run \
    --execution-providers coreml cpu \
    --execution-thread-count 4 \
    --video-memory-strategy tolerant \
    --temp-frame-format jpeg \
    --open-browser "$@"
