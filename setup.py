import os
import pkg_resources
from setuptools import setup, find_packages


setup(
    name="CRAFT",
    py_modules=["CRAFT"],
    version="1.0",
    description="",
    author="Phanith LIM",
    url='https://github.com/Phanith-LIM/textdetection-craft.git',
    packages=find_packages(include=['CRAFT', 'CRAFT.*']),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ]
)
