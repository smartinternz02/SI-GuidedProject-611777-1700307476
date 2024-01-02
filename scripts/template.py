import os 
from pathlib import Path
import logging 

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s : %(message)s : ]')

proj_name = 'poxVisionDetection'

list_of_files = [
    f'.github/workflows/.gitkeep',
    f'src/{proj_name}/__init__.py',
    f'src/{proj_name}/components/__init__.py',
    f'src/{proj_name}/utils/__init__.py',
    f'src/{proj_name}/config/__init__.py',
    f'src/{proj_name}/config/configuration.py',
    f'src/{proj_name}/pipeline/__init__.py',
    f'src/{proj_name}/entity/__init__.py',
    f'src/{proj_name}/constants/__init__.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'templates/index.html',
    'main.py'
]

for filepath in list_of_files:
    filepath = Path(filepath)                    # path() WILL CONVERT THE PATH TO WINDOWS SPECIFIC PATH

    filedir, filename = os.path.split(filepath)  # SEPERATING THE FILEDIRECTORY AND FILEPATH
    
    if (filedir != ''):
        os.makedirs(filedir, exist_ok = True)
        logging.info(f'CREATING THE DIRECTORY {filedir} : FOR THE FILE : {filename}')

    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath, 'w') as file:        # -> THIS WILL CREATE THE FILE IF IT DOES NOT EXIST
            pass 
            logging.info(f'EMPTY FILE HAS BEEN CREATED, FILE NAME : {filename}')

    else:
        logging.info(f'{filename} IS ALREADY CREATED')
