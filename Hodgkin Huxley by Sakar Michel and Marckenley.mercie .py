This the code mark and I work on so far.
#I = is the total membrane current density (inward current positive);
#C_M is the membrane capcity per unit area
#D_V  the derivative of the displacement of the membrane potential.
#D_T the derivative of time.
#I_i is the ionic current density (inward current positive).
#This equation gives the value for the membrane capcity.

I = C_M(D_V/D_T) + I_i


#I_NA is the sodium ions.
#I_k is the potssium ions.
#I_l is the other ions.
I_i = I_NA + I_k + I_l

#g_NA is sodium ionic condantance.
#E is the membrane potential
#E_NA is the equilibrium potential for sodium.
#g_K is the equilibrium potential for potassium
#E_k is the equilibrum potential for potassium.
#g_L is the lekage ionic condantance.
#E_l is the potential at whih the 'leakage current' due to chlorde and other ions is zero.
I_NA = g_NA(E-E_NA)
I_k = g_K(E-E_K)
I_l = g_L(E-E_l)


#V is the resting potential.
#V_NA is the resting potential for sodium.
#V_K is the resting potential for potassium.
#V_l is the resting potential for lekage.
I_NA = g_NA(V-V_NA)
I_K =g_K(V-V_K)
I_L = g_l(V-V_l)

#E_r is the absoulte value for the resting potential V, V_NA, V_K and V_l                                                                                                                                                                                                                                                                                     
V = E - E_r
V_NA = E_NA - E_r
V_K = E_K - E_r
V_l = E_l - E_r

