import gcd

def jug_problem(a, b, k):
    class Jug(object):
        def __init__(self, capacity):
            self.capacity      = capacity
            self.filled_with   = 0

        def free_space(self):
            return self.capacity - self.filled_with

        def is_full(self):
            return self.filled_with == self.capacity

        def is_empty(self):
            return self.filled_with == 0

        def fill(self):
            self.filled_with = self.capacity

        def empty(self):
            self.filled_with = 0

        def fill_from(self, jug):
            if jug.filled_with <= self.free_space():
                self.filled_with += jug.filled_with
                jug.empty()
            else:
                jug.filled_with -= self.free_space()
                self.filled_with = self.capacity

        def __str__(self):
            return "{}:{}".format(self.filled_with, self.capacity)

    jug1, jug2 = Jug(a), Jug(b)
    solution = []

    def solve(jug1, jug2, k):
        if jug2.filled_with != k:
            if jug2.is_full(): 
                jug2.empty()
            elif jug1.is_empty(): 
                jug1.fill()
            else:
                jug2.fill_from(jug1)
            solution.append((str(jug1), str(jug2)))
            solve(jug1, jug2, k)
            
    if k % gcd(a, b) == 0 and k <= b:
        solve(jug1, jug2, k)
        print( "->".join(map(str, solution)))
    else:
        print("Problem is not solvable with these arguments.")