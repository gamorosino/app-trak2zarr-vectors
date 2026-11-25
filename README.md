# trak2zarr-vectors

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Converts a tractogram (.trk, .tck or .trx) into a Zarr Vectors store with zarr-vectors-tools (zvtools convert), optionally storing lengths, endpoints and a multiresolution pyramid.**

Format conversion utility: picks the first provided input and calls zvtools convert with --num-chunks for .trk or --chunk-shape for .tck/.trx. Use it to make tractograms readable by Zarr Vectors viewers and cloud tools. Provide exactly one of the three inputs.

| | |
|---|---|
| 📥 **Inputs** | `neuro/track/trk` (optional) · `neuro/track/tck` (optional) · `neuro/track/trx` (optional) |
| 📤 **Outputs** | `neuro/track/zarr-vectors` |
| 🐳 **Container** | `gamorosino/zarr-vectors-tools:latest` |
| ⚙️ **Resources** | 4 GB memory · 1 h walltime |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.969](https://doi.org/10.25663/brainlife.app.969) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `trk` | `neuro/track/trk` | no | Tractogram in .trk format (provide only one input). |
| `tck` | `neuro/track/tck` | no | Tractogram in .tck format (provide only one input). |
| `trx` | `neuro/track/trx` | no | Tractogram in .trx format (provide only one input). |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `vectors` | `neuro/track/zarr-vectors` | Zarr Vectors store containing the streamline geometry converted from the input tractogram. |

<details>
<summary><b>⚙️ Parameters</b> (9)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `num_chunks` | number | `5000` | Target chunk count for TRK ingest (zvtools convert --num-chunks). Only used when the input is .trk. |
| `chunk_shape` | string | `50,50,50` | Spatial chunk shape X,Y,Z for TCK/TRX ingest (zvtools convert --chunk-shape). Only used when the input is .tck or .trx. |
| `workers` | number | `0` | Number of parallel worker processes (zvtools convert --workers). 0 disables parallelism. |
| `workers_backend` | string | `process` | Parallel backend when --workers is set: process or dask. |
| `compressor` | string | `zstd` | Chunk array compressor (zvtools convert --compressor): none, zstd, or blosc. |
| `compute_length` | boolean | `false` | Store per-streamline path length (zvtools convert --compute-length). |
| `compute_endpoints` | boolean | `false` | Store per-streamline endpoints (zvtools convert --compute-endpoints). |
| `coarsen` | string |  | Optional per-level coarsen factors, e.g. 8,8 (requires sparsity too; builds a multiresolution pyramid). |
| `sparsity` | string |  | Optional per-level sparsity factors, e.g. 2,4 (requires coarsen too; builds a multiresolution pyramid). |

</details>

<!-- brainlife-app:end -->

Convert a tractogram (.trk, .tck, or .trx) into a Zarr Vectors store using zarr-vectors-tools' zvtools CLI.

## Inputs

- `trk` (neuro/track/trk) -- optional
- `tck` (neuro/track/tck) -- optional
- `trx` (neuro/track/trx) -- optional

## Outputs

- `vectors` (neuro/track/zarr-vectors) -- Zarr Vectors store containing the streamline geometry converted from the input tractogram.

## Usage

Brainlife.io: run via `braise-app-run`/`braise-app-pipeline` (once registered
with `braise-app-create`), or the web UI.

Locally (outside brainlife): copy `config.json.example` to `config.json`,
fill in real file paths, then run `./main` from this directory. `main` pulls
its own container (`singularity exec docker://...`) -- no local install of
the underlying tool needed, only Singularity itself.

Entrypoint: `trak2zarr_vectors.py`

Exactly one of `trk`/`tck`/`trx` should be set (the others left `null`);
`trak2zarr_vectors.py` picks the first non-null one and calls `zvtools
convert` with the right flags for that format (`--num-chunks` for `.trk`,
`--chunk-shape` for `.tck`/`.trx`).

## Container

`Dockerfile` here is reference only -- brainlife.io apps never build their
own container, `main` just pulls the already-published image
(`docker://gamorosino/zarr-vectors-tools:latest`). It installs
[`zarr-vectors-py`](https://github.com/Andrew-Keenlyside/zarr-vectors-py)
and [`zarr-vectors-tools`](https://github.com/AllenInstitute/zarr-vectors-tools)
(`zvtools`) from a full git clone of their `main` branch with a plain, non-editable
install, since the on-disk format `zarr-vectors-tools` requires (0.9.0) isn't
published on PyPI yet -- see the [zarr-vectors-tools
docs](https://zarr-vectors-tools.readthedocs.io/en/latest) for details.

## Authors

- Gabriele Amorosino <ga24643@eid.utexas.edu>

## License

MIT, see `LICENSE`.
