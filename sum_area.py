import pandas as pd
import numpy as np

# Waves N
df_n = pd.read_csv("mangle_masks/waves_wide_N_area.dat", delim_whitespace=True, skiprows=2, header=None)
df_n[0] = df_n[0].astype(float)
total_area_n = df_n[0].sum()
# convert to sq deg
total_area_n = total_area_n*180**2/(np.pi**2)
print(f"waves wide N total area: {total_area_n} sq deg")

# Waves S
df_s = pd.read_csv("mangle_masks/waves_wide_S_area.dat", delim_whitespace=True, skiprows=2, header=None)
df_s[0] = df_s[0].astype(float)
total_area_s = df_s[0].sum()
# convert to sq deg
total_area_s = total_area_s*180**2/(np.pi**2)
print(f"waves wide S total area: {total_area_s} sq deg")

# Combined total
total_area_combined = total_area_n + total_area_s
print(f"waves wide combined total area: {total_area_combined} sq deg")

# Save all results to a text file
with open("waves_wide_total_area_full_mask.txt", "w") as f:
    f.write(f"waves wide N total area: {total_area_n} sq deg\n")
    f.write(f"waves wide S total area: {total_area_s} sq deg\n")
    f.write(f"waves wide combined total area: {total_area_combined} sq deg\n")
