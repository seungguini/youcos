"""Setup for the youcos package."""

import setuptools

with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Seunggun Lee",
    author_email="seungguini@gmail.com",
    name='youcos',
    license="MIT",
    description='youcos is a simple Python package for collecting YouTube videos and comments',
    version='v0.0.5',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/seungguini/youcos',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['selenium', 'google-api-python-client'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
