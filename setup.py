from setuptools import setup, find_packages
from typing import List   # ✅ Correct import for type hints in Python <3.9

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        # remove -e . if present in requirements.txt
        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements

setup(
    name="ML project 1",
    version="0.0.1",
    author="Nara Naveen",
    author_email="nara.naveen@example.com",
    description="A simple machine learning project",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
