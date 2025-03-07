class R2Vector:
    def __init__(self, *, x: float, y: float):
        self.x = x
        self.y = y

    def norm(self) -> float:
        """Calculate the Euclidean norm of the vector."""
        return sum(val**2 for val in vars(self).values())**0.5

    def __str__(self) -> str:
        return str(tuple(getattr(self, i) for i in vars(self)))

    def __repr__(self) -> str:
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    def __add__(self, other: 'R2Vector') -> 'R2Vector':
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __sub__(self, other: 'R2Vector') -> 'R2Vector':
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __mul__(self, other: 'R2Vector') -> float:
        if type(other) in (int, float):
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            return self.__class__(**kwargs)        
        elif type(self) == type(other):
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            return sum(args)            
        return NotImplemented

    def __eq__(self, other: 'R2Vector') -> bool:
        if type(self) != type(other):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))
        
    def __ne__(self, other: 'R2Vector') -> bool:
        return not self == other

    def __lt__(self, other: 'R2Vector') -> bool:
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()

    def __gt__(self, other: 'R2Vector') -> bool:
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()

    def __le__(self, other: 'R2Vector') -> bool:
        return not self > other

    def __ge__(self, other: 'R2Vector') -> bool:
        return not self < other

class R3Vector(R2Vector):
    def __init__(self, *, x: float, y: float, z: float):
        super().__init__(x=x, y=y)
        self.z = z

    def norm(self) -> float:
        """Calculate the Euclidean norm of the vector."""
        return (self.x**2 + self.y**2 + self.z**2)**0.5
        
    def cross(self, other: 'R3Vector') -> 'R3Vector':
        if type(self) != type(other):
            return NotImplemented
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }
        
        return self.__class__(**kwargs)

v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5, y=1.25, z=2)
print(f'v1 = {v1}')
print(f'v2 = {v2}')
v3 = v1 + v2
print(f'v1 + v2 = {v3}')
v4 = v1 - v2
print(f'v1 - v2 = {v4}')
v5 = v1 * v2
print(f'v1 * v2 = {v5}')
v6 = v1.cross(v2)
print(f'v1 x v2 = {v6}')
