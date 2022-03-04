def byte(str_:str)->int:
    hash = {} 
    for i in str_:
        if hash.get(i):
            hash[i] += 1
        else:
            hash[i] = 1 
    print(hash)
    for i in range(len(str_)):
        if hash.get(str_[i]) == 1:
            return i
    
    return -1

def test():
    assert(byte("abcabd")) == 2
    assert(byte("thedailybyte")) == 1
    assert(byte("developer")) == 0
    assert(byte("aaabbccdd")) == -1  


def main():
    test()

if __name__ == "__main__":
    main()

