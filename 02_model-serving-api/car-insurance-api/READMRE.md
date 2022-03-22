# Classification Model Package
The api servise is build with 'FastAPI' using 'uvicorn'.
Folder 'app' contains the details. This is created to give a structure to the model development.

Tox is used here for execution.
Tox is a generic virtualenv management and test command line tool. Its goal is to standardize testing in Python.
Using Tox we can (on multiple operating systems):
 - Eliminate PYTHONPATH challenges when running scripts/tests
 - Eliminate virtualenv setup confusion
 - Streamline steps such as model training, model publishing

## Run With Tox (Recommended)
pip install tox
Make sure you are in the "02_model-serving-api/car-insurance-api" directory (where the tox.ini file is) 
then run the command: tox (this runs the tests and typechecks, trains the model under the hood). 
The first time you run this it creates a virtual env and installs dependencies, so takes a few minutes.

'tox -e run' will run the api ( but first model needs to be trained)
'tox -e train' will train the model 

## Run Without Tox
Add "02_model-serving-api/car-insurance-api" and "carinsurance_model paths" to your system PYTHONPATH
pip install -r test_requirements
Train the model: python "carinsurance_model/train_pipeline.py"
Run the tests pytest tests
