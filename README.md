# 💎 Diamond Price Prediction 💎

## Overview
This project is intended to implement cutting-edge technologies from the field of ML and MLOps in order to create a solution, which allows the end-user to make predictions about a particular diamond's price.

The repository is divided into two branches, where *master* contains code related to model training and API, and *streamlit* stores the frontend.

If you want to navigate to a different branch, just run:
```shell
git checkout <branch_name>
```

## Setup
After cloning the repository you first have to set it up. Configure your Python interpreter to use Python 3.10. You can use either *Conda* or *venv*.

Install the required packages using:
```shell
pip install -r src/requirements.txt
```
After that manually create a */conf/local* directory.

## Kedro
### Pipelines overview
There are four distinct pipelines:

* **data_prep** - clean, removes outliers, standardizes, and spltis the data
* **train_model** - train AutoGluon predictor
* **evaluate_metrics** - produces DataFrame and PyPlot summaries of regression metrics
* **api_pipeline** - automated inference pipeline using kedro-fastapi


### Pipeline usage

You can run all Kedro pipelines at once using:

```shell
kedro run
```
or a selected pipeline:
```shell
kedro run --pipeline <pipeline_name>
```
### Kedro Viz
You can visualize all pipelines using:
```shell
kedro viz run
```
or a selected pipeline using:
```shell
kedro viz run --pipeline <pipeline_name>
```

### Fast API
This plugin automatically creates an MLPredictor that can perform inference using the defined *predict* method. It then runs Uvicorn and exposes the API on port 8000 by default. The API creation is based on *api.yml* and is orchestrated by Kedro like the rest of the project (see folder *api_pipeline*).

To start the API, run:
```shell
kedro fast-api run
```
#### Calling the API
If you want to test the API locally, first run it (with the command above) and then try to make a prediction. You can do that by opening http://0.0.0.0:8000 in your browser and input the data manually in the Swagger docs.

Another way to do so is passing the parameters in the URL itself, like so:
```html
http://0.0.0.0:8000/diamond_price?carat=1&cut=Ideal&color=E&clarity=I1&depth=1&table=1&x=1&y=1&z=1
```

## Docker
Since the app is supposed to be shareable, after developing it locally it can be containerized into a Docker image. The way the project is packaged into a Docker image is defined in the Dockerfile.

First, build the image:
```shell
docker build -t <image_name> .
```

Optionally, test the image locally:
```shell
 docker run -p 8000:8000 -e PORT=8000 <image_name>
```

Then you're free to use the image to create containers with the solution anywhere.

## Google Cloud
Our team has decided to share the app via Google Cloud's Cloud Run. In order to make that work, you need to put the Docker image you've built on Artifacts Registry. Please refer to the [official documentation](https://cloud.google.com/artifact-registry/docs/docker).

## Streamlit
In order to use the frontend first checkout to *streamlit* branch:
```shell
git checkout streamlit
```
Then install the required packages using:
```shell
pip install -r requirements.txt
```
Then run the frontend using:

```shell
streamlit run app.py
```
## Tkinter
In order to use the frontend first checkout to *Tkinter* branch:
```shell
git checkout Tkinter
```
Then install the required packages using:
```shell
pip install -r requirements.txt
```
Then create the executable file using:

```shell
pyinstaller main.py --onefile --name <name> --noconsole
```

This will create executable file in directory 'Dist'. To run the app simply go to this file and doubleclick it.
