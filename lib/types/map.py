# this code is ugly

class Map(object):
    def __init__(self, size):
        self.size   = size
        self.keys   = [None] * size
        self.values = [None] * size

    def __getitem__(self, key):
        return self.__get(key)

    def __setitem__(self, key, value):
        self.__put(key, value)

    def __get(self, key):
        stop = False
        value = None
        index = self.__hash(key)

        if self.keys[index] == key:
            value = self.values[index]
        else:
            new_index = self.__rehash(index)

            while not stop and self.keys[new_index] != None:
                if self.keys[new_index] == key:
                    stop = True
                    value = self.values[index]
                else:
                    new_index = self.__rehash(new_index)
                    if new_index == index: stop = True

        return value




    def __put(self, key, value):
        index = self.__hash(key)
        stop  = False

        if not self.keys[index]:
            self.keys[index] = key
            self.values[index] = value
        elif self.keys[index] == key:
            self.values[index] = value
        else:
            new_index = self.__rehash(index)
            while not stop and self.keys[new_index] not in [None, key]:
                new_index = self.__rehash(new_index)
                if new_index == index: stop = True

            if not stop:
                self.keys[new_index] = key
                self.values[new_index] = value


    def __hash(self, key):
        return key % self.size

    def __rehash(self, oldhash):
        return (oldhash + 1) % self.size
