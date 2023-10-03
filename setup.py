# This file we require to convert your code in the libraray format 
# install your source code in lib format
# To create lib

from setuptools import find_packages,setup

from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT ="-e ." # it is mnetioned here bcz we want trigger requirements.txt file


def get_requirements()->List[str]: #->List[str] returns list which is a string
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list= requirement_file.readlines()
    requirement_list= [requirement_name.replace("\n" , "") for requirement_name in requirement_list]
    
    
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list



setup(
    
    name = "insurance",
    version="0.0.1",
    author = "Manisha Sharma",
    author_email ="manishash479@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements(),
)



