def palindrome1(l:list, start:int, end:int) -> bool:
    if start >= end: return True 
    
    if l[start] == l[end]:
        return palindrome1(l,start+1,end-1)

    else:
        return False

def palindrome2(l:list, start:int, end:int) -> bool:
    if start >= end: return True 
    
    if l[start] == l[end]:
        return palindrome2(l,start+1,end-1)

    else:
        return palindrome1(l,start+1,end) or palindrome1(l,start,end-1)
        

def test():
    assert(palindrome2("abcba",0,len("abcba")-1))
    assert(palindrome2("foobof",0,len("foobof")-1))
    assert(not palindrome2("abccab",0,len("abccab")-1))

def main():
    test()
    

if __name__ == "__main__":
    main()