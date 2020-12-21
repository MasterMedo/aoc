from lark import Lark, LarkError
from contextlib import suppress


def solve(rules, messages):
    rules = rules.translate(str.maketrans('0123456789', 'abcdefghij'))
    parser = Lark(rules, start='a')
    match = 0
    for line in messages.splitlines():
        with suppress(LarkError):
            parser.parse(line)
            match += 1
    return match


with open('../input/19.txt') as f:
    rules, messages = f.read().split('\n\n')

print(solve(rules, messages))
rules = rules.replace('8: 42', '8: 42 | 42 8')
rules = rules.replace('11: 42 31', '11: 42 31 | 42 11 31')
print(solve(rules, messages))
