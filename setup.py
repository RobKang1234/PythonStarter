from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='py_starter_auto_template',
    version='0.0.1',  # Initial version, will be managed by bump2version
    description='Creating a template Python package with a CLI interface. ',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pyinit=pystarter.src.cli:main',
        ],
    },
    include_package_data=True,  # This will include non-code files specified in MANIFEST.in
    python_requires='>3.11',  # This specifies that your package requires Python > 3.11
    install_requires=required,
)