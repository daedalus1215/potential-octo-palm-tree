### Consider Generator Expressions for Large List Comprehensions
import math

value = [len(x) for x in open('my_file.txt')]
print(value)

#### Generator
it = (len(x) for x in open('my_file.txt'))

roots = ((x, x ** 0.5) for x in it)

print(next(roots))


### Compose Multi Generators with yield from
def move(period, speed):
    for _ in range(period):
        yield speed


def pause(period):
    for _ in range(period):
        yield 0


def animate():
    for delta in move(4, 5.0):
        yield delta
    for delta in pause(3):
        yield delta
    for delta in move(2, 3):
        yield delta


for delta in animate():
    print(delta)


#### Use the yield from for cleaner code
def animate2():
    yield from move(4, 5.0)
    yield from pause(3)
    yield from move(2, 3)


for delta in animate2():
    print(delta)


### Avoid Injecting data into generators with send
def my_generator():
    received = yield 1
    print(f'received = {received}')


it = iter(my_generator())
output = next(it)
print(f'output = {output}')
try:
    next(it)
except StopIteration:
    pass


def transmit(output):
    if output is None:
        print(f'Output is None')
    else:
        print(f'Output: {output:>5.1f}')


def wave_modulating(steps):
    step_size = 2 * math.pi / steps
    amplitude = yield  # receive initial amplitude
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        doutput = amplitude * fraction
        amplitude = yield doutput  # receive next amplitude

def render(delta):
    print(f'Delta: {delta:.1f}')

def run(func):
    for delta in func():
        render(delta)

print('----------------------------')

def run_modulating(it):
    amplitudes = [None, 7, 7]
    ite = wave_modulating(12)
    for amplitude in amplitudes:
        output = ite.send(amplitude)
        transmit(output)

run_modulating(wave_modulating(12))

def wave(amplitude, steps):
    step_size = 2 * math.pi / steps
    for step in steps:
        radians = step * step_size
        fraction = math.sin(radians)
        doutput = amplitude * fraction
        yield doutput

def complex_wave():
    yield from wave(7.0, 3)
    yield from wave(2.0, 4)
    yield from wave(10.0, 5)

def complex_wave_modulating():
    yield from wave_modulating(3)
    yield from wave_modulating(4)
    yield from wave_modulating(5)

run_modulating(complex_wave_modulating())