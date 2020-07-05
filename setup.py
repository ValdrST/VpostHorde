#!/usr/bin/env python
from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(name='VpostHorde',
      version="0.9.2",
      description='Web stress test',
      long_description=readme,
      long_description_content_type="text/markdown",
      author='Valdr Stiglitz',
      author_email='valdr.stiglitz@gmail.com',
      url='https://github.com/ValdrST/VpostHorde',
      packages=set(['VpostHorde','VpostHorde.tools']),
      include_package_data=True,
      install_requires=[i.strip() for i in open("./requirements.txt").readlines()],
      entry_points={
          'console_scripts': ['VpostHorde = VpostHorde:main']
      },
      classifiers=[
          'Programming Language :: Python :: 3',
          "Operating System :: OS Independent",
      ])
