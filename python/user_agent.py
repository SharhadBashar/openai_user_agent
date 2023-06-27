import user_agents
from pprint import pprint

class User_Agent:
    def __init__(self):
        None

    def get_user_agent_info(self, ua_string):
        ua = user_agents.parse(ua_string)

        # pprint(ua.__dict__)
        
        device_type = ua.device.family
        browser_name = ua.browser.family
        mobile_device = ua.device.model
        manufacturer = ua.device.brand
        os_name = ua.os.family
        is_tablet = ua.is_tablet
        is_mobilephone = ua.is_mobile
        is_browser = ua.is_pc
        is_touchcapable = ua.is_touch_capable
        is_robot = ua.is_bot
        
        return {
            'device_type': device_type, 
            'browser_name': browser_name, 
            'mobile_device': mobile_device, 
            'manufacturer': manufacturer, 
            'os_name': os_name, 
            'is_tablet': is_tablet, 
            'is_mobilephone': is_mobilephone, 
            'is_browser': is_browser, 
            'is_touchcapable': is_touchcapable, 
            'is_robot': is_robot
        }
    
if __name__ == '__main__':
    pprint(User_Agent().get_user_agent_info('Mozilla/5.0 (Linux; Android 9; KFMUWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/112.3.1 like Chrome/112.0.5615.207 Safari/537.36'))