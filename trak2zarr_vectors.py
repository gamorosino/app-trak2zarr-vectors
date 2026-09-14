#!/usr/bin/env python3
"""Convert a tractogram (.trk/.tck/.trx) into a zarr-vectors store via zvtools."""
import json
import os
import subprocess
import sys

with open("config.json") as f:
    config = json.load(f)

INPUT_KEYS = ("trk", "tck", "trx")

# Matches the neuro/track/zarr-vectors datatype's own file field
# (store: dirname=vectors.zarrvectors) -- the output directory is named
# after the "vectors" output id, containing that exact dirname.
OUTPUT_DIR = "vectors"
OUTPUT_STORE = os.path.join(OUTPUT_DIR, "vectors.zarrvectors")


def pick_input():
    for key in INPUT_KEYS:
        value = config.get(key)
        if value and value != "null":
            return key, value
    sys.exit("Error: no tractogram input found in config.json (expected one of: trk, tck, trx)")


def main():
    fmt, input_path = pick_input()

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    cmd = ["zvtools", "convert", input_path, OUTPUT_STORE, "--format", fmt]

    if fmt == "trk":
        cmd += ["--num-chunks", str(config.get("num_chunks", 5000))]
    else:
        cmd += ["--chunk-shape", str(config.get("chunk_shape", "50,50,50"))]

    workers = config.get("workers")
    if workers:
        cmd += ["--workers", str(workers)]
        cmd += ["--workers-backend", str(config.get("workers_backend", "process"))]

    compressor = config.get("compressor", "none")
    if compressor and compressor != "none":
        cmd += ["--compressor", compressor]

    if config.get("compute_length"):
        cmd += ["--compute-length"]
    if config.get("compute_endpoints"):
        cmd += ["--compute-endpoints"]

    coarsen = config.get("coarsen")
    sparsity = config.get("sparsity")
    if coarsen and sparsity:
        cmd += ["--coarsen", str(coarsen), "--sparsity", str(sparsity)]

    print("+ " + " ".join(cmd))
    result = subprocess.run(cmd)
    if result.returncode != 0:
        sys.exit(result.returncode)

    subprocess.run(["zvtools", "info", OUTPUT_STORE], check=False)
    subprocess.run(["zvtools", "validate", OUTPUT_STORE], check=False)


if __name__ == "__main__":
    main()
