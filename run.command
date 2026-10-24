#!/usr/bin/env bash

# Resolve project directory
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR" || exit 1

export OMP_NUM_THREADS=4
export VECLIB_MAXIMUM_THREADS=4

python3 educationswap.py run \
    --execution-providers coreml cpu \
    --execution-thread-count 4 \
    --video-memory-strategy tolerant \
    --temp-frame-format jpeg \
    --open-browser "$@"
