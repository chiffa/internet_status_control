"""
Generic Setup configured for the project
"""
from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='DNS route diagnosis',
    version='0.0.2',
    description='Information Flow Analyzer for biological networks',
    long_description=long_description,
    url='https://github.com/chiffa/internet_status_control',
    author='Andrei Kucharavy',
    author_email='andrei.chiffa136@gmail.com',
    license='BSD',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD 3-clause license',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: Name Service (DNS)',
        'Topic :: System :: Networking :: Monitoring',
    ],
    keywords='network diagnostics, traceroute, ping',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['numpy',
                      'matplotlib',
                      'click',],
    entry_points="""
    [console_scripts]
    statstrace = tracert_stats:main
    """,
)