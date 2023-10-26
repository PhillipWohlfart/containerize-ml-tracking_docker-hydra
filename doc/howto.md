## Jupyter image
`docker build -t custom-jupyter .`

## Run the Docker Container:
Once the image is built, run a Docker container from it using the docker run command. 
You can specify options such as port mapping and volume mounting if needed.

`docker run -p 8888:8888 -v notebook_data:/app/notebook_data custom-jupyter`


## Use Jupyter Notebook:
After running the container, you will see output in the terminal that includes a URL with a token.

### jupyter in vscode
- click on the notebook in your vscode
- select kernel on the top right for an existing jupyter server
- http://127.0.0.1:8888/?token=<your-token> as url
- <your-token> as password

### go to website
http://127.0.0.1:8888/?token=<your-token> to your browser

## Mlflow
### Before executing code
- `mlflow ui` to start the tracking server on `http://127.0.0.1:5000`

