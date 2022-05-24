import base64
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Scrapper:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def download_all_pages_from_volume(self, volume, url):
        self.driver.get(url)
        numbers_of_chapters = self.get_number_of_chapters()
        for i in range(1, numbers_of_chapters):
            time.sleep(1)
            self.download_page(i, volume)
            self.goto_next_page()

        self.download_page(numbers_of_chapters, volume)

    def get_number_of_chapters(self):
        title = self.driver.find_element(By.XPATH, '//*[@id="main"]/h1').text.split()
        number_of_chapters = int(title[len(title) - 1])

        return number_of_chapters

    def download_page(self, page_number, volume):
        canvas = self.driver.find_element(By.ID, "the-canvas")
        canvas_base64 = self.driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
        canvas_png = base64.b64decode(canvas_base64)

        with open(rf"heartstopper{volume}/page{page_number}.png", "wb") as file:
            file.write(canvas_png)

    def goto_next_page(self):
        next_page_btn = self.driver.find_element(By.CLASS_NAME, 'btn.btn-primary.float-right')
        time.sleep(0.5)
        next_page_btn.click()
