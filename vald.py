
class Hodgkin_Huxley_Model:

    def __init__(self, G_NA, V_m, E_NA, G_K,E_K, G_lk, V_lk):
        """ (Hodgkin_Huxley_Model, float, float, float, float, float, float) -> NoneType

        set up instructions
        1. I'm assuming you are familiar on how to run this program.
        2. I provide instruction just in case.
        3. import vald
        
        
        The function initializes the variables require for the first differential eqaution
        on page 48, Chapter 3: The Hodgkin-Huxley Model.

        >>> differentialEquation3_9a = vald.Hodgkin_Huxley_Model(
            120,1,55,36,-72,0.3,-49.87)

        >>>differentialEquation3_9a.G_NA
        '120'

        >>>differentialEquation3_9a.V_m
        '1'

        >>>differentialEquation3_9a.E_NA
        '55'

        >>>differentialEquation3_9a.G_K
        '36'

        >>>differentialEquation3_9a.E_K
        '-72'

        >>>differentialEquation3_9a.G_lk
        '0.3'

        >>>differentialEquation3_9a.V_lk
        '-49.387'
    
        """

        #G_NA is the Sodium condutance.
        self.G_NA = G_NA

        #V_m is the membrane potential.
        self.V_m = V_m

        #E_NA is the equilibrium potential for sodium
        self.E_NA = E_NA

        #G_K is the Potassium condutance. 
        self.G_K = G_K

        #E_k is the equilibrium potential for Potassium.
        self.E_K = E_K

        #G_lk is the leakage conductance.
        self.G_lk = G_lk

        #V_lk is the leakage voltage.
        self.V_lk = V_lk



   

    def setDifferentialEquation3_9a(self):
        """ (Hodgkin_Huxley_Model) -> float

            Return the value of the differential equation 3.9a

            >>>differentialEquation3_9a_variable.CdVM_divideBy_dt_variable_equation(
            120,1,55,36,-72,0.3,-49.87)

            >>>differentialEquation3_9a_variable.setDifferentialEquation3_9a()
            '3801.13'
        """
        return -1 *  self.G_NA * (self.V_m - self.E_NA) -1 * self.G_K * (self.V_m - self.E_K) -1 * (self.V_m - self.V_lk)  


    def setDifferentialEquation3_9b_variable(self):
        """ (Hodgkin_Huxley_Model) -> NoneType

       This function initialize the variable require for the differential equation
       on page 48, Chapter 3: The Hodgkin-Huxley Model 3.9b
        
        

        >>>differentialEquation3_9b = vald.Hodgkin_Huxley_Model(
           120,1,55,36,-72,0.3,-49.87)

        >>>differentialEquation3_9b.setDifferentialEquation3_9b_variable()

        >>>differentialEquation3_9b.V_r
        '2'

        >>>differentialEquation3_9b.u
        '-1'
        >>>differentialEquation3_9b.alpha_n
        '1.099999999999999'

        >>>differentialEquation3_9b.beta_n
        '0.0015625'

        """

        #V_r is the resting potential
        self.V_r = 2

        #u = V_m - V_r
        self.u = self.V_m - self.V_r

        #n is the probability the potassium channel is open.
        self.n = 1

        #alpha is the rate at which closed gates transition to an open state.
        self.alpha_n = 0.01 * (10 - self.u) / (( 1 - 0.1 *self.u)-1)

        #beta is the rate at which open gates transition to the closed state. 
        self.beta_n = 0.125 * (-1 * self.u / 80)

    
    def setDifferentialEquation3_9b(self):
        """ (Hodgkin_Huxley_Model) -> float

            Return the value of the differential equation 3.9b

            >>>differentialEquation3_9b = vald.Hodgkin_Huxley_Model(
            120,1,55,36,-72,0.3,-49.87)

            >>>differentialEquation3_9b.setDifferentialEquation3_9b_variable()

            >>>differentialEquation3_9b.setDifferentialEquation3_9b()
            '-0.0015624999999999112'
        """
        return -1 * (self.alpha_n + self.beta_n) * self.n + self.alpha_n

    def setDifferentialEquation3_9c_variable(self):
        """ (Hodgkin_Huxley_Model) -> NoneType

       This function initialize the variable require for the differential equation
       on page 48, Chapter 3: The Hodgkin-Huxley Model 3.9c
        
        

        >>>differentialEquation3_9c = vald.Hodgkin_Huxley_Model(
           120,1,55,36,-72,0.3,-49.87)

        >>>differentialEquation3_9c.setDifferentialEquation3_9b_variable()

        >>>differentialEquation3_9c.setDifferentialEquation3_9c_variable()

        >>>differentialEquation3_9c.V_r
        '2'

        >>>differentialEquation3_9c.u
        '-1'

        >>>differentialEquation3_9c.m
        '1'
        
        >>>differentialEquation3_9c.alpha_m
        '1.625'

        >>>differentialEquation3_9c.beta_m
        '0.2222222222222222'

        """

        
        self.V_r = 2
        self.u = self.V_m - self.V_r

        #m - is the open probability for the activation gate of the sodium channel
        self.m = 1

        self.alpha_m = 0.1 * (25 - self.u) / (( 2.5 - 0.1 *self.u)-1)

        self.beta_m = 4 * (-1 * self.u / 18)


    def setDifferentialEquation3_9c(self):
        """ (Hodgkin_Huxley_Model) -> float

            Return the value of the differential equation 3.9c

        >>>differentialEquation3_9c = vald.Hodgkin_Huxley_Model(
           120,1,55,36,-72,0.3,-49.87)

        >>>differentialEquation3_9c.setDifferentialEquation3_9b_variable()

        >>>differentialEquation3_9c.setDifferentialEquation3_9c_variable()

        >>>differentialEquation3_9c.setDifferentialEquation3_9c()
        '-0.22222222222222232'
        """
        return -1 * (self.alpha_m + self.beta_m) * self.m + self.alpha_m






    def setDifferentialEquation3_9d_variable(self):
        """ (Hodgkin_Huxley_Model) -> NoneType

        This function initialize the variable require for the differential equation
        on page 48, Chapter 3: The Hodgkin-Huxley Model 3.9d
        
        

        >>>differentialEquation3_9d = vald.Hodgkin_Huxley_Model(
           120,1,55,36,-72,0.3,-49.87)

        >>>differentialEquation3_9d.setDifferentialEquation3_9b_variable()

        >>>differentialEquation3_9d.setDifferentialEquation3_9d_variable()

        >>>differentialEquation3_9d.V_r
        '2'

        >>>differentialEquation3_9d.u
        '-1'

        >>>differentialEquation3_9d.h
        '1'
        
        >>>differentialEquation3_9d.alpha_h
        '0.0035000000000000005'

        >>>differentialEquation3_9d.beta_h
        '0.24390243902439027'

        """

        
        self.V_r = 2
        self.u = self.V_m - self.V_r

        #h is the open probability for the inactivation gate
        self.h = 1

        self.alpha_h = 0.07 * (- self.u / 20)
        self.beta_h = 1 / (3 - 0.1 * self.u + 1)


    def setDifferentialEquation3_9d(self):
        """ (Hodgkin_Huxley_Model) -> float

            Return the value of the differential equation 3.9d

         >>>differentialEquation3_9d = vald.Hodgkin_Huxley_Model(
           120,1,55,36,-72,0.3,-49.87)

        >>>differentialEquation3_9d.setDifferentialEquation3_9b_variable()

        >>>differentialEquation3_9d.setDifferentialEquation3_9d_variable()

        >>>differentialEquation3_9d.setDifferentialEquation3_9d()
        '-0.24390243902439027'
        """
        return -1 * (self.alpha_h + self.beta_h) * self.h + self.alpha_h  

    
        
        
        

    
