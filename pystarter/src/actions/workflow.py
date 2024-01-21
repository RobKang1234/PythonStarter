import os 

def create_ci_workflow():
    """Creates a GitHub Actions workflow file in the .github/workflows directory.
    """
    # create .github/workflows directory
    os.makedirs('.github/workflows', exist_ok=True)
    
    # get name of current folder
    project_name = os.getcwd().split('/')[-1]
    # create workflow file with template
    with open('.github/workflows/ci.yml', 'w') as f:
        f.write(f"""
# .github/workflows/ci.yml

name: {project_name}_ci

on:
    push:
        branches: [ "main" ]
    pull_request:
        branches: [ "main" ]

    jobs:
    build:

        runs-on: ubuntu-latest
        strategy:
        fail-fast: false
        matrix:
            python-version: ["3.10", "3.11"]

        steps:
        - uses: actions/checkout@v3
        - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v3
        with:
            python-version: ${{ matrix.python-version }}
        - name: Install dependencies
        run: |
            python -m pip install --upgrade pip
            python -m pip install flake8 pytest
            if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
        - name: Lint with flake8
        run: |
            # stop the build if there are Python syntax errors or undefined names
            flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
            # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
            flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
        - name: Test with pytest
        run: |
            pytest

""")