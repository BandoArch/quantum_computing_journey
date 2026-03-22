from qiskit import QuantumCircuit

# Create a circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply X gate (quantum NOT - flips |0> to |1>)
qc.x(0)

# Measure the qubit
qc.measure(0, 0)

# Draw the circuit
print(qc.draw())