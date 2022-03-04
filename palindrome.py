#"level", return true
#"algorithm", return false
#"A man, a plan, a canal: Panama.", return true


#0 1 2 3 4
#l e v e l


from curses.ascii import isalpha


def validPalindrome(str_: str, start:int, end:int) -> bool:

    if start <= end:
        if start == end:
            return True
        
        else:
            if not isalpha(str_[start]):
                return validPalindrome(str_, start+1,end)
            elif not isalpha(str_[end]):
                return validPalindrome(str_, start,end-1)
            elif str_[start].lower()  == str_[end].lower():
                return validPalindrome(str_, start+1,end-1)
            else:
                return False
    else:
        return False

    


def test():
    assert(validPalindrome("level",0,len("level")-1)) == True
    assert(validPalindrome("algorithm",0,len("algorithm")-1)) == False
    assert(validPalindrome("A man, a plan, a canal: Panama.",0,len("A man, a plan, a canal: Panama.")-1)) == True

def main():
    test()
   
if __name__ == "__main__":
    main()



#input: any string, but converted to list, converted by cast(list(str)), to able to switch your elements, index of the start and last chars
#output: the input string in reverse order, but in list shape. This list is converted to string by join method