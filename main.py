class Vector:
    def __init__(self, coord: list[int]):
        self.coord = coord

    def __len__(self):
        return len(self.coord)

    def __str__(self):
        return f"Vector({', '.join(map(str, self.coord))})"

    def __add__(self, other):
        if isinstance(other, Vector):
            new_coord = self.coord.copy()
            for i, item in enumerate(other.coord):
                new_coord[i] += item
            return Vector(new_coord)
        raise TypeError(f"Vector unsupported + with {other.__class__.__name__}")


v1 = Vector([1, 2, 3, 4])
v2 = Vector([7, 8, 9])
v3 = 10
print(v1 + v2)
