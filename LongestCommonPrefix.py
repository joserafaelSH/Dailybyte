#["colorado", "color", "cold"], return "col"
#["a", "b", "c"], return ""
#["spot", "spotty", "spotted"], return "spot"

def pop(x:str):
    aux = list(x)
    if len(aux)>0:
        aux.pop()
        aux = ''.join(aux)
        return aux
    else:
        return False


def LCP(x:list)->str:
    falha = 0
    str_ = min(x)
    j = x.index(str_)
    while(len(str_)>0):
        for i in range(len(x)):
            if i != j:
                if x[i].find(str_) == -1:
                    falha = 1
                    break 
        if falha == 0:
            return str_
        else:
            falha = 0
        str_ = pop(str_)
        if str_ == False: return ""
    return ""

def test():
    assert(LCP(["colorado", "color", "cold"])) == "col"
    assert(LCP(["a", "b", "c"])) == ""
    assert(LCP(["spot", "spotty", "spotted"])) == "spot"

def main():
    test()

if __name__ == "__main__":
    main()