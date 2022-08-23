from setuptools import setup
from typing import List
#Variable declaration
PROJECT_NAME="House_Rent_Prediction"
VERSION="0.0.2"
AUTHOR="MANJUNATH"
DESCRIPTION="This is demo project"
PACKAGES=["housing"]
REQUIREMENT_FILENAME="requirements.txt"


"""This function will return all the list of requirements mention in the requirements.txt file"""
def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILENAME) as requirement_file:
        return requirement_file.readlines()


#Setup file
setup(name=PROJECT_NAME,
 version=VERSION,
 author=AUTHOR,
 description=DESCRIPTION,
 packages=PACKAGES,
 install_requires=get_requirements_list()
 )

