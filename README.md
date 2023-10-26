# Description
Provides an example of how to create a containerized Jupyter Application to run ML experiments in it and track the results as well as defining configurations dynamically.
\\
The purpose is to have an app in a container for independent dependencies and still have a powerful tracking of your machine learning experiments.

- Docker for containerization
- MLflow for tracking experiments
- Hydra dynamic config management

## Utils

- `hydra` folder just shows basic functionality of hydra config management
- `jupyterTracking` folder provides a docker file and notebooks for running a simple ml experiment either with or without hydra config management. For further Instructions see `doc/howto`
- `doc/process` are only general thoughts about working with these technologies
