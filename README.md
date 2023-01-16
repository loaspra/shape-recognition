# shape-recognition
CNN, GAN and GBDT models that extract features to identify shapes on a given image

## Set up the environment
1. Install [Poetry](https://python-poetry.org/docs/#installation)
2. Set up the environment:
```bash
make activate
make setup
```

## Install new packages
To install new PyPI packages, run:
```bash
poetry add <package-name>
```

## Run the entire pipeline
To run the entire pipeline, type:
```bash
dvc repo
```