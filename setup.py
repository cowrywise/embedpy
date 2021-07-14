from setuptools import setup, find_packages
from embed import version
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="embedpy",
    version=version.__version__,
    packages=find_packages(),
    url="https://github.com/cowrywise/embedpy",
    license=version.__license__,
    author=version.__author__,
    author_email="embed@cowrywise.com",
    install_requires=["requests", "pytest", "pytest-mock"],
    keywords=["cowrywise", "embedpy"],
    description="Python client library for Cowrywise Embed Investments API",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
