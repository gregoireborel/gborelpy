# gborelpy

Python utilities for Gymshark projects and services.

## Build and publish locally
1. Login
```bash
gcloud auth login
gcloud auth application-default login
```
2. Outside your package virtual environment, install Poetry and Twine
    - [Poetry](https://python-poetry.org/docs/)
    - 
        ```bash
        pip install twine
        ```
3. Configure authentication to Artifact Registry for Python package repositories by following [Authenticating with keyring](https://cloud.google.com/artifact-registry/docs/python/authentication#keyring) (from your package virtual environment)
4. Make your changes in the code. Don't forget to update version number in [pyproject.toml](./pyproject.toml)
5. Build the package (_dist_ folder will be created) and publish it
```bash
cd ~/gborelpy
poetry build
python3 -m twine upload --repository-url https://[LOCATION].pkg.dev/PROJECT_ID/[REPO]/ dist/*
```

## Install the package in a project locally
Go to your project virtual environment.

1. Tell pip where to download the package
```bash
pip install --index-url https://[LOCATION].pkg.dev/PROJECT_ID/[REPO]/ gborelpy
```
2. Check that package has been successfully imported. In your code:
```
from gborelpy.beam_utils import ParseJSON
```

## Links
[Store Python packages in Artifact Registry](https://cloud.google.com/artifact-registry/docs/python/store-python)