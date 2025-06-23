import pandas as pd
import numpy as np

#Specify filepath
gaia_stars_filepath = '23-06-25_masked_objects_list/Masking/gaiastarmaskwaves.csv'

#Load csv with pands
stars = pd.read_csv(gaia_stars_filepath)

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
    mask1 = (g > 3.5) & (g < 16)
    mask2 = g <= 3.5
    r[mask1] = (10 ** (1.3 - 0.13 * g[mask1])) 
    r[mask2] = 7 
    return r/60 

# Get masking Radii
stars['masking_radii[deg]'] = mask_radius_waves(stars['phot_g_mean_mag'])

# Filter for waves n and s. Also remove photo_g_mean mag column, and dim GAIA stars. 
waves_n = stars[(stars['dec'] >= -15) & (stars['phot_g_mean_mag'] <= 16)][['ra', 'dec', 'masking_radii[deg]']]
waves_s = stars[(stars['dec'] < -15) & (stars['phot_g_mean_mag'] <= 16)][['ra', 'dec', 'masking_radii[deg]']]

#Save down files in mangle friendly. format. 
waves_n.to_csv('starmask_waves_n.dat', sep=' ', index=False, header=False)
waves_s.to_csv('starmask_waves_s.dat', sep=' ', index=False, header=False)
