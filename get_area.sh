# Point to mangle directory
export MANGLE_DIR="/research/astro/gama/loveday/sw/mangle2.2"

#Get area of each polygon.
$MANGLE_DIR/bin/poly2poly -oa waves_wide_N_full_mask.ply mangle_masks/waves_wide_N_area.dat
$MANGLE_DIR/bin/poly2poly -oa waves_wide_S_full_mask.ply mangle_masks/waves_wide_S_area.dat


#$MANGLE_DIR/bin/poly2poly -oa final_masks/waves_wide_N_full_mask_old_radius_rule.ply mangle_masks/waves_wide_N_area.dat
#$MANGLE_DIR/bin/poly2poly -oa final_masks/waves_wide_S_full_mask_old_radius_rule.ply mangle_masks/waves_wide_S_area.dat
