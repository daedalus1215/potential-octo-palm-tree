from urllib.parse import parse_qs
from collections.abc import MutableMapping
import SetDefaultVisits
import DefaultDictVisit

# key = 'my_var'
# value = 1.234
# print('%-1s = %.3f' % (key,value))


pantry = [
    ('avocados', 1.25),
    ('bananas', 2.5),
    ('cherries', 15)
]
# # for i, (item, count) in enumerate(pantry):
# #     print(f'{item} = {round(count)}')

# for i, (item, count) in enumerate(pantry):
#     print(f'#{i+1}: '
#     f'{item.title():<10s} = '
#     f'{round(count)}')

my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print(repr(my_values))
print(f'red_str = {my_values.get("red")[0]}')
print(f'blue_str = {my_values.get("blue")[0]}')
print(f'green_str = {my_values.get("green")[0]}')
print(f'opacity = {my_values.get("opacity", [""])[0]}')
print('---------------------')
red_str = my_values.get('red', [''])
print(int(red_str[0]) if red_str[0] else 0)
opaicty_str = my_values.get('opacity', [''])
print(int(opaicty_str[0]) if opaicty_str[0] else 0)


def get_first_value(values, key, default=0):
    """ Let's check to make sure we have a value """
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default


print(get_first_value(my_values, 'red', 10))

favorite_snacks = {
    'salty': ('pretzels', 100),
    'sweet': ('cookies', 180),
    'veggie': ('carrots', 20)
}

((type1, (name1, cals1)),
 (type2, (name2, cals2)),
 (type3, (name3, cals3))) = favorite_snacks.items()

print(f'Favorite {type1} is {name1} with {cals1} calories')

print('---------------------')


def bubble_sort(a_a):
    """ yes"""
    for _ in range(len(a_a)):
        for i in range(1, len(a_a)):
            if a_a[i] < a_a[i - 1]:
                temp = a_a[i]
                a_a[i] = a_a[i-1]
                a_a[i-1] = temp


def bubble_sort2(a_a):
    """ yes"""
    for j in enumerate(a_a):
        for i in range(1, (a_a)):
            if a_a[j] < a_a[i]:
                temp = a_a[i]
                a_a[i] = a_a[j]
                a_a[j] = temp


tester = ['orange', 'green', 'blue']
bubble_sort(tester)
print(tester)


snacks = [('bacon', 350), ('donut', 240), ('muffin', 190)]

for rank, (name, calories) in enumerate(snacks, 1):
    print(f'#{rank}: {name} has {calories} calories')


for i, (item, count) in enumerate(pantry):
    print(f'#{i + 1}: '
          f'{item.title():<10s} = '
          f'{round(count)}')

names = ['Cecilia', 'Lisa', 'Marie']
counts = [len(n) for n in names]
print(counts)

max_count = 0
longest_name = ''
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count
print(max_count)
print(longest_name)


count = 0

fresh_fruit = {
    'lemon': 10,
    'oranges': 12,
    'apples': 2
}


def make_lemonade(count):
    print(f'Making lemonade with: {count} count')


def out_of_stock():
    print('we are out of stock')


if 0 != fresh_fruit.get('lemon', 0):
    make_lemonade(count)
else:
    out_of_stock()

if count := fresh_fruit.get('lemon', 0):
    make_lemonade(count)
else:
    out_of_stock()

if count := fresh_fruit.get('lemon', 0) >= 4:
    make_lemonade(count)
else:
    out_of_stock()


def slice_bananas(count):
    print(f'sliced bananas, returning {count} count')
    return count


def make_smoothies(pieces):
    return f'making smoothies with {pieces} pieces'


def make_cider(count):
    print(f'Making cider with {count} count')
    return count


count = 0

if (count := fresh_fruit.get('banana', 0) >= 2):
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
elif (count := fresh_fruit.get('apple', 0) >= 4):
    to_enjoy = make_cider(count)
else:
    to_enjoy = 'Nothing'

print(f'to enjoy {to_enjoy}')


a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print('middle two: ', a[3:5])


class Tool:
    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight

    def __repr__(self) -> str:
        return f'Tool({self.name}, {self.weight})'


tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.5),
    Tool('handwrench', 0.5),
    Tool('chisel', 0.25)
]

tools.sort(key=lambda x: (-x.weight, x.name))
print(f'tools sorted looks like {tools}')

votes = {
    'otter': 1281,
    'polar bear': 589,
    'fox': 863
}


def populate_ranks(votes, ranks):
    """ check """
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


def get_winner(ranks):
    """ Return the first result from the dict, since it is expected to be in order due to ython 3.6+ """
    return next(iter(ranks))


def get_winner_2(ranks):
    """ Sort the ranks, could be redundant - they might already be sorted - but covers the case of a custom iterable that is not a dict and cannot guarantee order of elements. """
    for name, rank in ranks.items():
        if rank == 1:
            return name


def get_winner_3(ranks):
    """ This will be faster than get_winner_2, since we will not be needlessly sorting ranks. """
    if not isinstance(ranks, dict):
        raise TypeError('must provide a dict instance')
    return next(iter(ranks))


ranks = {}
populate_ranks(votes, ranks)
print(ranks)
winner = get_winner(ranks)
print(winner)


class SortedDict(MutableMapping):
    """Testing"""

    def __init__(self) -> None:
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __iter__(self):
        print(f'keys are = {self.data.keys()}')
        keys = list(self.data.keys())
        print(f'list of keys are {keys}')
        keys.sort()
        for key in keys:
            yield key

    def __delitem__(self, key):
        del self.data[key]

    def __len__(self):
        return len(self.data)


sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(f'{next(iter(ranks))} {next(iter(ranks))}')

print('------------------------')

old_visits = {
    'Mexico': {'Tulum', 'Puerto Vallarta'},
    'Japan': {'Hakone'},
}

# Short way of setting a default, if no value exists for France
old_visits.setdefault('France', set()).add('Aries')
# Long way of setting a default, if no value exists for Japan
if (japan := old_visits.get('Japan')) is None:
    old_visits['Japan'] = japan = set()
    japan.add('Koyoto')

print(old_visits)

print('------------------------')
visit = SetDefaultVisits.Visits()
visit.add('Russia', 'Yekaterinburg')
visit.add('Tanzania', 'zanziba')
visit.add('Tanzania', 'another')

print(visit.data)

print('------------------------')
visit2 = DefaultDictVisit.Visits()
visit2.add('England', 'Bath')
visit2.add('England', 'London')
print(visit2.data)
