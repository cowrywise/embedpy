from setuptools import setup, find_packages
from embed import version
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

requirements_file = os.path.join(os.path.dirname(__file__), "requirements.txt")


def parse_requirements(filename):
    """
    Load requirements from a pip requirements file
    """
    lines = []

    with open(filename, "r") as fd:
        for line in fd.readlines():
            line = line.strip()
            if line and not line.startswith("#"):
                lines.append(line)
        return lines


setup(
    name="embed",
    version=version.__version__,
    packages=find_packages(),
    url="https://github.com/cowrywise/embed-python",
    license=version.__license__,
    author=version.__author__,
    author_email="embed@cowrywise.com",
    install_requires=parse_requirements("requirements.txt"),
    keywords=["api", "investments", "client", "embed"],
    description="Python client library for Cowrywise Embed Investments API",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
