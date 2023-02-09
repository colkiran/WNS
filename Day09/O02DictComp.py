
d1 = [(x, y) for x in range(3) for y in range(3)]
print(d1)

print("-" * 40)
d2 = [(x, y) for x in range(1, 6) for y in range(1, x + 1)]
print(d2)

print("-" * 40)

players = {
    'sachin': [350, 250, 300, 400, 385],
    'rahul': [200, 300, 450, 150, 185],
    'sehwag': [300, 350, 425, 400, 360],
    'sourav': [180, 250, 200, 350, 150],
    'laxman': [345, 300, 200, 150, 190],
    'yuvraj': [190, 150, 120, 250, 275]
}

print(players['sachin'])
print(sum(players['sachin']))

print("-" * 40)
plrys = [k for k in players]
print(plrys)

print("-" * 40)
plyr_scr = {k : sum(v) for k, v in players.items()}
print(plyr_scr)

print("-" * 40)
plyr_scr = {k : (lambda scores: sum(scores) / len(scores)) (v)
            for k, v in players.items()}
print(plyr_scr)

print("-" * 40)
basic = [{x: (lambda par: "Mr." + par) ("sachin {}".format(x))}
         for x in range(1, 6)]
print(basic)

print("-" * 40)
vals = {(lambda par: par * 10)(k): (lambda par: par * par)(v)
        for k, v in {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}.items()}
print(vals)

players = {
    'sachin': [350, 250, 300, 400, 385],
    'rahul': [200, 300, 450, 150, 185],
    'sehwag': [300, 350, 425, 400, 360],
    'sourav': [180, 250, 200, 350, 150],
    'laxman': [345, 300, 200, 150, 190],
    'yuvraj': [190, 150, 120, 250, 275]
}

print("-" * 40)
scr = [plyr_scr for plyr_scr in players.values()]
print(scr)

print("-" * 40)
scr = [x for plyr_scr in players.values() for x in plyr_scr]
print(scr)

print("-" * 40)
scr = [x for plyr_scr in players.values() for x in plyr_scr if x >= 200]
print(scr)

print("-" * 40)
scrGrt200 = {name : [scr for scr in score if scr >= 200]
             for name, score in players.items()}
print(scrGrt200)
