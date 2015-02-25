import eis_functions

import matplotlib.pyplot as plt
import numpy as np


#generate data for a given circuit
circuit = 'Rel+Rct/Qdl'
prmfilepath = './data/test.PrmInit'
savefilepath = './data/Generated_Data.data'
f_limits=(1e-3, 1e9)

eis_functions.generate_calculated_values(circuit=circuit,
                                         prmfilepath=prmfilepath,
                                         savefilepath=savefilepath,
                                         f_limits=f_limits,
                                         points_per_decade=10,
                                         sigma=5.0)

f, Re, Im = np.loadtxt(savefilepath, usecols=(0,1,2), delimiter='\t', unpack=True)

plt.plot(Re, Im, marker='o')
plt.gca().set_aspect('equal')
ymin, ymax = plt.ylim()
plt.ylim(ymax, ymin)

plt.show()


    
datafilepath = savefilepath
    
eis_functions.run_fit(circuit, datafilepath, prmfilepath,
        nb_run_per_process=20, nb_minimization=50,
        init_types=('random','random','random'), f_limits=f_limits, immittance_type = 'Z',
        root = './data/fit_results/', alloy='test', alloy_id='1',
        random_loops=200, process_id=1, simplified=False,
        maxiter_per_parameter=200, maxfun_per_parameter=200, xtol=1e-30, ftol=1e-30,
        full_output=True, retall=False, disp=False, fmin_callback=None, callback=eis_functions._callback_fit)

    

    