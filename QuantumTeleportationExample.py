#Quantum teleportation
#By: Brady Phelps
#GitHub @ BP-2
from qiskit import * 
from QuantumTeleportationUniversal import Teleportation 

#Gather input values
print("Hello, which Qubit would you like to make your original Qubit? (1,2, or 3)")
original = input("Number: ")

#ec
while (original != "1" and original != "2" and original != "3"):
    print("incorrect input, please enter 1, 2, or 3")
    original = input("Number: ")
original = int(original)-1
print("Which qubit would you like to make your target? (1,2, or 3 but not the same as original bit)")
target = input("Number: ")

#ec
while(original == target or (target != "1" and target != "2" and target != "3")):
    print("incorrect input, please enter 1, 2, or 3 but not the same as original bit")
    target = input("Number: ")
target = int(target)-1
print("Would you like to transfer a 0, 1, or 1/sqrt(2)?  (input a 0, 1, or 2 respectively)")
op = input("Operation number: ")

#ec
while(op != "0" and op != "1" and op != "2"):
    print("incorrect input, please enter 0, 1, or 2")
    op = input("Operation number: ")
print("Running circuit to transfer data from bit " + str(original+1) + " to bit " + str(target+1))

#create circuit
qc = QuantumCircuit(3,3)

#assign op
match op:
    case "0":
        print("")
    case "1":
        qc.x(original)
    case "2":
        qc.h(original)
    case other:
        print("Error")

#prolly inefficient way of grabbing freebit value
blandList = [0,1,2]
freeBit = 0
for x in blandList:
    if original != x and target != x:
        freeBit = x

#print(str(original) + str(target) + str(freeBit))

#call teleportation
Teleportation(qc, original, target, freeBit)