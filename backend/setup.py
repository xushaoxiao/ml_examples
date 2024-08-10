""" Python setup.py script for the backend package. """
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safety.
    >>> read("project", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths), 
        encoding=kwargs.get("encoding", "utf8")
    ) as open_file:
        open_file.read()
    return content


def read_requirements(path):
    """Read the contents of a requirements file."""
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="ml_examples",
    version=read("ml_examples", "VERSION"),
    description="Awesome backend created by me sharing how to build ML engineering.",
    url="https://github.com/xushaoxiao/ml_examples.git",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Shaoxiao Xu",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": [
            "ml_examples = ml_examples.__main__:main"
        ]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
