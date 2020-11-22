#!/home/thomas/anaconda3/bin/python3

from datetime import datetime as dt

PATH = '/home/thomas/Desktop/'

filename = (str(dt.today().month) + str(dt.today().day) +
            str(dt.today().hour) +
            str(dt.today().minute) + 'test.txt')

with open(PATH + filename, 'wt') as f:
    f.write('test')

print(filename + ' angelegt')
