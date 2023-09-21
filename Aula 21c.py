def teste(b):
    global a #o Global transforma a váriavel a em global, ou seja, independente de onde ela esteja no códico seu valor será 8.
    a = 8
    b = b + 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')