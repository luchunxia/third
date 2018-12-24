from base.base_aciton import BaseAciton
import base

class SettingPage(BaseAciton):
    def __init__(self, driver):
        BaseAciton.__init__(self, driver)

    def click_search(self):
        self.click_element(base.setting_search_button)

    def input_content(self, content):
        self.input_element_content(base.setting_search_text, content)

    def click_back(self):
        self.click_element(base.setting_search_back)