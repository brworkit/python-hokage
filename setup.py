import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hokage",
    version="0.0.5",
    author="brworkit",
    author_email="brworkit@gmail.com",
    description="A python package for avoid repetitions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brworkit/python-hokage.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)