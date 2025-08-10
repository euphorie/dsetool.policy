# -*- coding: utf-8 -*-
"""Installer for the dsetool.policy package."""

from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="dsetool.policy",
    version="1.0.0.dev0",
    description="DS eTool Policy package",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="ale-rt",
    author_email="alessandro.pisa@gmail.com",
    url="https://github.com/syslabcom/dsetool.policy",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/dsetool.policy",
        "Source": "https://github.com/syslabcom/dsetool.policy",
        "Tracker": "https://github.com/syslabcom/dsetool.policy/issues",
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["dsetool"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        # -*- Extra requirements: -*-
        "osha.oira",
        "z3c.jbot"
    ],
    extras_require={
        "test": [
            "plone.app.testing",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
