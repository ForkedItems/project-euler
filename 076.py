'''
This problem is a variant of P0078

1   = 1

2   = 2
    = 1 + 1

3   = 3
    = 2 + 1
    = 1 + 1 + 1

4   = 4
    = 3 + 1
    = 2 + 2
    = 2 + 1 + 1
    = 1 + 1 + 1 + 1

5   = 5
    = 4 + 1
    = 3 + 2
    = 3 + 1 + 1
    = 2 + 2 + 1
    = 2 + 1 + 1 + 1
    = 1 + 1 + 1 + 1 + 1

6   = 6
    = 5 + 1
    = 4 + 2
    = 4 + 1 + 1
    = 3 + 3
    = 3 + 2 + 1
    = 3 + 1 + 1 + 1
    = 2 + 2 + 2
    = 2 + 2 + 1 + 1
    = 2 + 1 + 1 + 1 + 1
    = 1 + 1 + 1 + 1 + 1 + 1

7   = 7
    = 6 + 1
    = 5 + 2
    = 5 + 1 + 1
    = 4 + 3
    = 4 + 2 + 1
    = 4 + 1 + 1 + 1
    = 3 + 3 + 1
    = 3 + 2 + 2
    = 3 + 2 + 1 + 1
    = 3 + 1 + 1 + 1 + 1
    = 2 + 2 + 2 + 1
    = 2 + 2 + 1 + 1 + 1
    = 2 + 1 + 1 + 1 + 1 + 1
    = 1 + 1 + 1 + 1 + 1 + 1 + 1

'''


from euler import partition as p


assert 7 == p(5)
assert 56 == p(11)
assert 190569291 == p(100)-1    # excluding itself (1-partition)
print p(100)-1
