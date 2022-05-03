# CarInsurance Model Package

Here the model is packaged though, for ease of execution no versioned distribution file ( .whl, .gz) file is generated and used for api creation.

Folder "config" and file 'config.yml' contains the model configurations.

"datasets" contains the train and test datasets.

"processing" contains files to save/load pipeline, feature transformation , input validation.

"trained_model" folder have the latest trained model .pkl file.

'pipeline.py' contains the pipeline.

'train_pipeline.py' is build to train the pipeline.

'predict.py' is build to predict based on the latest model .pkl file saved on folder "trained_model".
