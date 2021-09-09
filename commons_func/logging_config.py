from .generic_func import *
import logging

START_PATH ='doc/log/log-'+todayToString()+'.txt'



logging.basicConfig(filename = START_PATH, filemode='a', format='%(asctime)s- %(name)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

