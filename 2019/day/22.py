def get_coefficients(length):
    a, b = 1, 0
    with open('../input/22.txt') as f:
        for cmd, *_, n in map(str.split, f):
            if cmd == 'deal' and n.startswith('stack'):
                b = (length - 1 - b) % length

            elif cmd == 'cut':
                b = (b - int(n)) % length

            else:
                a = a*int(n) % length
                b = b*int(n) % length
    return a, b


card = 2019
length = 10007
a, b = get_coefficients(length)
print(position := (a * card + b) % length)

position = 2020
length = 119315717514047
iterations = 101741582076661
a, b = get_coefficients(length)

inv_a = pow(a, length - 2, length)
inv_a_to_k = pow(inv_a, iterations, length)
coef = ((inv_a_to_k - 1) * pow(inv_a - 1, length - 2, length) - 1) % length
print(((position - b) * inv_a_to_k - b * coef) % length)
