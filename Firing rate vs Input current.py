import numpy as np
import matplotlib.pyplot as plt

# Input current values
currents = np.linspace(0, 5, 50)

# Store firing rates
rates = []

for I in currents:
    # Simple threshold-linear response
    rate = max(0, I - 1)
    rates.append(rate)

plt.plot(currents, rates)
plt.title("Firing Rate vs Input Current")
plt.xlabel("Input Current")
plt.ylabel("Firing Rate")
plt.show()
