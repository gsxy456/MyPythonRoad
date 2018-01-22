# 函数的好处：可复用，可扩展，保持一致性
import time


def logger():
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('a.txt', 'a+') as f:
        f.write('%s end action\n' % time_current)


def test1():
    print('in the text1!')
    logger()

test1()