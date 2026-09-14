def _show(value):
    if value is not None:
        print(repr(value))

# Python and NumPy tutorial — executable source adapted from aim-lab/mlh-course-material
import random
import numpy as np
random.seed(42)
np.random.seed(42)

# %% Cell 9: Hierarchy in Python: packages, modules and virtual environments
import sys
import random
import math as mt
from math import ceil as ce
print(f'A random number in [3 9] for exapmle is: ', random.uniform(3, 9))
print(mt.pi)
p = 2.4
print(mt.floor(p))
print(ce(p))

# %% Cell 19: Numbers
x = 3
print(x, type(x))

# %% Cell 20: Numbers
x = 5
print(x)
x += 1
print(x)
x -= 2
print(x)
x *= 8
print(x)
x /= 3
print(x)
x //= 4
print(x)

# %% Cell 24: Booleans
t, f = (True, False)

# %% Cell 26: Booleans
print(t and f)
print(t or f)
print(not t)
print(t != f)

# %% Cell 28: Strings
hello = 'hello'
world = 'world'
combined = '"hello world"'
print(combined)
_show((hello, combined, len(hello)))

# %% Cell 29: Strings
_show('aaa ' + 'bbb')

# %% Cell 31: Strings
s = 'hello'
a = [1, 2, 3]
print('%s %s: pi=%.5f' % (s, a, mt.pi))
print('{} {}: pi={:.5f}'.format(s, a, mt.pi))
print(f'{s} {a}: pi={mt.pi:.5f}')

# %% Cell 33: Strings
s = 'hello'
print(s.capitalize())
print(s.upper())
print(s.rjust(7))
print(s.center(7))
print(s.replace('l', '(ell)'))
print('  world '.strip())

# %% Cell 39: Lists
xs = [3, 1, 2]
print(xs)
print(xs[2], xs[-1])

# %% Cell 41: Lists
print(xs + [4, 5, 9])
print(3 * xs)

# %% Cell 42: Lists
xs[2] = 'foo'
print(xs)

# %% Cell 43: Lists
xs.append('bar')
print(xs)

# %% Cell 44: Lists
x = xs.pop()
print(x)
print(xs)

# %% Cell 46: Lists
x = []
x = list()

# %% Cell 49: Slicing
nums = list(range(5))
_show(nums)

# %% Cell 50: Slicing
_show(nums[2:4])

# %% Cell 51: Slicing
_show(nums[2:])

# %% Cell 52: Slicing
_show(nums[:2])

# %% Cell 53: Slicing
_show(nums[:])

# %% Cell 54: Slicing
_show(nums[:-1])

# %% Cell 55: Slicing
_show(nums[0:4:2])

# %% Cell 56: Slicing
nums[2:4] = [8, 9]
_show(nums)

# %% Cell 57: Slicing
nums[0:1] = []
del nums[-1]
_show(nums)

# %% Cell 60: Loops
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)

# %% Cell 62: Loops
animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print(f'#{idx + 1}: {animal}')

# %% Cell 65: List comprehensions
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
_show(squares)

# %% Cell 67: List comprehensions
squares = [x ** 2 for x in nums]
_show(squares)

# %% Cell 69: List comprehensions
even_squares = [x ** 2 for x in nums if x % 2 == 0]
_show(even_squares)

# %% Cell 71: List comprehensions
nums2 = [-1, 1]
_show([x * y for x in nums for y in nums2])

# %% Cell 73: List comprehensions
arr = [3, 6, 8, 0, 1, 2, 1]
print([x for x in arr if x < 3])

# %% Cell 76: Dictionaries
d = {'dog': 'cute', 'cat': 'evil'}
print(d['cat'])
print('cat' in d)

# %% Cell 77: Dictionaries
d['fish'] = 'silence'
_show(d)

# %% Cell 78: Dictionaries
try:
    d['monkey']
except KeyError as e:
    print(e, file=sys.stderr)

# %% Cell 79: Dictionaries
print(d.get('monkey', 'rr'))
print(d.get('fish', 'N/A'))

# %% Cell 80: Dictionaries
del d['fish']
_show(d)

# %% Cell 81: Dictionaries
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    print(f'A {animal} has {d[animal]} legs')

# %% Cell 82: Dictionaries
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, num_legs in d.items():
    print(f'A {animal} has {num_legs} legs')

# %% Cell 83: Dictionaries
_show(dict(foo=1, bar=2, baz=3))

# %% Cell 85: Dictionaries
d = {}
d = dict()

# %% Cell 88: Dictionary comprehensions
nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
_show(even_num_to_square)

# %% Cell 91: Sets
animals = {'cat', 'dog'}
print(animals)
print('cat' in animals)
print('fish' in animals)

# %% Cell 92: Sets
animals.add('fish')
print('fish' in animals)
_show(len(animals))

# %% Cell 93: Sets
animals.add('cat')
_show(animals)

# %% Cell 95: Sets
animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print(f'#{idx + 1}: {animal}')

# %% Cell 97: Sets
s = set()

# %% Cell 100: Set comprehensions
from math import sqrt
s = {int(sqrt(x)) for x in range(37)}
_show(s)

# %% Cell 103: Tuples
tup = (1, 2, 'three')
_show(tup)

# %% Cell 105: Tuples
_show((tup[0:1], tup[1:3], tup[-1], len(tup)))

# %% Cell 107: Tuples
d = {(x, x + 1): x for x in range(10)}
_show(d)

# %% Cell 109: Tuples
one, two, three = tup
print(one)
print(two)
print(three)

# %% Cell 111: Tuples
t = ()
t = tuple()

# %% Cell 115: Functions
def sign(x):
    if x > 0:
        y = 1
        return ('positive', y)
    elif x < 0:
        y = -1
        return ('negative', y)
    else:
        y = 0
        return ('zero', y)
for x in [-2, 0, 3]:
    print(sign(x))
    res, y = sign(x)
    print(res)
    print(y)

# %% Cell 117: Functions
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# %% Cell 118: Functions
print(quicksort(arr))

# %% Cell 120: Functions
def hello(name, loud=False):
    if loud:
        print('HELLO, %s' % name.upper())
    else:
        print('Hello, %s!' % name)
hello('Bob')
_show(hello('Fred', loud=True))

# %% Cell 123: Small anonymus functions - lambda
f1 = lambda a, b: a * b
print(f1(10, 5))
f2 = lambda x: 'mom' in x
example = ['kid', 'mom', 'dad']
print(f2(example))
f3 = lambda x: x.index('kid')
print(f3(example))

# %% Cell 126: Positional and Keyword arguments
def myfunc(a1, a2, a3, *extra_args, kw1='foo', kw2='bar', kw3=3, **extra_kwargs):
    print(f'Get positional args: {(a1, a2, a3)}')
    print(f'Get keyword args   : {dict(kw1=kw1, kw2=kw2, kw3=kw3)}')
    print(f'Get extra positional args: {extra_args}')
    print(f'Get extra keyword args: {extra_kwargs}')

# %% Cell 128: Positional and Keyword arguments
_show(myfunc(1, 2, 3, 4, 5, 6))

# %% Cell 129: Positional and Keyword arguments
my_args = [1, 2, 3, 4, 5]
_show(myfunc(*my_args))

# %% Cell 130: Positional and Keyword arguments
_show(myfunc(1, 2, 3, kw3=3, kw2=2, dog='cute'))

# %% Cell 131: Positional and Keyword arguments
my_kwargs = dict(kw1=1, kw2=2, kw3=3, kw4=4)
_show(myfunc(1, 2, 3, **my_kwargs))

# %% Cell 133: Positional and Keyword arguments
try:
    myfunc(1, 2)
except TypeError as e:
    print(e, file=sys.stderr)

# %% Cell 135: Classes
class Greeter:

    def __init__(self, name):
        self.name = name

    def greet(self, loud=False):
        if loud:
            print('HELLO, %s!' % self.name.upper())
            self.m = 1
        else:
            print('Hello, %s' % self.name)
            self.m = 0

    def greetback(self):
        if self.m == 1:
            print('HELLO TO YOU TOO!')
g = Greeter('Fred')
g.greet()
g.greetback()
g.greet(loud=True)
_show(g.greetback())

# %% Cell 138: Numpy
import numpy as np

# %% Cell 142: Arrays
a = np.array([1, 2, 3])
print(f'shape={a.shape},   a[1]={a[1]},   type={type(a)}')
a[0] = 5
_show(a)

# %% Cell 143: Arrays
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print('shape =', b.shape)

# %% Cell 144: Arrays
_show((b[0, 0], b[0, 1], b[1, 0]))

# %% Cell 146: Arrays
_show(np.zeros((2, 2)))

# %% Cell 147: Arrays
_show(np.zeros_like(b))

# %% Cell 148: Arrays
_show(np.ones((10, 1)))

# %% Cell 149: Arrays
_show(np.full((3, 3), 7.2))

# %% Cell 150: Arrays
_show(np.eye(4, dtype=int))

# %% Cell 151: Arrays
t = np.random.random((4, 4, 3))
_show(t)

# %% Cell 152: Arrays
_show(t[1, 1, 2])

# %% Cell 154: Rank-1 Arrays
a1 = np.array([1, 2, 3])
print(f'\n a1 {a1.shape}:\n', a1)
a_col = a1.reshape(-1, 1)
print(f'\n a_col {a_col.shape}:\n', a_col)
a_row = a1.reshape(1, -1)
print(f'\n a_row {a_row.shape}=\n', a_row)

# %% Cell 156: Rank-1 Arrays
print('\n a1 * a1 =', np.dot(a1, a1))
print('\n a_row * a1 =', a_row @ a1)
print('\n a1 * a_col =', a1 @ a_col)
print('\n a_row * a_col =', a_row @ a_col)
print('\n a_col * a_row =\n', a_col @ a_row)

# %% Cell 160: Slicing
import numpy as np
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
_show(a)

# %% Cell 161: Slicing
b = a[:2, 1:3]
print(b)

# %% Cell 163: Slicing
b[0, 0] = 77777
_show(a)

# %% Cell 165: Slicing
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
_show(a)

# %% Cell 166: Slicing
b = a[:2, 1:3]
b = 2 * b
print(b)

# %% Cell 167: Slicing
b[0, 0] = 77777
_show(a)

# %% Cell 169: Slicing
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
_show(a)

# %% Cell 171: Slicing
row_r1 = a[1, :]
row_r2 = a[1:2, :]
row_r3 = a[[1], :]
print(row_r1, 'shape=', row_r1.shape)
print(row_r2, 'shape=', row_r2.shape)
print(row_r3, 'shape=', row_r3.shape)

# %% Cell 172: Slicing
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)
print(col_r2, col_r2.shape)

# %% Cell 174: Integer array indexing 
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)

# %% Cell 175: Integer array indexing 
print(a[[0, 1, 2], [0, 1, 0]])
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))

# %% Cell 176: Integer array indexing 
print(a[[0, 0], [1, 1]])
print(np.array([a[0, 1], a[0, 1]]))

# %% Cell 178: Integer array indexing 
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
_show(a)

# %% Cell 179: Integer array indexing 
b = np.array([0, 2, 0, 1])
print(np.arange(4))
print(b)
_show(a[np.arange(4), b])

# %% Cell 180: Integer array indexing 
a[np.arange(4), b] += 1000
_show(a)

# %% Cell 182: Boolean array indexing
a = np.array([[1, 2], [3, 4], [5, 6]])
print('a=\n', repr(a))
bool_idx = a > 2
_show(bool_idx)

# %% Cell 183: Boolean array indexing
_show(a[a > 2])

# %% Cell 187: Datatypes
x = np.array([1, 2])
y = np.array([1.0, 2.0])
z = np.array([1, 2], dtype=np.int64)
_show((x.dtype, y.dtype, z.dtype))

# %% Cell 191: Elementwise operations
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)
print(x + y)
print(np.add(x, y))

# %% Cell 192: Elementwise operations
print(x - y)
print(np.subtract(x, y))

# %% Cell 193: Elementwise operations
print(x * y)
print(np.multiply(x, y))

# %% Cell 194: Elementwise operations
print(x / y)
print(np.divide(x, y))

# %% Cell 195: Elementwise operations
print(np.sqrt(x))

# %% Cell 198: Inner products
v = np.array([9, 10])
w = np.array([11, 12])
print(v.dot(w))
print(np.dot(v, w))

# %% Cell 199: Inner products
X = np.array([[1, 2], [3, 4]])
print('X =\n', repr(X))
print('Xv =', x.dot(v))

# %% Cell 200: Inner products
Y = np.array([[5, 6], [7, 8]])
print('Y= \n', repr(Y))
print('XY =\n', X.dot(Y))

# %% Cell 202: Inner products
x = np.array([[1, 2], [3, 4]])
print(np.sum(x))
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))

# %% Cell 204: Inner products
print(x)
print(x.T)
print(np.transpose(x))

# %% Cell 205: Inner products
v = np.array([1, 2, 3])
print(v.reshape(1, -1))
print(v.reshape(-1, 1))

# %% Cell 208: Broadcasting
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)
for i in range(4):
    y[i, :] = x[i, :] + v
_show(y)

# %% Cell 210: Broadcasting
vv = np.tile(v, (4, 1))
_show(vv)

# %% Cell 211: Broadcasting
y = x + vv
_show(y)

# %% Cell 213: Broadcasting
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v
print('shapes: ', x.shape, v.shape)
_show(y)

# %% Cell 215: Broadcasting
v = np.array([1, 2, 3])
w = np.array([4, 5])
_show(np.reshape(v, (3, 1)) * w)

# %% Cell 216: Broadcasting
print(x)
_show(x * 2)
