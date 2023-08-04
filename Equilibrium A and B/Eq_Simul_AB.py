# Equilibrium script
# by Carlos Neves, UFPA

import numpy as np
import matplotlib.pyplot as plt

# Parameters

# velocity constants
k_A = 0.0001 # M/s
k_B = 0.01 # M/s

# initial concentations
C_A_i = 0.0 # M=mol/L
C_B_i = 1.0 # M=mol/L

# final time in ms
t_ms_f = 5000 # ms

# Processing
# concentrations at time t
C_A_t = np.array([]) 
C_B_t = np.array([])

# start array with initial concentration
i = 0 # index
C_A_t = np.append(C_A_t, C_A_i) # M=mol/L
C_B_t = np.append(C_B_t, C_B_i) # M=mol/L

# time interval of 1ms
t_ms = np.arange(0, t_ms_f, 1)

for t in t_ms[1:]:
	i = i + 1

	C_A_t_before = C_A_t[i-1]
	C_B_t_before = C_B_t[i-1]

	# C_A_t = C_A_t-1 + C_A_t_consumed + C_A_t_produced
	C_A_t = np.append(C_A_t, C_A_t_before + (-k_A * C_A_t_before) + (k_B * C_B_t_before))
	
	# C_B_t = C_B_t-1 + C_B_t_consumed + C_B_t_produced
	C_B_t = np.append(C_B_t , C_B_t_before + (-k_B * C_B_t_before) + (k_A * C_A_t_before))

plt.plot(t_ms, C_A_t, t_ms, C_B_t)
plt.legend(["[A]", "[B]"])
plt.suptitle('Equilibrium A=B')
plt.title('kB=0.01M/s; kA=0.0001M/s')
plt.xlabel('t / ms')
plt.ylabel('concentration / M')
plt.grid(True)
plt.savefig('Equilibrium_A_0.0M_kA_0.0001Mpersec_B_1.0M_kB_0.01Mpersec.png')
plt.show()
