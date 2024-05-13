#!/usr/bin/python3

def switch(my_list=[]):
    if len(my_list) == 0:
        return None
    new_list = my_list.copy()
    new_list[0], new_list[-1] = new_list[-1], new_list[0]
    return new_list
