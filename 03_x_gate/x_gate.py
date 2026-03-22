from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(1, 1)
qc.x(0)
qc.measure(0, 0)

sampler = StatevectorSampler()
job = sampler.run([qc])
result = job.result()

print(result[0].data.c.get_counts())