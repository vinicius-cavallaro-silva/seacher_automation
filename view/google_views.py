from selenium.webdriver.common.keys import Keys


class GoogleHandler:

    def __init__(self, driver):
        self.driver = driver

    def new_search(self, text):
        self.driver.switch_to.window(self.driver.window_handles[0])
        search = self.driver.find_element_by_name('q')

        self.driver.find_element_by_name('q').clear()
        search.send_keys(text)
        search.send_keys(Keys.RETURN)

    def get_links_list_by_searched(self):
        links = self.driver.find_elements_by_css_selector('div.g a:first-child')
        return links

    def validate_list_links(self, link_list):
        list_links = []
        for link in link_list:
            page = link.get_attribute("href")
            if len(list_links) <= 2:
                if not "google" in page:
                    print(page)
                    list_links.append(page)
            else:
                break
        return list_links

    def open_google(self):
        self.driver.get('http://www.google.com.br')
        try:
            cookies = self.driver.find_element_by_xpath('//*[contains(text(), "Concordo")]')
            if cookies:
                cookies.click()
        except:
            pass
            print('Cookies accepted...')
