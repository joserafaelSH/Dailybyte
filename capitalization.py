
from curses.ascii import islower, isupper


def verification(str_:str, start:int, fnc)->bool:
    for i in range(start,len(str_)):
        if not fnc(str_[i]):
            return False
    return True

def capitalization(str_:str)->bool:
    if len(str_)> 1:
        if str_[0].islower():
            return verification(str_,1, islower)
            
        if str_[0].isupper() and str_[1].islower() :
            return verification(str_,1,islower)
        
        if str_[0].isupper() and str_[1].isupper() :
            return verification(str_,2,isupper)
    else:
        return True


def teste():
    assert(capitalization("USA")) == True
    assert(capitalization("Calvin")) == True
    assert(capitalization("compUter")) == False
    assert(capitalization("coding")) == True

def main():
    teste()

if __name__ == "__main__":
    main()