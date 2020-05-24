def enough(cap, on, wait):
    if cap - (on + wait) >= 0:
        return 0
    elif cap -(on + wait) < 0:
        return abs(cap - (on + wait))