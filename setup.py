from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='py_starter_auto_template',
    author='Shaofeng Kang',
    author_email='robkangshaofeng@gmail.com',
    version='0.0.2',  # Initial version, will be managed by bump2version
    description='Creating a template Python package with a CLI interface. ',
    keywords='python starter template cli version control python-starter python-starter-template python-starter-cli',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pyinit=python_starter.src.cli:main',
        ],
    },
    include_package_data=True,  # This will include non-code files specified in MANIFEST.in
    python_requires='>3.11',  # This specifies that your package requires Python > 3.11
    install_requires=required,
)