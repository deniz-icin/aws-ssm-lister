import argparse
from parameters import is_response_successful , list_parameters , list_contents_of_parameter

parser = argparse.ArgumentParser()
parser.add_argument('--parameter', default=False)    
args = parser.parse_args()

def main():
    parameter_name = args.parameter
    parameters = list_parameters()
    parameter_names = [p.get('Name') for p in parameters]
    parameter_exist = parameter_name in parameter_names 

    if parameter_exist:
        print(list_contents_of_parameter(parameter_name))
    else:
        print(f"The parameter {parameter_name} does not exist.")

if __name__ == "__main__":
    main()