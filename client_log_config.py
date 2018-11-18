#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:38:16 2018

@author: pc
"""

import logging

# Создание именованного логгера
logger = logging.getLogger('client')

# Формат и направлеие вывода log
fh = logging.FileHandler(filename='./log/client.log')
fh.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(module)s %(message)s"))

# Подключение к logger
logger.addHandler(fh)
logger.critical('critical message')


#log_cl.critical("Can't connect to %(host)s at port %(port)d", params)
#logging.basicConfig(filename='./log/client.log',
#                format="%(created)f %(levelno)s %(module)s %(message)s")
