def cannibals_and_missionaries():
    initial_state  = [3, 3, 1] # [m, c, b], initial left side
    cache  = []
    solution = []

    def travel(state, m, c):
        s = copy_state(state)

        if state[2] == 1:
            if s[0] < m or s[1] < c:
                return False

            s[0] -= m
            s[1] -= c
            s[2] = 0
        else:
            if (s[0] + m > 3) or (s[1] + c > 3):
                return False

            s[0] += m
            s[1] += c
            s[2] = 1

        return s


    def copy_state(state):
        s = [None] * 3
        s[0] = state[0]
        s[1] = state[1]
        s[2] = state[2]

        return s

    def cache_key(state):
        return "".join(map(str, state))

    def put_cache(state): 
        cache.append(cache_key(state))

    def add_to_solution(state):
        solution.append(cache_key(state))

    def get_cache(state):
        return cache_key(state) in cache

    def check_state(state):
        if state:
            ml = state[0]
            cl = state[1]
            mr = 3 - state[0]
            cr = 3 - state[1]
            
            return (ml >= cl or ml == 0) and (mr >= cr or mr == 0)

    def possible_transitions(state):
        return solve(state, 2, 0) or \
               solve(state, 1, 0) or \
               solve(state, 1, 1) or \
               solve(state, 0, 2) or \
               solve(state, 0, 1)

    def solve(state, m, c):
        new_state = travel(state, m, c)

        if new_state:
            if get_cache(new_state):
                return False
            else:
                put_cache(new_state)
        else:
            return False

        if not check_state(new_state):
            return False
        
        add_to_solution(state)

        if new_state == [0, 0, 0]:
            print("Solved")
            return True
        else:
            return possible_transitions(new_state)

    print(possible_transitions(initial_state))
    print(solution)
    print(cache)