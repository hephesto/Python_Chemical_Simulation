################################################
# Reaction NOBr NO Br2
# by Carlos Neves
################################################
# Reaction:
#
# 2NOBr(g) -> 2NO(g) + 1Br2(g)
#
# k(NO) = 0.16 mmol*dm-3*s-1
# (1/2)*v(NOBr) = (1/2)*v(NO) = (1/1)*v(Br2)
#
################################################
# Modules

import numpy as np
import matplotlib.pyplot as plt

################################################
# Parameters

# velocity constants
k_NO = 0.16*10**-3 # mol*dm-3*s-1
k_NOBr = 0.16*10**-6 # mol*dm-3*s-1

# initial concentations
C_NOBr_i = 0.001 # mol*dm-3
C_NO_i = 1.0 # mol*dm-3
C_Br2_i = 1.0 # mol*dm-3

# final time in ms
t_s_f = 50000 # s 833,333min = 13,9h

################################################
# Processing

# concentrations at time t
C_NOBr_t = np.array([]) 
C_NO_t = np.array([])
C_Br2_t = np.array([])

# start array with initial concentration
i = 0 # index
C_NOBr_t = np.append(C_NOBr_t, C_NOBr_i) # M=mol/L
C_NO_t = np.append(C_NO_t, C_NO_i) # M=mol/L
C_Br2_t = np.append(C_Br2_t, C_Br2_i) # M=mol/L

# time interval of 1s
step = 10
t_s = np.arange(0, t_s_f, step)

for t in t_s[1:]:
	i = i + 1

	C_NOBr_t_before = C_NOBr_t[i-1]
	C_NO_t_before = C_NO_t[i-1]
	C_Br2_t_before = C_Br2_t[i-1]

	# C_NOBr_t = C_NOBr_t-1 - C_NOBr_t_consumed + C_NOBr_t_produced
	C_NOBr_t = np.append(C_NOBr_t, (C_NOBr_t_before -(1/1)*k_NO*C_NOBr_t_before*step +(1/1)*k_NOBr*C_NO_t_before*step))
	
	# C_NO_t = C_NO_t-1 + C_NO_t_produced - C_NO_t_consumed
	C_NO_t = np.append(C_NO_t , (C_NO_t_before + (1/1)*k_NO*C_NOBr_t_before*step -(1/1)*k_NOBr*C_NO_t_before*step))

	# C_Br2_t = C_Br2_t-1 + C_Br2_t_produced - C_Br2_t_consumed
	C_Br2_t = np.append(C_Br2_t , (C_Br2_t_before + (1/2)*k_NO*C_NOBr_t_before*step - (1/2)*k_NOBr*C_Br2_t_before*step))

# ploting
plt.plot(t_s, C_NOBr_t, t_s, C_NO_t, t_s, C_Br2_t)
plt.legend(["[NOBr]", "[NO]", "[Br2]"])
plt.suptitle('2NOBr(g) = 2NO(g) + 1Br2(g)')
plt.title('k_NO=0.16 mmol*dm-3*s-1')
plt.xlabel('t / s')
plt.ylabel('concentration / mol*dm-3')
plt.grid(True)
plt.savefig('Reaction_NOBr_0.001_NO_1.0_Br2_1.0.png')
plt.show()
