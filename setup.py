#!/usr/bin/env python

from os import path

from setuptools import find_packages, setup

from wagtail_wordpress_import import __version__

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "docs/long_description.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="wagtail-wordpress-import",
    version=__version__,
    description="Import XML data into wagtail to create pages and content",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Nick Moreton",
    author_email="nickmoreton@me.com",
    url="https://github.com/torchbox/wagtail-wordpress-import",
    packages=find_packages(),
    include_package_data=True,
    license="BSD",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Framework :: Django",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 5.1",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 2",
        "Framework :: Wagtail :: 3",
        "Framework :: Wagtail :: 4",
        "Framework :: Wagtail :: 6",
    ],
    install_requires=[
        "django==5.1",
        "wagtail==6.3.2",
        "lxml==5.3.1",
        "bleach==6.2.0",
        "prettytable==3.15.1",
        "shortcodes==5.4.0",
        "cached-property==2.0.1",
    ],
    extras_require={
        "testing": [
            "freezegun==0.3.15",
            "responses>=0.16.0,<0.17.0",
            "flake8==5.0.4",
            "isort==5.10.1",
            "black==22.10.0",
        ],
    },
    zip_safe=False,
)
