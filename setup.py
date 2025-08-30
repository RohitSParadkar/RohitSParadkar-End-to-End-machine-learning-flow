# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from typing import List

HYPN_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as f:
        requirements = [line.strip() for line in f if line.strip()]
    if HYPN_DOT in requirements:
        requirements.remove(HYPN_DOT)
    return requirements

setup(
    name="mlflow_learning",   # no spaces
    version="0.0.1",
    author="Rohit Paradkar",
    description="This is learning for package creation and distribution",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    python_requires=">=3.7"
)