from lib.types import queue

def radix_sort(array):
    radices = _get_radices(array)
    buckets = [queue.Queue() for i in range(10)]

    for radix in radices:
        new_array = []

        for number in array:
            pos = int(number % (radix * 10) / radix)
            buckets[pos].enqueue(number)

        for q in buckets:
            while not q.is_empty():
                new_array.append(q.dequeue())

        array = new_array

    return array

def _get_radices(array):
    radix, radices = (1, [1])

    for num in array:
        tmp = int(num / radix * 10)

        while tmp != 0:
            radix *= 10
            radices.append(radix)
            tmp = int(num / radix)

    return radices