PATH_LOG = '../logs/internal/'
PATH_CONFIG = '../config/'

API_CONFIG = 'api_key.json'
LOG_FILENAME = 'logging.log'

LOG_FORMAT = {
    'timestamp': '',
    'id': '',
    'log_type': '',
    'user_agent': '',
    'response': '',
    'prompt_tokens': -1,
    'completion_tokens': -1,
    'total_tokens': -1
}
LOG_SETUP_MESSAGE = {'title': 'User Agent OpenAI log file'}
LOG_TYPE = {'i': 'info', 'e': 'error'}

GPT_MODEL = 'gpt-3.5-turbo'

USER_STRING = '''
    Get the following information from this user agent string in a python dictionary format:
    {}
    deviceType
    browserName
    mobileDevice
    manufacturer
    osName
    isTablet
    isMobilephone
    isBrowser
    isRobot
    isSpam
'''
MESSAGES = [
    {'role': 'system', 'content': 'You are a helpful assistant that gives me information from a user agent string.'},
    {'role': 'user', 'content': ''}
]
