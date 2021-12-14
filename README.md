# Repository of Bank Marketing System
This project impelemented for capstone project of Machine Learning Zoomcamp

## Context

The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed. Based on client data, we can estimate probability of making deposit and decide if phone call to the client make sense. So the classification goal is to predict if the client will subscribe a term deposit (variable y).

## Dataset

http://archive.ics.uci.edu/ml/datasets/Bank+Marketing

## Feature Description

### bank client data:
- age (numeric)
- job: type of job (categorical: 'admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown')
- marital: marital status (categorical: 'divorced','married','single','unknown'; note: 'divorced' means divorced or widowed)
- education (categorical: 'basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown')
- default: has credit in default? (categorical: 'no','yes','unknown')
- housing: has housing loan? (categorical: 'no','yes','unknown')
- loan: has personal loan? (categorical: 'no','yes','unknown')

### related with the last contact of the current campaign:
- contact: contact communication type (categorical: 'cellular','telephone')
- month: last contact month of year (categorical: 'jan', 'feb', 'mar', ..., 'nov', 'dec')
- day_of_week: last contact day of the week (categorical: 'mon','tue','wed','thu','fri')
- duration: last contact duration, in seconds (numeric). Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no'). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.

### other attributes:
- campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
- pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)
- previous: number of contacts performed before this campaign and for this client (numeric)
- poutcome: outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success')

### social and economic context attributes
- emp.var.rate: employment variation rate - quarterly indicator (numeric)
- cons.price.idx: consumer price index - monthly indicator (numeric)
- cons.conf.idx: consumer confidence index - monthly indicator (numeric)
- euribor3m: euribor 3 month rate - daily indicator (numeric)
- nr.employed: number of employees - quarterly indicator (numeric)

### Output variable (desired target):
- y: has the client subscribed a term deposit? (binary: 'yes','no')


## Repo Structure

The following files are included in the repo:

```
heart-failure-prediction
├── Dockerfile <- Docker file with specifications of the docker container
├── Pipfile <- File with names and versions of packages installed in the virtual environment
├── Pipfile.lock <- Json file that contains versions of packages, and dependencies required for each package
├── Procfile <- Procfile for Cloud deployment
├── README.md <- Getting started guide of the project
├── bank-additional-full.csv <- Dataset
├── model.bin <- Exported trained model
├── notebook.ipynb <- Jupyter notebook with all codes
├── predict.py <- Model prediction API script for local deployment
├── preduct_test.py <- Model prediction API script for testing
├── requirements.txt <- Package dependency management file
└── train.py <- Final model training script
```

## Create a Virtual Environment

Clone the repo:

```
git clone <repo>
cd MLProject-Bank-Marketing-System
```

For the project, **virtualenv** is used. To install virtualenv:

```
pip install virtualenv
```

To create a virtual environment:

```
virtualenv venv
```

If it doesn't work then try:

```
python -m virtualenv venv
```

## Activate the Virtual Environment:

For Windows:

```
.\venv\Scripts\activate
```

For Linux and MacOS:

```
source venv/bin/activate
```

## Install Dependencies

Install the dependencies:

```
pip install -r requirements.txt
```

## Run the Jupyter Notebook

Run Jupiter notebook using the following command assuming we are inside the project directory:

```
jupyter notebook
```

## Run the Model Locally

The final model training codes are exported in this file. To train the model:

```
python train.py
``` 

For local deployment, start up the Flask server for prediction API:

```
python predict.py
```

Or use a WSGI server, Waitress to run:

```
waitress-serve --listen=0.0.0.0:9696 predict:app
```

It will run the server on localhost using port 9696.

Finally, send a request to the prediction API `http://localhost:9696/predict` and get the response:

```
python predict_test.py
```

## Run the Model in Cloud 

The model is deployed on **Heroku ** and can be accessed using:

```
https://bank-marketing-system.herokuapp.com/predict
```

The API takes a JSON array of records as input and returns a response JSON array.

How to deploy a basic Flask application to Pythonanywhere can be found [here](https://github.com/nindate/ml-zoomcamp-exercises/blob/main/how-to-use-pythonanywhere.md). 
Only upload the `bank-additional-full.csv`, `train.py`, and `predict.py` files inside the app directory.
Then open a terminal and run `train.py` and `predict.py` files. Finally, reload the application.
If everything is okay, then the API should be up and running.

To test the cloud API, again run `predict_test.py` from locally using the cloud API URL.

Notes:
- Pythonanywhere instance has almost all the necessary packages installed. So, we don't need to install packages manually.
- Some packages are not up to date. So, there might be compatibility issues, especially with Scikit-Learn and XGBoost.
For example changing `dv.get_feature_names_out()` to `dv.get_feature_names()` for lower versions of Scikit-Learn.

## Build Docker Image

To build a Docker image:

```
docker build -t bank-marketing-system .
```

TO run the image as a container:

```
docker run --rm -it -p 9696:9696 bank-marketing-system:latest
```

To test the prediction API running in docker, again run `predict_test.py` locally.

