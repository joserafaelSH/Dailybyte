

def uncommonWords(n1:str, n2:str) -> list:
    l1 = n1.split(" ")
    l2 = n2.split(" ")
    s1 = set(l1)
    s2 = set(l2)
    r1 = []
    x = s1 & s2 
    r1 = (s1 | s2) - x
    return r1

def test():
    assert(uncommonWords("the quick","brown fox")) == ["the", "quick", "brown", "fox"]
    assert(uncommonWords("the tortoise beat the haire","the tortoise lost to the haire")) ==  ["beat", "to", "lost"]
    assert(uncommonWords("copper coffee pot","hot coffee pot")) ==  ["copper", "hot"]

def main():
    #test()
    print(uncommonWords("the quick","brown fox"))
    print(uncommonWords("the tortoise beat the haire","the tortoise lost to the haire"))
    print(uncommonWords("copper coffee pot","hot coffee pot"))


if __name__ == "__main__":
    main()