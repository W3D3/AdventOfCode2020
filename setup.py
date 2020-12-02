from setuptools import setup, find_packages

setup(
    name="advent-of-code-2020",
    version="0.1",
    description="W3D3's solutions for https://adventofcode.com/",
    url="https://github.com/w3d3/advent-of-code-2020",
    author="W3D3",
    author_email="myusername@example.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    install_requires=[
        "advent-of-code-data >= 0.8.0",
        # list your other requirements here, for example:
        # "numpy", "parse", "networkx",
    ],
    packages=find_packages(),
    entry_points={
        "adventofcode.user": ["W3D3 = solutions:solve"],
    },
)