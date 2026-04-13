
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt



# STEP 1: Build the Oracle

def make_oracle(num_qubits):
    """
    This oracle marks the state |11> as the correct answer.
    It flips the sign (phase) of |11> and leaves everything else unchanged.
    """
    oracle = QuantumCircuit(num_qubits, name="Oracle")
    
    
    oracle.cz(0, 1)
    
    return oracle


# STEP 2: Build the Diffuser (Amplitude Amplification)


def make_diffuser(num_qubits):
    """
    This is the diffusion operator (also called Grover diffuser).
    It amplifies the probability of the marked state.
    """
    diffuser = QuantumCircuit(num_qubits, name="Diffuser")
    
    
    diffuser.h([0, 1])
    
    
    diffuser.x([0, 1])
    
    
    diffuser.cz(0, 1)
    
    
    diffuser.x([0, 1])
    
    
    diffuser.h([0, 1])
    
    return diffuser



# STEP 3: Build the Full Grover's Circuit

def build_grovers_circuit():
    """
    Builds the complete Grover's algorithm circuit for 2 qubits.
    Target state: |11>
    """
    num_qubits = 2
    
    
    circuit = QuantumCircuit(num_qubits, num_qubits)
    
    
    circuit.h([0, 1])
    circuit.barrier()  
    
    
    num_iterations = 1
    
    
    oracle = make_oracle(num_qubits)
    diffuser = make_diffuser(num_qubits)
    
    
    for i in range(num_iterations):
        circuit.append(oracle, [0, 1])
        circuit.barrier()
        circuit.append(diffuser, [0, 1])
        circuit.barrier()
    
    
    circuit.measure([0, 1], [0, 1])
    
    return circuit



# STEP 4: Run the circuit and see results

def run_grovers():
    print("=" * 50)
    print("Grover's Algorithm - 2 Qubit Example")
    print("Target State: |11>")
    print("=" * 50)
    
    
    circuit = build_grovers_circuit()
    
    
    print("\nQuantum Circuit:")
    print(circuit.draw(output='text', fold=-1))
    
    
    simulator = AerSimulator()
    
   
    compiled_circuit = transpile(circuit, simulator)
    
    
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(compiled_circuit)
    
    
    print("\nMeasurement Results (out of 1000 shots):")
    print("-" * 30)
    for state, count in sorted(counts.items()):
        percentage = (count / 1000) * 100
        bar = "#" * (count // 20)  
        print(f"  |{state}> : {count:4d} times ({percentage:.1f}%)  {bar}")
    
    print("\n")
    
    
    most_common = max(counts, key=counts.get)
    print(f"Most frequent result: |{most_common}>")
    print(f"This matches our target state |11>: {most_common == '11'}")
    
    print("\nExplanation:")
    print("  Before Grover's: each state had ~25% chance (equal superposition)")
    print("  After Grover's:  |11> should have ~100% chance (amplified!)")
    
   
    
    fig = plot_histogram(counts, title="Grover's Algorithm Results\n(Target: |11>)")
    plt.tight_layout()
    plt.savefig("grover_results.png", dpi=150, bbox_inches='tight')
    plt.show()
    


    return counts, circuit



# STEP 5: Also show step-by-step probabilities

def show_step_by_step():
    
    print("\n" + "=" * 50)
    print("Step-by-Step State Probabilities")
    print("=" * 50)
    
    from qiskit_aer import AerSimulator
    from qiskit.quantum_info import Statevector
    
    num_qubits = 2
    
    
    init_circuit = QuantumCircuit(num_qubits)
    init_circuit.h([0, 1])
    sv = Statevector.from_instruction(init_circuit)
    probs = sv.probabilities_dict()
    
    print("\nAfter H gates (superposition):")
    for state, prob in sorted(probs.items()):
        print(f"  |{state}> : {prob:.4f}  ({prob*100:.1f}%)")
    
    
    oracle_circuit = QuantumCircuit(num_qubits)
    oracle_circuit.h([0, 1])
    oracle_circuit.cz(0, 1)  
    sv2 = Statevector.from_instruction(oracle_circuit)
    probs2 = sv2.probabilities_dict()
    
    print("\nAfter Oracle (probabilities look same, but phase of |11> flipped):")
    print("(Phase flip is invisible in probabilities - it shows up after diffuser)")
    for state, prob in sorted(probs2.items()):
        print(f"  |{state}> : {prob:.4f}  ({prob*100:.1f}%)")
    
    
    full_circuit = QuantumCircuit(num_qubits)
    full_circuit.h([0, 1])
    full_circuit.cz(0, 1)       
    full_circuit.h([0, 1])      
    full_circuit.x([0, 1])
    full_circuit.cz(0, 1)
    full_circuit.x([0, 1])
    full_circuit.h([0, 1])      
    sv3 = Statevector.from_instruction(full_circuit)
    probs3 = sv3.probabilities_dict()
    
    print("\nAfter Oracle + Diffuser (1 full iteration):")
    for state, prob in sorted(probs3.items()):
        bar = "█" * int(prob * 40)
        print(f"  |{state}> : {prob:.4f}  ({prob*100:.1f}%)  {bar}")
    
    print("\nAs you can see, |11> now has ~100% probability!")




if __name__ == "__main__":
    
    counts, circuit = run_grovers()
    
    
    show_step_by_step()