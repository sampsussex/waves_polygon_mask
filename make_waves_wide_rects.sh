# Construct mangle-compatible Waves wide mask.    

# Define waves N region as 1 rectangles in waves_n_rect.dat
# Convert to polygon format (default weight=1)
echo "# WavesWide North 
# ra_min ra_max dec_min dec_max 
157.25 225.0 -3.95 3.95" > input_data/waves_n_rect.dat


# Define waves S region as 1 rectangles in waves_n_rect.dat
# Convert to polygon format (default weight=1)
echo "# WavesWide South 
# ra_min ra_max dec_min dec_max 
330.0 51.6 -35.6 -27.0" > input_data/waves_s_rect.dat

# Point to mangle directory
export MANGLE_DIR="/research/astro/gama/loveday/sw/mangle2.2"

# Create waves N region ply file
$MANGLE_DIR/bin/poly2poly -ir1 input_data/waves_s_rect.dat mangle_masks/waves_s_rect.ply
# Create waves N region ply file
$MANGLE_DIR/bin/poly2poly -ir1 input_data/waves_n_rect.dat mangle_masks/waves_n_rect.ply
