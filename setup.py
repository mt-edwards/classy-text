import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="classy-text",
    version="0.0.1",
    author="Matthew Edwards",
    author_email="matt.edwards@newcastle.ac.uk",
    description="This package is designed to teach text classification.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mt-edwards/classy-text",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)