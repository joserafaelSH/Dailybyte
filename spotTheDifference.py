
def byte(a:str, b:str)->str:
    hashA = {} 
    hashB = {} 
    for i in a:
        if hashA.get(i):
            hashA[i] += 1
        else:
            hashA[i] = 1
    
    for i in b:
        if hashB.get(i):
            hashB[i] += 1
        else:
            hashB[i] = 1

    
    for i in b:
        if not (hashB.get(i) and hashA.get(i)):
            return i 
       
    return ""

def test():
    assert(byte("foobar","barfoot")) == 't'
    assert(byte("ide","idea")) == 'a'
    assert(byte("coding","ingcod")) == ''

def main():
    test()


if __name__ == "__main__":
    main()
