from logic_gates import AND, OR, NOT, XOR

def half_adder(a,b):
    SUM = XOR(a,b)
    CARRY = AND(a,b)
    return SUM,CARRY

def full_adder(a,b,c):
    SUM1,CARRY1 = half_adder(a,b)
    SUM2,CARRY2 = half_adder(SUM1,c)
    
    cout=OR(CARRY1,CARRY2)    
    return SUM2,cout


    