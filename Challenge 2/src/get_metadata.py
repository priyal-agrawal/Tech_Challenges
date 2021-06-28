## editor : priyal Agrawal


import requests
import json

aws_metadata_url = 'http://169.254.169.254/latest/'


def json_lookup(url, path_list):
    output = {}
    for each in path_list:
        endpoint = url + each
        k = requests.get(endpoint)
        text = k.text
        if each[-1] == "/":
            list_of_all_values = k.text.splitlines()
            output[each[:-1]] = json_lookup(endpoint, list_of_all_values)
        elif jjson_validity(text):
            output[each] = json.loads(text)
        else:
            output[each] = text
    return output

## metadata_function called by main function get_json which takes all the url path to find metadata. The contextpath meta-data/ returns the top level metadata information. We can add more context path in variable "path_tofind" to get value for particular key. example : path_tofind = ["meta-data/","meta-data/placement/region"] where the second path will return the region of aws instance.

def metadata_function():
    path_tofind = ["meta-data/"]
    result = json_lookup(aws_metadata_url, path_tofind)
    return result

## primary function that calls metadata function
def get_json():
    metadata = metadata_function()
    get_json = json.dumps(metadata, indent=4, sort_keys=True)
    return get_json

## to check the json is valid
def jjson_validity(value):
    try:
        json.loads(value)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    print(get_json())
