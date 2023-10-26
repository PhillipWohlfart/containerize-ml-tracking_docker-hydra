## Decision
- regular python image is too big use slim version instead and install needed dependencies
- or here used the jupyter image for a jupyter server

## Docker
- recommend to use vscode docker extension to see volumes and folder structure

## Mlflow tracking
- autologging exists for various data science libraries also pytorch
only works on models trained using `Pytorch Lightning` though
https://mlflow.org/docs/latest/tracking.html#automatic-logging
- would be useful for many different experiments running that each have to be configured
- can transform pytorch to pytorch lightning
- otherwise manual logging

## Hydra
- hydra has lot of functionality through commmand line. Change stuff dynamically, is jupyternotebook the best option for it?
- bypass use of @hydra.main(), and as such, you won't be able to use some of Hydra's advanced features like command-line overrides.
### hydra in notebook
- `https://github.com/facebookresearch/hydra/blob/main/examples/jupyter_notebooks/compose_configs_in_notebook.ipynb`