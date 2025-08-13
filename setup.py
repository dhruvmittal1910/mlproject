from setuptools import find_packages,setup
from typing import List


# function to call requirements.txt
def get_requirements(file_name:str)->List[str]:
    # this function will return list of packages
    requirements=[]
    with open(file_name) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .") #for setup.py file not to run
setup(
    name="ML-Project-2",
    version="1.0.0",
    author="Dhruv Mittal",
    author_email="dhruvmittal1910@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)