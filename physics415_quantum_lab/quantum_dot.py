import matplotlib.pyplot as plt
import numpy as np


observed_data = [465, 522.5, 579, 620, 649]

actual_data = [436, 487, 547, 589, 611]

# plt.xlim(0,5)
# plt.ylim(0,5)

plt.xlabel("Observed Data(nm)") 
plt.ylabel("Actual Spectrum(nm)") 
plt.title("Observed Flourescent Spectra vs. Actual Flourescent Spectra") 
plt.scatter(observed_data, actual_data)

# This is a very nice and compact way to do a linear regression. 
fit = np.polyfit(observed_data, actual_data, 1) 
fit_fn = np.poly1d(fit)

print fit_fn

plt.plot(observed_data, fit_fn(observed_data)) 
plt.show()
