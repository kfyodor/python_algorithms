def hanoi(n):
    move_from, move_with, move_to = s.Stack(), s.Stack(), s.Stack()

    for i in list(range(n))[::-1]: 
        move_from.push(i + 1)

    def hanoi_rec(n, move_from, move_with, move_to):
        if n == 1:
            move_to.push(move_from.pop())
            print("Result: {}, {}, {}".format(move_from, move_with, move_to))
        else:
            hanoi_rec(n - 1, move_from, move_to, move_with)
            move_to.push(move_from.pop())
            print("Result: {}, {}, {}".format(move_from, move_with, move_to))
            hanoi_rec(n - 1, move_with, move_from, move_to)

    hanoi_rec(n, move_from, move_with, move_to)