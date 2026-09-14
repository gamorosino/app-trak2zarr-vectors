FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# zarr-vectors-tools depends on an unreleased core format (0.9.0) that is not
# published on PyPI yet, so both packages are installed from a full git clone
# of their main branch (not pip) with a plain, non-editable install.
RUN git clone https://github.com/Andrew-Keenlyside/zarr-vectors-py.git /opt/zarr-vectors-py \
    && pip install --no-cache-dir /opt/zarr-vectors-py

RUN git clone -b main https://github.com/AllenInstitute/zarr-vectors-tools.git /opt/zarr-vectors-tools \
    && pip install --no-cache-dir "/opt/zarr-vectors-tools[trk,trx]"
