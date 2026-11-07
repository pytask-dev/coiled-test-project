[windows]
set shell := ["powershell.exe", "-Command"]

install:
    uv sync --all-groups --all-extras

test *FLAGS:
    uv run --extra test pytest {{FLAGS}}

typing:
    uv run --group typing --extra dask --extra coiled ty check src/

lint:
    uvx prek run -a
