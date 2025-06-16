import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name ='mlproject'

list_of_files=[
".github/workflow/.getkeep",
f"src/{project_name}/__init__.py",
f"src/{project_name}/components/data_ingestion.py",
f"src/{project_name}/components/data_transformation.py",
f"src/{project_name}/components/model_tranier.py",
f"src/{project_name}/components/mdel_monitering.py",
f"src/{project_name}/pipelines/__iniy__.py",
f"src/{project_name}/pipelines/training_pipelines.py",
f"src/{project_name}/pipelines/prediction_pipelines.py",
f"src/{project_name}/ecxeption.py",
"app.py",
"setup.py",
"requirements.txt"
]
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)


    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:{filedir} for the file {filename}")


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            logging.info(f"creating empty file:{filepath}")


    else:
        logging.info(f"{filename } is already exists")        








