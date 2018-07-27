#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools


def main():
    setuptools.setup(
        name= "bootstrap",
        version= "0.1.1",
        description= "hh bootstrap",
        url= "https://github.com/SuminAndrew/multiprocess-bootstrap",
        author= "SuminAndrew",
        py_modules= ["bootstrap"],
        entry_points= """
            [console_scripts]
            bootstrap = bootstrap:bootstrap
        """
    )

if __name__ == "__main__":
    main()
