import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

def get_browser_launch_options():
    return {
        'headless': os.getenv('HEADLESS').upper() == 'TRUE'
    }


def get_base_url():
    return os.getenv('BASE_URL').lower()


def get_browser_context_options():
    return {
        "viewport": {
            "width": os.getenv("VIEWPORT_WIDTH"),
            "height": os.getenv("VIEWPORT_HEIGHT")
        }
    }