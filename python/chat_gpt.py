import os
import json
import openai
from pprint import pprint

from constants import *
from logger import Logger

class Chap_GPT:
    def __init__(self):
        with open(os.path.join(PATH_CONFIG, API_CONFIG)) as file:
            apis = json.load(file)
        openai.api_key = apis['open_ai']
        self.openai = openai
        self.user_string = USER_STRING
        self.messages = MESSAGES
        
    def get_response_dict(self, response_text):
        start_index = response_text.find('{')
        end_index = response_text.rfind('}') + 1
        dict_string = response_text[start_index: end_index]
        return eval(dict_string)

    def get_user_agent_info(self, user_agent_string):
        self.messages[1]['content'] = self.user_string.format(user_agent_string)
        try:
            response = openai.ChatCompletion.create(
                model = GPT_MODEL,
                messages = self.messages
            ) 
            usage = response['usage']
            response_text = response['choices'][0]['message']['content']
            response_dict = self.get_response_dict(response_text)
            
            Logger(LOG_TYPE['i'], user_agent_string, response_text, usage['prompt_tokens'], usage['completion_tokens'], usage['total_tokens'])
            
            return response_dict
        except Exception as error:
            Logger(LOG_TYPE['e'], user_agent_string, str(error), usage['prompt_tokens'], usage['completion_tokens'], usage['total_tokens'])
    
if __name__ == '__main__':
    pprint(Chap_GPT().get_user_agent_info('Mozilla/5.0 (Linux; Android 10; Note 8P Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36'))
