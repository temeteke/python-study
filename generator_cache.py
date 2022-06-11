class CachedGenerator:
    def __init__(self, generator):
        self.generator = generator
        self.items = []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        if key < len(self.items):
            return self.items[key]

        while True:
            try:
                self.items.append(next(self.generator))
            except StopIteration:
                raise IndexError
            try:
                return self.items[key]
            except IndexError:
                pass

    def __iter__(self):
        return self

    def __contains__(self, item):
        return item in self.items

    def __next__(self):
        item = next(self.generator)
        self.items.append(item)
        return item


def my_generator():
    for i in range(10):
        print(f'Generating {i}')
        yield i


cg = CachedGenerator(my_generator())
print(cg[0])
print(cg[1])
print(cg[0])
print(cg[-1])
print(0 in cg)
print(len(cg))
print(2 in cg)
print(next(cg))
print(2 in cg)
