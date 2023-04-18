This file contains the information of the procedure that was followed for the Project.

## End to end ML project.


### Create a new environment
" -p indicates to create new environment in the current directory "

```
conda create -p venv python==3.8
conda activate venv/
```

### Install all the necessary packages using requirements.txt file
```
pip install -r requirements.txt
```

### In order convert a folder into packages we create setup.py and include the following code
```
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
```

### We add '-e .' in requirement.txt so that when we use "pip install -r requirements.txt" it will auto execute the "setup.py".