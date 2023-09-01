class WebUtils:
    def __init__(self, driver):
        self.driver = driver

    def get_element_text(self, selector):
        element = self.driver.find_element_by_path(selector)
        return element.text
