#! usr/bin/env python3

import FEData as model
import numpy as np

reduction_d = np.array([0.00000000e+00, 
             0.00000000e+00, 
             0.00000000e+00, 
             0.00000000e+00,
             1.96070886e-05, 
             -1.12000000e-05, 
             1.33070886e-05, 
             -6.21701899e-05,
             7.07088608e-07, 
             -9.14743460e-05, 
             -9.52708861e-06, 
             -8.38210127e-05,
             -1.79270886e-05, 
             -4.93018565e-05, 
             -2.21270886e-05, 
             -7.46666667e-06,
             -4.25316456e-06, 
             -5.09701899e-05, 
             -2.20632911e-06, 
             -9.56802532e-05,
             4.30632911e-06, 
             -8.05602532e-05, 
             4.25316456e-06, 
             -4.18351899e-05])

penalty_d = np.array( [-1.17490734e-14,
             -2.32044199e-14,
              1.17490734e-14,
             -1.54696133e-14,
              1.96070886e-05,
             -1.12000000e-05,
              1.33070886e-05,
             -6.21701899e-05,
              7.07088606e-07,
             -9.14743460e-05,
             -9.52708861e-06,
             -8.38210127e-05,
             -1.79270886e-05,
             -4.93018566e-05,
             -2.21270886e-05,
             -7.46666668e-06,
             -4.25316456e-06,
             -5.09701899e-05,
             -2.20632912e-06,
             -9.56802532e-05,
              4.30632912e-06,
             -8.05602532e-05,
              4.25316456e-06,
             -4.18351899e-05])

error_d = np.abs(reduction_d - penalty_d)
mean_error_d = np.mean(error_d)

print(mean_error_d)


