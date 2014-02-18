def pascal_triangle(n):
    def coeff(n, r):
        return int(factorial(n) / (factorial(r) * factorial(n - r)))

    def print_center(arr, n):
        l = len(arr)

        arr = ['']*((n + 1 - l)) + arr

        print("  ".join(map(str, arr)))

    def pascal_rec(n):
        if n == 0:
            return [[1]]
        else:
            row = []
            for r in range(0, n + 1):
                row.append(coeff(n, r))

            return pascal_rec(n - 1) + [row]

    for r in pascal_rec(n):
        print_center(r, n)