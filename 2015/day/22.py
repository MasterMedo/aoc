import random

def magic_missle(spell):
    global bHp
    bHp -= 4

def drain(spell):
    global bHp, mHp
    bHp -= 2
    mHp += 2

def shield(spell):
    global mDef
    mDef = 7
    recast(spell)

def poison(spell):
    global bHp
    bHp -= 3
    recast(spell)

def recharge(spell):
    global mana
    mana += 101
    recast(spell)

def recast(spell):
    global toCast, tmpCast, mDef
    spell['turns'] -= 1
    if spell['turns'] > 0:
        tmpCast[spell['name']] = spell
    elif spell['turns'] <= 0 and spell['name'] == 'shield':
        mDef = 0

def cast():
    global toCast, tmpCast
    for index in toCast:
        spell = toCast[index]
        spell['spell'](spell)
    toCast = tmpCast.copy()
    tmpCast = {}

spells = [
        {'name': 'magic_missle', 'cost': 53,  'turns': 1, 'spell': lambda spell: magic_missle(spell)},
        {'name': 'drain',        'cost': 73,  'turns': 1, 'spell': lambda spell: drain(spell)},
        {'name': 'shield',       'cost': 113, 'turns': 6, 'spell': lambda spell: shield(spell)},
        {'name': 'poison',       'cost': 173, 'turns': 6, 'spell': lambda spell: poison(spell)},
        {'name': 'recharge',     'cost': 229, 'turns': 5, 'spell': lambda spell: recharge(spell)}
        ]

with open('../input/22.txt') as fp:
    ibHp, ibAtt = [int(i.split(': ')[1]) for i in fp.readlines()]

m = float('inf')
while True:
    bHp, bAtt = ibHp, ibAtt
    mHp, mDef, mana = 50, 0, 500
    cnt, toCast, tmpCast = 0, {}, {}
    win, lose = False, False
    while not any([win, lose]):
        # my turn
        mHp -= 1 # comment for part 1
        cast()
        if mana < 53 or mHp <= 0:
            lose = True
            break
        elif bHp <= 0:
            win = True
            break
        spell = random.choice([spell.copy() for spell in spells \
            if spell['name'] not in toCast and spell['cost'] <= mana])
        mana -= spell['cost']
        cnt += spell['cost']
        toCast[spell['name']] = spell
        # boss turn
        cast()
        if bHp <= 0:
            win = True
            break
        mHp -= (bAtt - mDef) if bAtt - mDef > 0 else 1
    if win and cnt < m:
        m = cnt
        print cnt
