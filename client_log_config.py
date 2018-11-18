#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:38:16 2018

@author: pc
"""

import logging
from functools import wraps
import inspect

def log(f):
    @wraps(f)
    def decor(*args):
        caller_name = inspect.stack()[1][3]
        s = "Функция {} вызвана из функции {}".format(f.__name__, caller_name)
        print('Decorator to function {}\nwith args: {}'.format(f.__name__,args))
        f(*args,s)
    return decor

@log
def do_log(*args):
    logger = logging.getLogger('server')
    
    fh = logging.FileHandler(filename='./log/server.log')
    fh.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(module)s %(message)s"))
    logger.addHandler(fh)
    logger.critical('critical message')
    if args:
        logger.critical(args[0])

def main():
    do_log()

if __name__ == '__main__':
    main()
