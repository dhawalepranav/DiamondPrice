from setuptools import find_packages,setup
from typing import List

hypen_dot_e='-e .'

def get_requirements(file_path:str) ->List[str] :
    requirements=[]
    with open(file_path) as f :
        requirements=f.readlines()
        requirements=[i.replace("\n","") for i in requirements]

        if hypen_dot_e in requirements:
            requirements.remove(hypen_dot_e)

    return requirements



setup(
    name="First_Project",
    version="0.0.1",
    author="Pranav",
    author_email="pranavdhawale1998@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)