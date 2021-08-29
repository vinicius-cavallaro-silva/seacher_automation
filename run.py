__author__ = 'Vinicius Cavallaro da Silva'
__email__ = 'vinicius.cavallaro.silva'
__status__ = 'Development'

if __name__ == '__main__':
    from model.conection_db import create_all
    from controller.handler_google_searchers import HandlerSearchers

    print('Creating Table...')
    create_all()

    print('Starting automation...')
    searchers = HandlerSearchers()
    searchers.flow_search()
