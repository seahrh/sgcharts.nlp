from setuptools import setup, find_packages
__version__ = '0.2.0'
setup(
    name="sgcharts.nlp",
    version=__version__,
    python_requires='>=3.5.0',
    install_requires=[
        'regex==2018.08.29'
    ],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    description='python3 utilities for natural language processing (English)',
    author='sgcharts',
    author_email='admin@sgcharts.com',
    url='https://github.com/seahrh/sgcharts.nlp'
)
