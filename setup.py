from setuptools import setup

setup(name="pyims",
    version='0.1',
    description='A python wrapper for the IMS Word Sense Disambiguation tool (Zhong and Ng, 2010)',
    url='http://github.com/vishnumenon/pyims',
    author="Vishnu Menon",
    author_email="me@vishnumenon.com",
    license='MIT',
    packages=['pyims'],
    install_requires=[
        'nltk',
    ],
    zip_safe=False)
