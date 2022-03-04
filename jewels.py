#jewels = "abc", stones = "ca", return 2
#jewels = "Af", stones = "AaaddfFf", return 3
#jewels = "AYOPD", stones = "ayopd", return 0



def jewels(jewels:str, stones:str) -> int:
    cont = 0
    for i in stones:
        if i in jewels:
            cont+=1
    return cont

def jewels2(jewels:str, stones:str) -> int:
    hash = {jewels[i]:1 for i in range(len(jewels))}
    cont = 0
    for i in stones:
        if hash.get(i):
            cont+=1
    return cont

def teste():
    assert(jewels("abc","ac")) == 2
    assert(jewels("Af","AaaddfFf")) == 3
    assert(jewels("AYOPD","ayopd")) == 0
    assert(jewels2("abc","ac")) == 2
    assert(jewels2("Af","AaaddfFf")) == 3
    assert(jewels2("AYOPD","ayopd")) == 0

def main():
    teste()

if __name__ == "__main__":
    main()