# Point to mangle directory
export MANGLE_DIR="/research/astro/gama/loveday/sw/mangle2.2"

#Get area of each polygon. Full mask.
$MANGLE_DIR/bin/poly2poly -oa waves_wide_N_full_mask.ply mangle_masks/waves_wide_N_area.dat
$MANGLE_DIR/bin/poly2poly -oa waves_wide_S_full_mask.ply mangle_masks/waves_wide_S_area.dat

# Get area of just star mask
$MANGLE_DIR/bin/poly2poly -oa final_masks/waves_wide_N_star_mask.ply mangle_masks/waves_wide_N_star_mask_area.dat
$MANGLE_DIR/bin/poly2poly -oa final_masks/waves_wide_S_star_mask.ply mangle_masks/waves_wide_S_star_mask_area.dat

# Get area of star and ghost mask
$MANGLE_DIR/bin/poly2poly -oa final_masks/waves_wide_N_star_ghost_mask.ply mangle_masks/waves_wide_N_star_ghost_mask_area.dat
$MANGLE_DIR/bin/poly2poly -oa final_masks/waves_wide_S_star_ghost_mask.ply mangle_masks/waves_wide_S_star_ghost_mask_area.dat

# Get area of star and ngc+ masks
$MANGLE_DIR/bin/poly2poly -oa final_masks/waves_wide_N_star_ngc+_mask.ply mangle_masks/waves_wide_N_star_ngc+_mask_area.dat
$MANGLE_DIR/bin/poly2poly -oa final_masks/waves_wide_S_star_ngc+_mask.ply mangle_masks/waves_wide_S_star_ngc+_mask_area.dat
