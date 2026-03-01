import numpy as np
import matplotlib.pyplot as plt
print("Script is running")
# Time axis
t = np.linspace(-1, 1, 1000)

# Sine wave
frequency = 5
sine_wave = np.sin(2 * np.pi * frequency * t)

# Unit step
unit_step = np.where(t >= 0, 1, 0)

# Plot
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, sine_wave)
plt.title("Sine Wave (5 Hz)")
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, unit_step)
plt.title("Unit Step Function")
plt.grid()

plt.tight_layout()

plt.savefig("signals_output.png")   # Save plot as image
print("Plot saved as signals_output.png")