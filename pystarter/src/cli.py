import argparse

from pystarter.src.actions.setup_project import create_project_floder
from pystarter.src.actions.workflow import create_ci_workflow

def main():
    parser = argparse.ArgumentParser(description='Create a Python project.')
    
    # pyinit -m create <project_name> -i ci 
    parser.add_argument('-m', dest='mode', help='The mode to perform an action.')
    parser.add_argument('project_name', help='The name of the project.')
    parser.add_argument('-i', dest='init_option', default=None, help='Optional initialization option, e.g., CI workflow.')

    args = parser.parse_args()

    if args.mode == 'create':
        create_project_floder(args.project_name)
        if args.init_option == 'ci':
            create_ci_workflow()
    
    else:
        print("Unsupported mode or action.")