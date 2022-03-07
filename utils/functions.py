import traceback

def commait(val):
    return "{:,}".format(val)

def printError(error):
    etype = type(error)
    trace = error.__traceback__
    lines = traceback.format_exception(etype, error, trace)
    traceback_text = ''.join(lines)
    print(traceback_text)