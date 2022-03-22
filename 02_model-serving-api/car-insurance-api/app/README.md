# Model API

The "carinsurance_model" folder contains the structured model.

"schemas" folder contains the input and output scemas of the api.

"tests" folder contain few basic unit testing on the model prediction and api.

'main.py' will trigger the api. 

'api.py' contain the routers (get and post operations) and 'config.py' contains the api configuraions.

Once the api will run.
- api can be opened from 'http://localhost:8001'
- 'http://localhost:8001/docs' will show the full Car Isurance api. here 'POST' operation can be used for prediction.
- 'http://localhost:8001/api/v1/health' will show the api name and version
