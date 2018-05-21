from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="pyims",
    version='0.1',
    description='A python wrapper for the IMS Word Sense Disambiguation tool (Zhong and Ng, 2010)',
    url='http://github.com/vishnumenon/pyims',
    author="Vishnu Menon",
    author_email="me@vishnumenon.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
        'nltk',
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    zip_safe=False)
