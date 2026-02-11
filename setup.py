"""
L-ZIP Setup Configuration
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="l-zip",
    version="1.0.0",
    author="L-ZIP Team",
    description="Logic-based Zero-redundancy Information Prompting - MCP Server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/l-zip",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "lzip=cli:main",
        ],
    },
)
