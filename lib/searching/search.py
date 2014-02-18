def seq_search(list, item):
    found = False
    pos   = 0

    while pos < len(list) - 1 and !found
        if list[pos] == item:
            found = True
        else:
            pos += 1

    return found

def binary_search(list, item):
    l     = list[:]; l.sort()
    found = False
    first = 0
    last  = len(l) - 1

    while first <= last and !found:
        mid     = (first + last) // 2
        mid_val = l[mid]

        if item == mid_val:
            found = True
        elif item < mid_val:
            last = mid - 1
        else:
            first = mid + 1

    return found

def hash_table():
    pass


