import sys
from pprint import pprint

from chat_gpt import Chap_GPT
from user_agent import User_Agent

if __name__ == '__main__':
    try :
        user_agent_string = sys.argv[1]
    except:
        user_agent_string = 'Mozilla/5.0 (Linux; Android 10; Note 8P Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36'
    user_agent_dict = User_Agent().get_user_agent_info(user_agent_string)
    chat_gpt_dict = Chap_GPT().get_user_agent_info(user_agent_string)

    user_agent_combined_dict = {
        'browser_name': [chat_gpt_dict['browserName'], user_agent_dict['browser_name']],
        'device_type': [chat_gpt_dict['deviceType'], user_agent_dict['device_type']],
        'is_browser': [chat_gpt_dict['isBrowser'], user_agent_dict['is_browser']],
        'is_mobilephone': [chat_gpt_dict['isMobilephone'], user_agent_dict['is_mobilephone']],
        'is_robot': [chat_gpt_dict['isRobot'], user_agent_dict['is_robot']],
        'is_spam': chat_gpt_dict['isSpam'],
        'is_tablet': [chat_gpt_dict['isTablet'], user_agent_dict['is_tablet']],
        'is_touchcapable': user_agent_dict['is_touchcapable'],
        'manufacturer': [chat_gpt_dict['manufacturer'], user_agent_dict['manufacturer']],
        'mobile_device': [chat_gpt_dict['mobileDevice'], user_agent_dict['mobile_device']],
        'os_name': [chat_gpt_dict['osName'], user_agent_dict['os_name']]
    }
    pprint(user_agent_combined_dict)
