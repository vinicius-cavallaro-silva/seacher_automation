from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from model.searcher_table import SearcherModel
from view.google_views import GoogleHandler
from view.utils import Utils


class HandlerSearchers:
    def __init__(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.utils = Utils(self.browser)
        self.searcher_google = GoogleHandler(self.browser)
        self.list_search = ["Business process automation", "Automating repetitive tasks", "Data collection"]

    def flow_search(self):

        print('Opening Browser...')
        self.searcher_google.open_google()
        self.utils.maximize_window()
        for item in self.list_search:
            print('Starting researches...')
            self.searcher_google.new_search(text=item)
            self.utils.scrolling_page()

            print('Colecting researches leads...')
            links = self.searcher_google.get_links_list_by_searched()

            print('Validating links to deepen searches...')
            list_links = self.searcher_google.validate_list_links(link_list=links)

            print('Opening research links...')
            for link in list_links:
                self.utils.open_new_tab(link_page=link)
                self.utils.open_link(link=link)

                print('Taking a printscreen...')
                self.utils.take_picture(name_photo=item)
                self.utils.scrolling_page()

                print('Closing tab...')
                self.utils.close_tab()

                print('Saving results in Database ')
                SearcherModel.create_or_update(link_searched=link, photo_name=item)

        print('Closing browser...')
        self.utils.close_window()

        print('End.')
