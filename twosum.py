#[1, 3, 8, 2], k = 10, return true (8 + 2)
#[3, 9, 13, 7], k = 8, return false
#[4, 2, 6, 5, 2], k = 4, return true (2 + 2)


def twosum(l:list, k:int) -> bool:
    for i in l:
        if i <= k:
            for j in range(i,len(l)):
                if i + l[j] == k:
                    return True

def test_twosum():
    assert(twosum([1, 3, 8, 2], 10))
    assert( not twosum([3, 9, 13, 7], 8))
    assert(twosum([4, 2, 6, 5, 2], 4))


def twosum_fon(l:list, k:int)->bool:
    sol = []
    hash = {}
    for i in range(len(l)):
        aux = k - l[i]
        if aux in hash:
            sol.append(l.index(hash.get(aux)))
            sol.append(i)
            return sol
        hash[l[i]] = l[i]
    
    return sol

def test_twofon():
    assert(twosum_fon([1, 3, 8, 2], 10))
    assert( not twosum_fon([3, 9, 13, 7], 8))
    assert(twosum_fon([4, 2, 6, 5, 2], 4))


def main():
    #test_twosum()
    #test_twofon() 
    #print(twosum_fon([1, 3, 8, 2], 10))
    print(twosum_fon([0,4,3,0],0))


if __name__ == "__main__":
    main()