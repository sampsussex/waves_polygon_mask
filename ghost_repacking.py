import pandas as pd
import numpy as np

#set filepath
ghosts_filepath = '23-06-25_masked_objects_list/Masking/GhostLocations_v0.csv'

#Load csv with pands
ghosts = pd.read_csv(ghosts_filepath)

def mask_radius_waves(g):
    """
    Calculate r[deg] based on the given formula.

    Parameters:
        g (float or array-like): Input magnitude.

    Returns:
        numpy.ndarray: Calculated r[deg].
    """
    g = np.asarray(g)  # Ensure g is a NumPy array
    r = np.zeros_like(g, dtype=float)
    mask1 = g > 6
    mask2 = (g > 2.5) & (g <= 6)
    mask3 = (g <= 2.5)
    r[mask1] = 3.39
    r[mask2] = 10**(1.07-0.09*g[mask2])
    r[mask3] = 7
    return r/60 

# Get masking Radii
ghosts['masking_radii[deg]'] = mask_radius_waves(ghosts['mag'])

# Filter for waves n and s. Also remove photo_g_mean mag column, and dim GAIA stars. 
waves_n = ghosts[(ghosts['dec'] >= -15) & (ghosts['mag'] <= 16)][['ra', 'dec', 'masking_radii[deg]']]
waves_s = ghosts[(ghosts['dec'] < -15) & (ghosts['mag'] <= 16)][['ra', 'dec', 'masking_radii[deg]']]

#Save down files in mangle friendly. format. 
waves_n.to_csv('ghostmask_waves_n.dat', sep=' ', index=False, header=False)
waves_s.to_csv('ghostmask_waves_s.dat', sep=' ', index=False, header=False)