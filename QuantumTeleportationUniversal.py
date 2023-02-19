#Quantum teleportation
#By: Brady Phelps
#GitHub @ BP-2
from qiskit import * 
from qiskit.tools.visualization import plot_histogram

#arguments (QuantumCircuit(x,x), int originBit, int targetBit, int freeBit)
#this will work for a 3 qubit state
def Teleportation(qc, originBit, targetBit, freeBit):
    #create entanglement between freebit and target bit
    qc.h(freeBit)
    qc.cx(freeBit,targetBit)
    #create entanglement(reverse) between originBit and freeBit
    qc.cx(originBit,freeBit)
    qc.h(originBit)
    #measure originBit and freeBit
    qc.measure([originBit,freeBit],[originBit,freeBit])
    #work back out the correct value
    qc.cx(freeBit,targetBit)
    qc.cz(originBit,targetBit)
    #measure and simulate and get counts
    qc.measure([targetBit],[targetBit])
    sim = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend = sim, shots = 1024).result()
    counts = result.get_counts()
    print(counts)
