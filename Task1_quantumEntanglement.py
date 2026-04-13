
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


qc = QuantumCircuit(2, 2)


qc.h(0)


qc.cx(0, 1)


qc.measure(0, 0)
qc.measure(1, 1)


print("The Quantum Circuit:")
print(qc.draw())


simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()


print("Measurement Results (out of 1000 shots):")
print(counts)
print("We only see '00' and '11' -- never '01' or '10'.")
print("This is because the qubits are entangled!")


plot_histogram(counts, title="Bell State Measurement Results")
plt.show()