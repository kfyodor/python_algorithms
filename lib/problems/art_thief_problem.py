def art_thief_problem(): # dynamic naive approach
    class ArtItem(object):
        def __init__(self, item_id, weight, value):
            self.item_id = item_id
            self.weight  = weight
            self.value   = value

    class Knapsack(object):
        def __init__(self, items):
            self.items = items

        def __lt__(self, k):
            return self.value() < k.value()

        def weight(self):
            return sum(map(lambda item: item.weight, self.items))

        def value(self):
            return sum(map(lambda item: item.value, self.items))

        def add(self, item):
            if self.has_item(item) or (self.weight() + item.weight) > 20:
                return False
            else:
                return Knapsack(self.items + [item])

        def has_item(self, item):
            return item in self.items

        def __str__(self):
            return "Weight: {}, Value: {}, Items: {}".format(
                self.weight(),
                self.value(),
                "-".join(map(lambda item: str(item.item_id), self.items))
            )

        def key(self):
            return str(sorted(map(lambda item: item.item_id, self.items)))

    items = [
        ArtItem(1, 2, 3),
        ArtItem(2, 3, 4),
        ArtItem(3, 4, 8),
        ArtItem(4, 5, 8),
        ArtItem(5, 9, 10)
    ]

    def art_thief_rec(n, knapsack, cache):
        item = items[n]

        new_knapsack = knapsack.add(item)

        if new_knapsack:
            if not new_knapsack.key() in cache.keys():
                cache[new_knapsack.key()] = ""
                return max([art_thief_rec(n, new_knapsack, cache) for n in range(0, len(items))])
            else:
                return new_knapsack
        else:
            return knapsack


    def solve():
        cache = {}
        knapsack = Knapsack([])
        return max([art_thief_rec(n, knapsack, cache) for n in range(0, len(items))])

    print("Grab those for max profit: {}".format(solve()))
