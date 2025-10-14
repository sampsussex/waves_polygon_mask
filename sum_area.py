import pandas as pd
import numpy as np
import os

# -----------------------------------------------------
# Function to read and sum areas from a .dat file
# -----------------------------------------------------
def read_area_file(filename):
    df = pd.read_csv(filename, delim_whitespace=True, skiprows=2, header=None)
    df[0] = df[0].astype(float)
    total_area = df[0].sum()
    # convert steradians → square degrees
    total_area_sqdeg = total_area * (180 / np.pi) ** 2
    return total_area_sqdeg

# -----------------------------------------------------
# Define the masks and their corresponding filenames
# -----------------------------------------------------
masks = {
    "full_mask": {
        "N": "mangle_masks/waves_wide_N_area.dat",
        "S": "mangle_masks/waves_wide_S_area.dat"
    },
    "star_mask": {
        "N": "mangle_masks/waves_wide_N_star_mask_area.dat",
        "S": "mangle_masks/waves_wide_S_star_mask_area.dat"
    },
    "star_ghost_mask": {
        "N": "mangle_masks/waves_wide_N_star_ghost_mask_area.dat",
        "S": "mangle_masks/waves_wide_S_star_ghost_mask_area.dat"
    },
    "star_ngc+_mask": {
        "N": "mangle_masks/waves_wide_N_star_ngc+_mask_area.dat",
        "S": "mangle_masks/waves_wide_S_star_ngc+_mask_area.dat"
    }
}

# -----------------------------------------------------
# Compute total areas and store results
# -----------------------------------------------------
results = []

for mask_name, files in masks.items():
    entry = {"Mask Type": mask_name}

    if os.path.exists(files["N"]):
        area_n = read_area_file(files["N"])
    else:
        area_n = np.nan
        print(f"Warning Missing file: {files['N']}")

    if os.path.exists(files["S"]):
        area_s = read_area_file(files["S"])
    else:
        area_s = np.nan
        print(f"Warning Missing file: {files['S']}")

    entry["WAVESwide N (sq deg)"] = area_n
    entry["WAVESwide S (sq deg)"] = area_s
    entry["WAVESwide N+S (sq deg)"] = area_n + area_s if not np.isnan(area_n + area_s) else np.nan

    results.append(entry)

# -----------------------------------------------------
# Save to CSV
# -----------------------------------------------------
df_out = pd.DataFrame(results)
df_out.to_csv("waves_wide_total_areas.csv", index=False)

print("✅ Saved results to 'waves_wide_total_areas.csv'")
print(df_out)
