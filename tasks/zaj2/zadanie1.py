# -*- coding: utf-8 -*-


def xrange(start_stop, stop=None, step=None):
    """
    Funkcja która działa jak funkcja range (wbudowana i z poprzednich zajęć)
    która działa dla liczb całkowitych.
    """
    if stop == None:
        stop = start_stop
        start = 0
    else: start = start_stop
    if step == None: step = 1
    yield start
    while True:
        start+=step
        
        if start >= stop: break
        yield start

print(list(xrange(3,10,3)))
