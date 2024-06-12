import pytest
from playwright.sync_api import Dialog


@pytest.fixture(scope="session")
def browser_context_args():
    return {
        # "record_video_dir": "videos/",
        # "record_video_size": {"width": 640, "height": 480},
        "viewport": {"width": 800, "height": 800}
        # "viewport": {
        #     "width": 1920,
        #     "height": 1080,
        # }
    }