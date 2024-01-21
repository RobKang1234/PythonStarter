# PythonStarter
 Auto-generate starter template of python3 and create env

# Usage
## To create a project base template with bump2version managing versioning
```bash
  pyinit -m create <project_name> 
```
In your project folder, it will create 
```bash
  package_name/
  |-- src/
  |   |-- __init__.py
  |-- tests/
  |   |-- test_placeholder.py
  |-- .bumpversion.cfg
  |-- .gitattributes
  |-- .girigore
  |-- MANIFEST.in
  |-- pytest.ini
  |-- setup.py
```

## To create github/workflows
```bash
  pyinit -m create <project_name> -i ci 
```

It will create
```bash
.github/
  |-- workflows/
  |   |-- <project_name>_ci.yml

```




