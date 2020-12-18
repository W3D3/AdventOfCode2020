from setuptools import setup, find_packages

setup(
    name="AdventOfCode2020",
    version="0.1",
    description="W3D3's solutions for Advent of Code 2020",
    url="https://github.com/W3D3/AdventOfCode2020",
    author="W3D3",
    author_email="christoph@wedenig.org",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    install_requires=[
        "advent-of-code-data >= 0.9.5",
        "parse",
        "networkx",
        "matplotlib",
        "numpy",
        "lark-parser"
    ],
    packages=find_packages(),
    entry_points={
        "adventofcode.user": ["W3D3 = solutions:solve"],
    },
)
