def oops():
    raise IndexError("Oops! You have encountered an index error.")


def caller():
    try:
        oops()
    except IndexError as e:
        print("Caught the IndexError exception:", e)


caller()


def oops_2():
    raise KeyError("Oops! You have encountered an index error.")


def caller_2():
    try:
        oops_2()
    except IndexError as e:
        print("Caught the IndexError exception:", e)


caller_2()
