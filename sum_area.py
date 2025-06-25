import pandas as pd

#Waves N
# Load the file
df_n = pd.read_csv("mangle_masks/waves_wide_N_area.dat", delim_whitespace=True)
# Convert the 'area(str)' column to float (if it's not already)
df_n['area(str)'] = df_n['area(str)'].astype(float)
# Sum all the areas
total_area_n = df_n['area(str)'].sum()

print(f"waves wide N total area: {total_area_n}")

#Waves S
# Load the file
df_s = pd.read_csv("mangle_masks/waves_wide_S_area.dat", delim_whitespace=True)
# Convert the 'area(str)' column to float (if it's not already)
df_s['area(str)'] = df_s['area(str)'].astype(float)
# Sum all the areas
total_area_s = df_s['area(str)'].sum()

print(f"waves wide S total area: {total_area_s}")


# Save the result to a text file
with open("waves_wide_total_area_full_mask.txt", "w") as f:
    f.write(f"waves wide N total area: {total_area_n}\nwaves wide S total area: {total_area_s}\n")