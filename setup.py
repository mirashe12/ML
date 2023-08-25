from setuptools import find_packages,setup
from typing import List
hyphedot="-e ."
def get_requirements(file_path:str)->list[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() 
        requirements=[req.replace("\n","") for req in requirements]
        
        if hyphedot in requirements:
            requirements.remove(hyphedot)
    return requirements
setup(
    name='MLKASESX',
    version='0.0.1',
    author='rohith',
    author_email='rohithmr12121@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)