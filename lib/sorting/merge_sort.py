def merge_sort_rec(_list):
    def sort(_list):
        if len(_list) == 0 or len(_list) == 1:
            return _list
        else:
            (left, right) = split(_list)
            return merge(sort(left), sort(right))

    def merge(left, right):
        if len(left) == 0 or len(right) == 0:
            return left or right
        else:
            (l, *ls) = left
            (r, *rs) = right

            if l > r:
                return [r] + merge(left, rs)
            else:
                return [l] + merge(ls, right)

    def split(_list):
        if len(_list) <= 1:
            return (_list, [])
        else:
            (x, y, *xys) = _list
            (xs, ys)     = split(xys)
            return ([x] + xs, [y] + ys)

    sort(_list)