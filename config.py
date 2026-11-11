import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

def get_browser_launch_options():
    return {
        'headless': os.getenv('HEADLESS').upper() == 'TRUE'
    }

def get_mobile_device_type():
    mobile = os.getenv('MOBILE', '').strip().lower()
    if not mobile or mobile == 'none':
        return None
    return mobile

def get_browser_type():
    return os.getenv('BROWSER').lower()

def get_base_url():
    return os.getenv('BASE_URL').lower()


def get_browser_context_options():
    return {
        "viewport": {
            "width": int(os.getenv("VIEWPORT_WIDTH")),
            "height": int(os.getenv("VIEWPORT_HEIGHT"))
        }
    }