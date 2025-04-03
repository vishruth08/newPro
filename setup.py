from setuptools import find_packages,setup
from typing import List
dotenv_text="-e ."
def get_requirements(filepath:str)->List['str']:
    lst=[]
    with open(filepath,'r') as file:
        lst=file.readlines()
        lst=[lst1.replace("\n","") for lst1 in lst ]
        if dotenv_text in lst:
            lst.remove(dotenv_text)
    return lst



setup(
    name='mletoeproject',
    version='0.0.1',
    author='vishruth',
    author_email='vishu.valandas@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)