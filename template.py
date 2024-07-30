import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

package_name="Kidney-Disease"

List_of_files =[
    ".github/workflows/.gitkeep",
    f"src/{package_name}/_init_.py",
    f"src/{package_name}/components/_init_.py",
    f"src/{package_name}/utils/_init_.py",
    f"src/{package_name}/config/_init_.py",
    f"src/{package_name}/config/configure.py",
    f"src/{package_name}/pipeline/_init_.py",
    f"src/{package_name}/entity/_init_.py",
    f"src/{package_name}/constants/_init_.py",
    "config/config.yaml"
    "dvc.yaml",
    "params.yaml",
    "requirements.text",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"~
]
for filepath in List_of_files:
    filepath=Path(filepath)
    filedir,file_name=os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
    logging.info(f"Creating directory;{filedir} for file {file_name}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
        logging.info(f"Creating file; for file {filepath}")
    else :
        logging.info(f"{file_name} already exist:")