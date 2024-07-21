# gborelpy

Python utilities for gborel projects and services.

## Maintenance
1. Login
```bash
gcloud auth login
gcloud auth application-default login
```
2. Update the code
3. Amend the package version in [pyproject.toml](./pyproject.toml)

## Install the package in a project locally
Go to your project virtual environment.

1. Tell pip where to download the package
```bash
pip install keyrings.google-artifactregistry-auth
pip install --extra-index-url https://europe-west1-python.pkg.dev/sample-project/python-repo/simple/ gborelpy==0.4.0
```
2. Check that package has been successfully imported. In your code:
```
from gborelpy.beam_utils import ParseJSON
```

More info about the setup instructions from the Artifact Registry repository:
```bash
gcloud artifacts print-settings python \
    --project=gborel-sample-project \
    --repository=python-repo \
    --location=europe-west1
```

## Links
[Store Python packages in Artifact Registry](https://cloud.google.com/artifact-registry/docs/python/store-python)