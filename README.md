# QC @ IIT Indore Induction 2026

This repository contains the code and theoretical explanations for the Quantum Computing Club inductions at IIT Indore (2026). It includes the implementation of fundamental quantum circuits and search algorithms using IBM's Qiskit framework.

##  Prerequisites & Installation

To run these scripts, you need to have Python installed along with the Qiskit libraries and Matplotlib for visualizations.

```bash
pip install qiskit qiskit-aer matplotlib
```
## Task 1 — Bell State Quantum Circuit

### Problem
Build a 2-qubit quantum circuit that creates an entangled state using:
- A **Hadamard gate** on qubit 0 (creates superposition)
- A **CNOT gate** with qubit 0 as control and qubit 1 as target (creates entanglement)
- Measure both qubits and observe the output

### Solution
The circuit produces the **Bell state |Φ⁺⟩ = (1/√2)(|00⟩ + |11⟩)** — a maximally entangled two-qubit state.

**Solution Procedure:**
- Start with 2 quantum bits in `|0⟩` state and 2 classical bits for storing final measurements.
- Applied Hadamard gate on first qubit.
- Applied CNOT gate with first qubit as control qubit and second qubit as target qubit.
- Measured the states of both qubits and stored it's state into respected cbits.


**Key result:** Running 1000 shots on the Aer simulator gives ~50% `|00⟩` and ~50% `|11⟩` with zero occurrences of `|01⟩` or `|10⟩`. This perfect correlation is direct evidence of quantum entanglement.

## Task 2 — Grover's Algorithm

### Problem
Given an unsorted search space of N items, find the one correct item. Classically this takes O(N) time in the worst case — you check items one by one. For large N, this gets very slow.

### What Grover's Algorithm Does
Grover's is a quantum search algorithm that solves this in O(√N) steps — a quadratic speedup over classical search. It works in two phases repeated √N times:
- **Oracle** — marks the correct answer by flipping its quantum phase
- **Diffuser** — amplifies the probability of the marked state so it dominates on measurement

### Implementation
- Search space: 2 qubits → 4 possible states (|00>, |01>, |10>, |11>)
- Target state: |11>
- Oracle: CZ gate (flips phase of |11> only)
- Iterations: 1 
### Result
Before running the algorithm, all 4 states have equal probability of 25%. After just 1 iteration of Oracle + Diffuser, the target state |11> comes up ~100% of the time and all other states drop to ~0%. This confirms that amplitude amplification successfully found the marked state.




