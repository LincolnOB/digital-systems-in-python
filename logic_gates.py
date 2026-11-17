
# A=int(input("input logic value: "))
# B=int(input("input logic value: "))

# AND gate
def AND(A,B):
    if (A and B) == 1:
         return 1
    else:
        return 0
    
# OR gate   
def OR(A,B):
    if A or B==1:
        return 1
    else:
        return 0
    
# NOT gate 
def NOT(A):
    if A==1:  
        return 0
    else:
        return 1
    
# NAND gate              
def NAND(A,B):
    if A and B == 1:
        return 0
    else:
        return 1   
    
# NOR gate
def NOR(A,B):
    if A or B ==1:
        return 0
    else:
        return 1     

# XOR gate
def XOR(A,B):
    if A == B:
        return 0
    else:
        return 1    
 
# XNOR gate    
def XNOR(A,B):
    
    if A==B:
        return 1 
    else:
        return 0



