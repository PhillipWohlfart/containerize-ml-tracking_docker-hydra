# Use an official Jupyter Notebook image as the base
FROM jupyter/base-notebook

# Set the working directory inside the container
WORKDIR /app

# Install additional packages (PyTorch, torchvision, NumPy, Matplotlib, Pandas, and other dependencies)
RUN pip install \
    'torch' \
    'torchvision' \
    'mlflow' \
    'matplotlib' \
    'hydra-core'

# Install Git with elevated privileges (use sudo)
USER root
RUN apt-get update && apt-get install -y git

# Expose the Jupyter Notebook port (if not exposed by the base image)
EXPOSE 8888

# Create a directory for notebook data and set it as the working directory
RUN mkdir /app/notebook_data
WORKDIR /app/notebook_data

# Copy your Jupyter Notebook files into the container, relative path of notebook in the beginning
COPY /notebooks/* /app/notebook_data/

# Set the Git executable path
ENV GIT_PYTHON_GIT_EXECUTABLE /usr/bin/git

# Start Jupyter Notebook when the container runs
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--notebook-dir=/app/notebook_data", "--NotebookApp.allow_origin='*'"]
