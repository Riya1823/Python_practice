from setuptools import setup, find_packages
from os import path


setup(

    name = "cidr_info",
    version = "0.1.0",
    description = "Show information about a CIDR notation string",
    author = "Ravi Shekhar Jethani",
    author_email = "rsjethani@gamil.com",
    py_modules = ["cidr_info"],
    install_requires = [],
    entry_points = {
        "console_scripts": ["cidr_info=cidr_info:main"]
    },
    project_urls = {
        "source": "https://github.com/rsjethani/cidr_info"
    }
)
