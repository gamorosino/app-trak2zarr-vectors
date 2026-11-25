<h1 align="center">trak2zarr-vectors</h1>

<p align="center">
  Converts a tractogram (.trk, .tck or .trx) into a Zarr Vectors store with zarr-vectors-tools (zvtools convert), optionally storing lengths, endpoints and a multiresolution pyramid.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.969"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.969-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-see_LICENSE-lightgrey.svg" alt="License"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Converts a tractogram (.trk, .tck or .trx) into a Zarr Vectors store with zarr-vectors-tools (zvtools convert), optionally storing lengths, endpoints and a multiresolution pyramid.**

Format conversion utility: picks the first provided input and calls zvtools convert with --num-chunks for .trk or --chunk-shape for .tck/.trx. Use it to make tractograms readable by Zarr Vectors viewers and cloud tools. Provide exactly one of the three inputs.

| | |
|---|---|
| **Inputs** | `neuro/track/trk` (optional) · `neuro/track/tck` (optional) · `neuro/track/trx` (optional) |
| **Outputs** | `neuro/track/zarr-vectors` |
| **Container** | `gamorosino/zarr-vectors-tools:latest` |
| **Resources** | 4 GB memory · 1 h walltime |
| **Run it** | [doi.org/10.25663/brainlife.app.969](https://doi.org/10.25663/brainlife.app.969) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `trk` | `neuro/track/trk` | no | Tractogram in .trk format (provide only one input). |
| `tck` | `neuro/track/tck` | no | Tractogram in .tck format (provide only one input). |
| `trx` | `neuro/track/trx` | no | Tractogram in .trx format (provide only one input). |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `vectors` | `neuro/track/zarr-vectors` | Zarr Vectors store containing the streamline geometry converted from the input tractogram. |

<details>
<summary><b>Parameters</b> (9)</summary>

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

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.969](https://doi.org/10.25663/brainlife.app.969), choose `neuro/track/trk`, `neuro/track/tck`, `neuro/track/trx` from your project, set the parameters and press **Execute**. The results are saved to your project as `neuro/track/zarr-vectors`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `gamorosino/zarr-vectors-tools:latest`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "trk": "/path/to/trk/trk",
       "tck": "/path/to/tck/tck",
       "trx": "/path/to/trx/trx",
       "num_chunks": 5000,
       "chunk_shape": "50,50,50",
       "workers": 0,
       "workers_backend": "process",
       "compressor": "zstd",
       "compute_length": false,
       "compute_endpoints": false,
       "coarsen": "",
       "sparsity": ""
   }
   ```

3. Run `./main`.

## Troubleshooting

- **no output produced**: Check that one tractogram input is provided and the conversion log for errors.

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

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- trak2zarr-vectors. brainlife.io App. [doi:10.25663/brainlife.app.969](https://doi.org/10.25663/brainlife.app.969)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Gabriele Amorosino

## License

See [LICENSE](LICENSE).
