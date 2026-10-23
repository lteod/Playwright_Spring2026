import pytest

import config

from fixtures.new_user import get_shopper


@pytest.fixture(scope="session")
def browser_type_launch_args():
    return config.get_browser_launch_options()

@pytest.fixture(scope="session")
def base_url():
    return config.get_base_url()

# @pytest.fixture(scope="session")
# def browser_context_args(base_url):
#     return {
#         "base_url": base_url,
#         "viewport": {
#             "width": int(config.get_browser_context_options()['viewport']['width']),
#             "height": int(config.get_browser_context_options()['viewport']['height']),
#         },
#     }
