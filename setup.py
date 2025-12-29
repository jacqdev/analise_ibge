from setuptools import setup, find_packages

setup(
    name="analise_ibge",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "streamlit",
        "pytest",
        "pytest-cov"
    ],
)
