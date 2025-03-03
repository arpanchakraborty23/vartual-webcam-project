from typing import List
from setuptools import setup,find_packages

Hypen_dot_e='-e .'
def get_requirements(file_path:str)->[List]:
    requirements=[]
    with open(file_path, 'r') as f:
        requirements=f.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if Hypen_dot_e in requirements:
            requirements.remove(Hypen_dot_e)
    return requirements

setup(
    name='Vartual-webcam',
    version='1.0',
    packages=find_packages(),
    author='Arpan Chakraborty',
    author_email='arpanchakraborty500@gmail.com',
    install_requires=get_requirements('requirements.txt'),
)