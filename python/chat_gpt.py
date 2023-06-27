import openai
from pprint import pprint

class ChapGPT:
    def __init__(self):
        None
    
    def get_user_agent_info(self, user_agent_string):
        openai.api_key = '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'  # Replace with your OpenAI API key

        prompt = f"User agent string: {user_agent_string}\n\ndeviceType\nbrowserName\nmobileDevice\nmanufacturer\nosName\nisTablet\nisMobilephone\nisBrowser\nisRobot\nisSpam\n---"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1,
            n=10,
            stop=None,
            temperature=0.0,
        )

        response_text = response.choices[0].text.strip()
        info_list = response_text.split("\n")

        device_type = info_list[0]
        browser_name = info_list[1]
        mobile_device = info_list[2]
        manufacturer = info_list[3]
        os_name = info_list[4]
        is_tablet = info_list[5]
        is_mobilephone = info_list[6]
        is_browser = info_list[7]
        is_robot = info_list[8]
        is_spam = info_list[9]

        return {
            'device_type': device_type, 
            'browser_name': browser_name, 
            'mobile_device': mobile_device, 
            'manufacturer': manufacturer, 
            'os_name': os_name, 
            'is_tablet': is_tablet, 
            'is_mobilephone': is_mobilephone, 
            'is_browser': is_browser, 
            'is_robot': is_robot
        }
    
if __name__ == '__main__':
    pprint(ChapGPT().get_user_agent_info('Mozilla/5.0 (Linux; Android 10; Note 8P Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36'))
