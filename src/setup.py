import setuptools

from src import __version__


with open("../README.md", "r") as fh:
    long_description = fh.read()


def get_requirements():
    """
    Returns a list of dependencies from the `requirements.txt` file
    """
    dep = []

    with open("../requirements.txt", "r") as fp:
        line = fp.readline()
        while line:
            dep.append(line.strip())
            line = fp.readline()

    return dep


setuptools.setup(
    name="falken_home",
    version=__version__,
    author="Richi Rod",
    author_email="ricardorg20@gmail.com",
    description="Get any data from Home consuming",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/falken20/falken_home",
    install_requires=get_requirements(),
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
