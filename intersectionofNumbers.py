

def intersection(n1:list, n2:list) -> list:
    s1 = set(n1)
    s2 = set(n2)
    l = list(s1 & s2) 

    return l 

def test():
    assert(intersection([2, 4, 4, 2],[2, 4])) == [2, 4]
    assert(intersection([1, 2, 3, 3],[3, 3])) ==  [3]
    assert(intersection([2, 4, 6, 8],[1, 3, 5, 7])) ==  []

def main():
    test()

if __name__ == "__main__":
    main()