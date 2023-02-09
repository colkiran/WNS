
fruits = [
    ('apple', 285),
    ('orange', 85),
    ('grapes', 140),
    ('pineapple', 70),
    ('Banana', 65),
    ('gauva', 120),
    ('Watermelon', 150),
    ('strawberry', 325)
]

print(f"fruits :{fruits}")

print("-" * 40)
prices = ["fruit" for fruit in fruits]
print(prices)

print("-" * 40)
prices = [fruit for fruit in fruits]
print(prices)

print("-" * 40)
prices = [fruit[0] for fruit in fruits]
print(prices)

print("-" * 40)
prices = [fruit[1] for fruit in fruits]
print(prices)

print("-" * 40)
prices = [fruit[1] * 0.9 for fruit in fruits]
print(prices)

print("-" * 40)
prices = [fruit[1] * 0.75 for fruit in fruits]
print(prices)

fruits = [
    ('apple', 285),
    ('orange', 85),
    ('grapes', 140),
    ('pineapple', 70),
    ('Banana', 65),
    ('gauva', 120),
    ('Watermelon', 150),
    ('strawberry', 325)
]

print("-" * 40)
expFrts = [fruit for fruit in fruits if fruit[1] > 100]
print(expFrts)

print("-" * 40)
expFrts = [[fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75] for fruit in fruits if fruit[1] > 100]
print(expFrts)

print("-" * 40)
sentence  = "the quick brown fox jumps over the lazy dog"
print(sentence)

words = [word for word in sentence.split()]
print(words)

words = [word for word in sentence.split() if word != 'the']
print(words)

words = [(word, len(word)) for word in sentence.split() if word != 'the']
print(words)

print("-" * 40)
lst = [n ** 2 for n in range(1, 11)]
print(lst)

print("-" * 40)
boys = ['mike', 'louis', 'charles', 'richard', 'kennedy', 'peter', 'ruben']
girls = ['grace', 'jenifer', 'mary', 'tina', 'tanya', 'belcia', 'aliyah']

combine = [(boy, girl) for boy in boys for girl in girls]
print(combine)

print("-" * 40)
combine  = list(zip(boys, girls))
print(combine)
