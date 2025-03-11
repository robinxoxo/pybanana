from setuptools import setup, find_packages
import os

# Read the content of README.md for the long description
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pybanana",
    version="0.4.5",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.25.0",
        "python-dateutil>=2.8.2",
    ],
    extras_require={
        "dev": [
            "pytest>=8.0.0",
            "requests-mock>=1.11.0",
        ],
    },
    author="robin",
    author_email="xrobinsong@gmail.com",
    description="A Python wrapper for the GameBanana API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/robinxoxo/pybanana",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)