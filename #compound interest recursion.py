def compound(p, r, t):
    while t > 0:
        p = p * (1 + (r/100))
        t-=1
        compound(p, r, t)
    return p
print(compound(6000, 7.5, 50))
100,5,4