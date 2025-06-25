import pandas as pd

# Waves N
df_n = pd.read_csv("mangle_masks/waves_wide_N_area.dat", delim_whitespace=True, skiprows=1, header=None)
df_n[0] = df_n[0].astype(float)
total_area_n = df_n[0].sum()
print(f"waves wide N total area: {total_area_n}")

# Waves S
df_s = pd.read_csv("mangle_masks/waves_wide_S_area.dat", delim_whitespace=True, skiprows=1, header=None)
df_s[0] = df_s[0].astype(float)
total_area_s = df_s[0].sum()
print(f"waves wide S total area: {total_area_s}")

# Combined total
total_area_combined = total_area_n + total_area_s
print(f"waves wide combined total area: {total_area_combined}")

# Save all results to a text file
with open("waves_wide_total_area_full_mask.txt", "w") as f:
    f.write(f"waves wide N total area: {total_area_n}\n")
    f.write(f"waves wide S total area: {total_area_s}\n")
    f.write(f"waves wide combined total area: {total_area_combined}\n")
