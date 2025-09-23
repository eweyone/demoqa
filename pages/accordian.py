from pages.base_page import BasePage
from components.components import WebElement



class Accordian(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.section_one_content = WebElement(driver, '#section1Content > p')
        self.section_one_heading = WebElement(driver, '#section1Heading')
        self.section_two_content_child_one = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.section_two_content_child_two = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.section_three_content = WebElement(driver, '#section3Content > p')