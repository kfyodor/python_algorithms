import lib.polish_notation as PolishNotation
import lib.radix_sort as radix_sort
import lib.html_tags_matcher as html_tags_matcher

import lib.types.linked_list as ll
import lib.types.queue as queue


import timeit

def polish_notation_test():
    expressions = [
        "1 * 2 + 3",
        "1 + 2 * 3",
        "1 * 2 * 3",
        "1 - 2 + 3",
        "( 1 / 2 ) + 3",
        "( 1 / 2 ) * 3",
        "( 1 / 2 ) * 3 + 4 + 5",
        "1 + 2 * 3 + 4",
        "2 ** 3 + 4 * 5",
        "1 * ( 2 + 3 )",
        "( 1 + 2 ) * ( 3 + 4 )",
        "( ( 1 + 2 ) * ( 3 + 4 ) )",
        "( 1 + 2 ) ** 3 + ( 3 * ( 2 + 1 ) )"
    ]

    for expr in expressions:
        postfix = PolishNotation.PostfixConverter(expr).convert()
        prefix  = PolishNotation.PrefixConverter(expr).convert()

        postfix_result  = PolishNotation.PostfixEvaluator(postfix).calculate()
        prefix_result   = PolishNotation.PrefixEvaluator(prefix).calculate()

        print ('Testing:            {}'.format(expr))
        print ('Postfix:            {}'.format(postfix))
        print ('Postfix result:     {}'.format(postfix_result))
        print ('Prefix:             {}'.format(prefix))
        print ('Prefix result:      {}'.format(prefix_result))

        if ( prefix_result == postfix_result):
            print ('PASS')
        else: 
            print ('FAIL')
        print ('')

def test_queue():
    q = queue.Queue()
    for i in range(10): q.enqueue(i)

    empty = q.is_empty()
    while not empty: 
        q.dequeue()
        empty = q.is_empty()

def test_queue_rear():
    q = queue.QueueRear()
    for i in range(10): q.enqueue(i)

    empty = q.is_empty()
    while not empty: 
        q.dequeue()
        empty = q.is_empty()

def test_queues():
    q  = timeit.timeit('main.test_queue()', setup='import main;')
    qr = timeit.timeit('main.test_queue_rear()', setup='import main;')

    print ('Test queue:      {}'.format(q))
    print ('Test queue rear: {}'.format(qr))

def test_radix_sort():
    array1 = [5,3,4,2,1]
    array2 = [500, 30, 200, 1, 123]
    array3 = [50230, 3120, 2, 1000, 123]
    array4 = [551, 523, 550, 552, 2]

    print("Test radix sort: ")
    print("{} became {}".format(array1, radix_sort.radix_sort(array1)))
    print("{} became {}".format(array2, radix_sort.radix_sort(array2)))
    print("{} became {}".format(array3, radix_sort.radix_sort(array3)))
    print("{} became {}".format(array4, radix_sort.radix_sort(array4)))
    print("")

def test_tags_matcher():
    tags1 = "<div> <div><p> Zhopa </p></div></div>"
    tags2 = "<div></div></p>"
    tags3 = "<p><div></div><div><tag></tag></div></p>"

    print("Tags matching in {}: {}".format(tags1, html_tags_matcher.check(tags1)))
    print("Tags matching in {}: {}".format(tags2, html_tags_matcher.check(tags2)))
    print("Tags matching in {}: {}".format(tags3, html_tags_matcher.check(tags3)))

def test_linked_list(double = False):
    klass = 'DoubleLinkedList' if double else 'UnorderedLinkedList'
    list = ll.__dict__[klass]()
    list.add(1)
    list.add("str")
    list.add(10)
    list.add(11)
    list.append("last")

    print("Testing unordered linked list ({}):".format(klass))
    print(list)
    # print("Length: {}".format(len(list)))

    print("Get 2: {}".format(list.get(2)))
    print("Get 0: {}".format(list.get(0)))
    print("Get 1: {}".format(list.get(1)))
    print("Get 3: {}".format(list.get(3)))

    list.remove(10)
    print("Removed `10`: {}".format(list))

    list.remove("last")
    print("Removed `last`: {}".format(list))

    list.remove(1)
    print("Removed `1`: {}".format(list))

    list.remove(11)
    print("Removed `11`: {}".format(list))

    list.remove('str')
    print("Removed `str`: {}".format(list))

    list.add(1)
    list.add(2)
    list.add(3)
    list.add(4)
    list.add(5)
    list.add(6)
    list.add(7)
    list.add(8)
    print("Pop from {}".format(list))

    print("Popped {}".format(list.pop()))
    print("Popped {} from 2".format(list.pop(2)))
    print("Popped {} from 5".format(list.pop(5)))
    print("Popped {} from 1".format(list.pop(1)))
    print(list)

def test_ordered_linked_list():
    list = ll.OrderedLinkedList()

    list.add(1)
    list.add(4)
    list.add(3)
    list.add(2)
    list.add(15)
    list.add(-1)
    list.add(-1)
    list.add(-2)
    list.add(3)
    list.add(100)

    print("Ordered linked list: {}".format(list))


#test_linked_list()
test_linked_list(True)