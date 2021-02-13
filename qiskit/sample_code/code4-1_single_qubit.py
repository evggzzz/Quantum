import qiskit
from qiskit import QuantumRegister
from qiskit import ClassicalRegister
from qiskit import Aer
from qiskit import execute
# 1 量子ビットを定義する
q1 = QuantumRegister(1)
# 1 古典ビットを定義する
c1 = ClassicalRegister(1)
# 結果の個数をカウントする
def get_result(qc, shots=1):
    simulator = Aer.get_backend('qasm_simulator')
    return execute(qc, simulator, shots=shots).result().get_counts(qc)
# 行列を表示する
def get_unitary(qc):
    simulator = Aer.get_backend('unitary_simulator') 
    return execute(qc, simulator).result().get_unitary(qc)