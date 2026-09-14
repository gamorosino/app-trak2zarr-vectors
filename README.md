# trak2zarr-vectors

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
