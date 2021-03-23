import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="imadlib",
    version="0.0.1",
    author="Imad Jamil",
    author_email="imad.jamil@live.com",
    description="Tools for everything",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/imadjamil/imadlib",
    packages=setuptools.find_packages(),
    classifiers=[
		"Development Status :: 3 - Alpha",
		"Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3",
        "Operating System :: OS Independent",
    ],
)