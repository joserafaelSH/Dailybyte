def anagrama(l:str, t:str):
    h1 = {}
    h2 = {}
    for i in range(len(l)):
        if not h1.get(l[i]):
            h1[l[i]] = 1 
        else:
            h1[l[i]] +=1

    for i in range(len(t)):
        if not h2.get(t[i]):
            h2[t[i]] = 1 
        else:
            h2[t[i]] +=1

    return True if h1==h2 else False

def test():
    assert(anagrama("cat","tac"))
    assert(anagrama("listen","silent"))
    assert(not anagrama("program","function"))

def main():
    test()



if __name__ == "__main__":
    main() 