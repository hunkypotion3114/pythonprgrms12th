"' Q1 '"

def exception_handler(value,mode=0):
    "' Handles incorrect input by user'"
    try:
        ele = eval(value)
    except NameError:
        if mode :
            ele = value
        else:
            ele = -1
    return ele


# def d