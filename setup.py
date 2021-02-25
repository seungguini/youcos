"""Setup for the chocobo package."""

import setuptools

with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Seunggun Lee",
    author_email="seungguini@gmail.com",
    name='YOUCOS',
    license="MIT",
    description='YOUCOS is a simple Python package for scraping YouTube videos and comments',
    version='v0.0.1.dev1',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/seungguini/youcos',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['selenium'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
