import json

def parse_coze_data(input_str: str):
    trimmed_input = input_str.strip()
    json_str = '[{' + trimmed_input.replace('\n\n', '},{')\
                                   .replace('\n', '",')\
                                   .replace('event:', '"event":"')\
                                   .replace('data:', '"data":') + '}]'
    
    parsed_data = json.loads(json_str)
    
    return parsed_data