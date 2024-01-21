import os

def create_project_floder(project_name: str) -> None:
    os.mkdir(project_name)
    os.chdir(project_name)
    
    # make src folder
    os.mkdir('src')
    
    # make tests folder 
    os.mkdir('tests')
    
    # create .gitignore file with template
    with open('.gitignore', 'w') as f:
        f.write("""
                
        """)
    
    