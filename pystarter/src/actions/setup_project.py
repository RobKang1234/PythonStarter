import os
import sys

from pystarter.src.templates.const import (
    test_ini, 
    test_placeholder, 
    gitignore_temp, 
    git_attributes, 
    bumpversion_cfg,
    manifest_in,
)

def create_project_floder(project_name: str) -> None:
    os.mkdir(project_name)
    os.chdir(project_name)
    
    # make src folder
    os.mkdir('src')
    with open('src/__init__.py', 'w') as f:
        f.write('')
    
    
    # make tests folder 
    os.mkdir('tests')
    
    # create test.ini file with template
    with open('pytest.ini', 'w') as f:
        f.write(test_ini)
    
    with open('tests/test_placeholder.py', 'w') as f:
        f.write(test_placeholder)
    
    # create .gitignore file with template
    with open('.gitignore', 'w') as f:
        f.write(gitignore_temp)
    
    # create .gitattributes file with template
    with open('.gitattributes', 'w') as f:
        f.write(git_attributes)
    
    # create version control files using bump2version
    with open('.bumpversion.cfg', 'w') as f:
        f.write(bumpversion_cfg)
    
    # create mainifest.in file with template
    with open('MANIFEST.in', 'w') as f:
        f.write(manifest_in)
    
    # create setup.py file with template
    with open('setup.py', 'w') as f:
        # if python version >= 3.12 
        if sys.version_info >= (3, 12):
            f.write(f"""
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='{project_name}',
    version='0.0.1',  # Initial version, will be managed by bump2version
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,  # This will include non-code files specified in MANIFEST.in
    python_requires='>3.11',  # This specifies that your package requires Python > 3.11
    install_requires=required,
)
            """)
        else: 
            f.write(f"""
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='',
    version='0.0.1',  # Initial version, will be managed by bump2version
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,  # This will include non-code files specified in MANIFEST.in
    python_requires='>3.11',  # This specifies that your package requires Python > 3.11
    install_requires=required,
)
            """)
    