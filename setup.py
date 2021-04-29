from setuptools import setup

setup(
    name="coincli",
    version="1.0.0",
    author="Arthur RICHARD",
    author_email="arthur.richard@protonmail.com",
    description="Unofficial Coinbase CLI tools based on Coinbase v2 API",
    packages=['coinbase'],
    install_requires=[
        "pipenv",
        "requests",
        "pydantic",
        "setuptools"
    ],
    url="https://github.com/arthuRHD/coincli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            'coincli=coinbase.cli:execute_from_commandline'
        ]
    }
)