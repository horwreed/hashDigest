import hashlib
import json

def parse_request_body(request_body):
    request_dict = json.loads(request_body)
    if 'message' not in request_dict.keys():
        raise Exception('Invalid request, missing message')
    return request_dict['message']

def generate_message_digest(message):
    m = hashlib.sha256()
    m.update(message.encode('utf-8'))
    return m.hexdigest()