import boto3

client = boto3.client('ssm')

def is_response_successful(response):
    status_code = response.get('ResponseMetadata').get('HTTPStatusCode')
    if 200 <= status_code < 300:
        return True
    return False

def list_parameters():
    response = client.describe_parameters()
    success = is_response_successful(response)
    if success is False: print("Connection failed.")
    parameters = response.get('Parameters',[])
    return parameters

def print_parameters():
    parameter_data = list_parameters()
    result = [
            "ParameterName: {:^30s} | Type: {:<25s}".format(parameter.get('Name'), parameter.get('Type'))
            for parameter in parameter_data
        ]
    return ('\n'.join(result))

def list_contents_of_parameter(parameter):
    response = client.get_parameters(
    Names=[
        parameter,
    ],
    WithDecryption=True
    )
    contents = response.get('Parameters',[])
    result = [
         'Value: {:^30s}  |  DataType: {:>15s}'.format(content.get('Value'), content.get('DataType'))
         for content in contents
         ]
    return ('\n'.join(result))