#!/usr/bin/python3
'''
Method that determines if all the boxes can be opened.
'''


def canUnlockAll(boxes):
    '''
    receives a list of lists
    '''
    open = []
    for i in range(len(boxes)):
        open.append(0)
    aux = []
    key = 0
    for keys in boxes[0]:
        if (keys > 0 and keys < len(boxes)):
            if open[keys] == 0:
                open[keys] = keys
    for boxnro in range(1, len(boxes)):
        if (boxnro == open[boxnro]):
            for keys in boxes[boxnro]:
                if (keys > 0 and keys < len(boxes)):
                    open[keys] = keys
        else:
            aux.append(boxnro)
    for box in aux:
        if (box == open[box]):
            for keys in boxes[box]:
                if (keys > 0 and keys < len(boxes)):
                    open[keys] = keys
    if(open.count(0) > 1):
        return False
    else:
        return True
