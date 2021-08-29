import time


class Utils:
    def __init__(self, driver):
        self.driver = driver

    def take_picture(self, name_photo: str):
        self.driver.save_screenshot(f'./image_screenshot/{name_photo}.png')
        print(f'Printscreen taken, photo will be saved as "/image_screenshot/{name_photo}.png"')

    def get_text_page(self, link_page: str):
        message = self.driver.find_element_by_tag_name("body").text
        print(f"{message} from {link_page}")

    def scrolling_page(self):
        SCROLL_PAUSE_TIME = 0.5
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        print('Scrolling page...')
        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def open_new_tab(self, link_page):
        # open new blank tab
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.execute_script("window.open();")
        # switch to the new window which is second in window_handles array
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(link_page)

    def close_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def close_window(self):
        self.driver.close()

    def open_link(self, link):
        self.driver.get(link)

    def maximize_window(self):
        self.driver.maximize_window()
