from qiskit_basic_kit import *
#=====control not gate======================
# 1 量子ビットを定義する
q1 = QuantumRegister(2)
# 1 古典ビットを定義する
c1 = ClassicalRegister(2)
# 量子回路を定義する
qc1 = QuantumCircuit(q1,c1)

qc1.h(0)
qc1.h(1)
qc1.cx(0,1)

qc1.measure(q1,c1)

#量子回路表示
print(qc1)
print("測定結果:",get_result(qc1,1000))

#=====phase kickbask=========================
# 1 量子ビットを定義する
q2 = QuantumRegister(2)
# 1 古典ビットを定義する
c2 = ClassicalRegister(2)
# 量子回路を定義する
qc2 = QuantumCircuit(q2,c2)

qc2.h(0)
qc2.x(1)
qc2.h(1)
qc2.cx(0,1)
qc2.h(0)
qc2.h(1)

qc2.measure(q2,c2)

#量子回路表示
print(qc2)
print("測定結果:",get_result(qc2,1000))
