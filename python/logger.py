import os
import json
import uuid
import logging
import datetime

from constants import *

'''
LOG_FORMAT = {
    'timestamp': '',
    'id': '',
    'log_type': '',
    'user_agent': '',
    'prompt': '',
    'response': ''
}
'''
class Logger:
    def __init__(self, log_type, user_agent, response, prompt_tokens, completion_tokens, total_tokens):
        if not (os.path.isfile(os.path.join(PATH_LOG, LOG_FILENAME))):
            f = open(os.path.join(PATH_LOG, LOG_FILENAME), 'w')
            f.write(json.dumps(LOG_SETUP_MESSAGE))
            f.write('\n')
            f.close()
        logging.basicConfig(filename = os.path.join(PATH_LOG, LOG_FILENAME), 
                            format = '%(message)s', 
                            filemode = 'a',
                            level = logging.ERROR) 
        
        logger = logging.getLogger()
        log = LOG_FORMAT.copy()
        log['timestamp'] = str(datetime.datetime.now())
        log['id'] = str(uuid.uuid4())
        log['log_type'] = log_type
        log['user_agent'] = user_agent
        log['response'] = response
        log['prompt_tokens'] = prompt_tokens
        log['completion_tokens'] = completion_tokens
        log['total_tokens'] = total_tokens
        logger.error(json.dumps(log))

if __name__ == '__main__':
    Logger(LOG_TYPE['i'], 'some user agent', 'some prompt', 'some success response')
    Logger(LOG_TYPE['e'], 'some user agent', 'some prompt', 'some error response')
