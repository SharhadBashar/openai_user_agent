import sys

from chat_gpt import Chap_GPT
from user_agent import User_Agent

if __name__ == '__main__':
    user_agent_string = command = sys.argv[1]
    user_agent_dict = User_Agent().get_user_agent_info(user_agent_string)
    chat_gpt_dict = Chap_GPT().get_user_agent_info