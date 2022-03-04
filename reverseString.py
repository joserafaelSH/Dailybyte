
#“Cat”, return “taC”
#“The Daily Byte”, return "etyB yliaD ehT”
#“civic”, return “civic” ###

def reverseString(str_: list, start:int, end:int) -> list:

    if start < end:
        if start == end:
            return str_
        
        else:
            str_[start],str_[end] = str_[end],str_[start]
            return reverseString(str_, start+1,end-1)
    
    else:
        return str_


def test():
    assert("".join(reverseString(list("Cat"),0,len("Cat")-1))) == "taC"
    assert("".join(reverseString(list("The Daily Byte"),0,len("The Daily Byte")-1))) == "etyB yliaD ehT"
    assert("".join(reverseString(list("civic"),0,len("civic")-1))) == "civic"

def main():
    test()
   
if __name__ == "__main__":
    main()



#input: any string, but converted to list, converted by cast(list(str)), to able to switch your elements, index of the start and last chars
#output: the input string in reverse order, but in list shape. This list is converted to string by join method