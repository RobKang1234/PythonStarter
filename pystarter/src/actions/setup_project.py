import os
import sys

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
        f.write("""
                    # pytest.ini
                    [pytest]
                    addopts = -ra -q
                    testpaths =
                        tests
        """)
    
    with open('tests/test_placeholder.py', 'w') as f:
        f.write("""
                    # tests/test_placeholder.py

                    def test_placeholder():
                        assert True
        """)
    
    # create .gitignore file with template
    with open('.gitignore', 'w') as f:
        f.write("""
                    # Byte-compiled / optimized / DLL files
                    __pycache__/
                    *.py[cod]
                    *$py.class

                    # C extensions
                    *.so

                    # Distribution / packaging
                    .Python
                    build/
                    develop-eggs/
                    dist/
                    downloads/
                    eggs/
                    .eggs/
                    lib/
                    lib64/
                    parts/
                    sdist/
                    var/
                    wheels/
                    share/python-wheels/
                    *.egg-info/
                    .installed.cfg
                    *.egg
                    MANIFEST

                    # PyInstaller
                    #  Usually these files are written by a python script from a template
                    #  before PyInstaller builds the exe, so as to inject date/other infos into it.
                    *.manifest
                    *.spec

                    # Installer logs
                    pip-log.txt
                    pip-delete-this-directory.txt

                    # Unit test / coverage reports
                    htmlcov/
                    .tox/
                    .nox/
                    .coverage
                    .coverage.*
                    .cache
                    nosetests.xml
                    coverage.xml
                    *.cover
                    *.py,cover
                    .hypothesis/
                    .pytest_cache/
                    cover/

                    # Translations
                    *.mo
                    *.pot

                    # Django stuff:
                    *.log
                    local_settings.py
                    db.sqlite3
                    db.sqlite3-journal

                    # Flask stuff:
                    instance/
                    .webassets-cache

                    # Scrapy stuff:
                    .scrapy

                    # Sphinx documentation
                    docs/_build/

                    # PyBuilder
                    .pybuilder/
                    target/

                    # Jupyter Notebook
                    .ipynb_checkpoints

                    # IPython
                    profile_default/
                    ipython_config.py

                    # pyenv
                    #   For a library or package, you might want to ignore these files since the code is
                    #   intended to run in multiple environments; otherwise, check them in:
                    # .python-version

                    # pipenv
                    #   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
                    #   However, in case of collaboration, if having platform-specific dependencies or dependencies
                    #   having no cross-platform support, pipenv may install dependencies that don't work, or not
                    #   install all needed dependencies.
                    #Pipfile.lock

                    # poetry
                    #   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
                    #   This is especially recommended for binary packages to ensure reproducibility, and is more
                    #   commonly ignored for libraries.
                    #   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
                    #poetry.lock

                    # PEP 582; used by e.g. github.com/David-OConnor/pyflow
                    __pypackages__/

                    # Celery stuff
                    celerybeat-schedule
                    celerybeat.pid

                    # SageMath parsed files
                    *.sage.py

                    # Environments
                    .env
                    .venv
                    env/
                    venv/
                    ENV/
                    env.bak/
                    venv.bak/

                    # Spyder project settings
                    .spyderproject
                    .spyproject

                    # Rope project settings
                    .ropeproject

                    # mkdocs documentation
                    /site

                    # mypy
                    .mypy_cache/
                    .dmypy.json
                    dmypy.json

                    # Pyre type checker
                    .pyre/

                    # pytype static type analyzer
                    .pytype/

                    # Cython debug symbols
                    cython_debug/

                    # PyCharm
                    #  JetBrains specific template is maintainted in a separate JetBrains.gitignore that can
                    #  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
                    #  and can be added to the global gitignore or merged into this file.  For a more nuclear
                    #  option (not recommended) you can uncomment the following to ignore the entire idea folder.
                    #.idea/

                
        """)
    
    # create .gitattributes file with template
    with open('.gitattributes', 'w') as f:
        f.write("""
                    # Set the default behavior, in case people don't have core.autocrlf set.
                    * text=auto

                    # Explicitly declare text files you want to always be normalized and converted
                    # to native line endings on checkout.
                    *.c text
                    *.h text

                    # Declare files that will always have CRLF line endings on checkout.
                    *.sln text eol=crlf

                    # Denote all files that are truly binary and should not be modified.
                    *.png binary
                    *.jpg binary
        """)
    
    # create version control files using bump2version
    with open('.bumpversion.cfg', 'w') as f:
        f.write("""
                    [bumpversion]
                    current_version = 0.0.1
                    commit = True
                    tag = True

                    [bumpversion:file:setup.py]
        """)
    
    # create mainifest.in file with template
    with open('MANIFEST.in', 'w') as f:
        f.write("""
                    # Include the README
                    include *.md

                    # Include the license file
                    include LICENSE

                    # Include the data files
                    recursive-include data *
        """)
    
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
    