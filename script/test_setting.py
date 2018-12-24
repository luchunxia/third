import os,sys
import pytest
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.setting_page import SettingPage
import base
import yaml

def get_setting_data():
    with open("./data/setting_data.yaml", "r") as f:
        return yaml.load(f).get("data")


class TestSetting():

    def setup(self):

        self.driver = init_driver(base.apppackage, base.appactivity)
        self.setting_page = SettingPage(self.driver)


    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("content", get_setting_data())
    def test_setting(self, content):
        self.setting_page.click_search()
        self.setting_page.input_content(content)
        self.setting_page.click_back()