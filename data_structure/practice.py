def test(v):
    if v < 11:
        print(v)
        test(2*v)
        test(2*v+1)


test(1)
