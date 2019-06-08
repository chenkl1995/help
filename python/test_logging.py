import logging
import os
import os.path as osp

if __name__ == '__main__':
    filepath = osp.join(os.getcwd(), 'test.log')
    logging.basicConfig(level=logging.INFO, filename=filepath)

    logging.info('Hello World!')