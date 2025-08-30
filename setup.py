from setuptools import setup, find_packages
import os

# Read the content of README.md for the long description
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pybanana",
    version="0.5.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "aiohttp>=3.12.0",
    ],
    extras_require={
        "dev": [
            "pytest>=8.0.0",
            "pytest-asyncio>=1.1.0",
        ],
    },
    author="robin",
    author_email="xrobinsong@gmail.com",
    description="A Python wrapper for the GameBanana API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/robinxoxo/pybanana",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.10",
    keywords="gamebanana api wrapper async mods gaming",
)