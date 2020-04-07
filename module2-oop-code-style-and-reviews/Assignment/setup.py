
# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dc-lambdata", # the name that you will install via pip
    version="1.0",
    author="Doug Cohen",
    author_email="doug-cohen@lambdastudents.com",
    description="Contains function converting state abbreviations to state names, and another function that splits dates ('MM/DD/YYYY', etc.) into multiple columns",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/dougscohen/DS-Unit-3-Sprint-1-Software-Engineering/tree/master/module2-oop-code-style-and-reviews/Assignment/dc_lambdata",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)