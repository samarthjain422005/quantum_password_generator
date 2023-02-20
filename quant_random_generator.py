'''
author: aakash k singh
date created: 6 Nov
purpose: for QCG hackathon

qiskit library required to be installed
'''

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, BasicAer, execute

def bin_to_dec(input_str):
    # will convert the string input given to decimal integer

    len_str = len(input_str)
    dec_no = 0
    for i in range(len_str):
        bin_digit = int(input_str[len_str - i - 1]) * (2**i)
        dec_no += bin_digit

    return dec_no

def quantum_random():
    #will generate a list with string of bits at 0th index
    n=7  #because we want ascii values so 0-127 range of number would work
    qr = QuantumRegister(n, 'q_reg')
    cr = ClassicalRegister(n, 'c_reg')
    qc = QuantumCircuit(qr, cr)

    for i in range(n):
        qc.h(qr[i])  #applying hadamard gate to each qubit
        
    qc.measure(qr,cr)
    backend = BasicAer.get_backend('statevector_simulator')
    job = execute(qc, backend, shots=1, memory = True)
    generated_list = job.result().get_memory()
    random_int = bin_to_dec(generated_list[0])
    return random_int

def generate(n):  # main function to generate random password
    # n is length of password
   
    passw = ''
    while len(passw) < n:

        random_int = quantum_random()
        if random_int in (list(range(63,91)) + list(range(97,123)) + list(range(35,39))):
            passw += chr(random_int)
            
    return passw
