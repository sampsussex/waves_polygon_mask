# Point to mangle directory
export MANGLE_DIR="/research/astro/gama/loveday/sw/mangle2.2"


# Combine (zero-weight) NGC masks with (unit-weight) waves region
$MANGLE_DIR/bin/pixelize mangle_masks/waves_n_rect.ply mangle_masks/starmask_n_reg.ply mangle_masks/ngc_n_reg.ply temp_n_1
$MANGLE_DIR/bin/pixelize mangle_masks/waves_s_rect.ply mangle_masks/starmask_s_reg.ply mangle_masks/ngc_s_reg.ply mangle_masks/extra_source_s_reg.ply temp_s_1

# Snap, balkanize & unify
$MANGLE_DIR/bin/snap temp_n_1 temp_n_2
$MANGLE_DIR/bin/snap temp_s_1 temp_s_2

$MANGLE_DIR/bin/balkanize temp_n_2 temp_n_3
$MANGLE_DIR/bin/balkanize temp_s_2 temp_s_3

$MANGLE_DIR/bin/unify temp_n_3 waves_wide_N_full_mask.ply
$MANGLE_DIR/bin/unify temp_s_3 waves_wide_S_full_mask.ply

#Generate 1000000 randoms. 
#$MANGLE_DIR/bin/ransack -r10000000 waves_wide_N_full_mask.ply waves_wide_N_full_mask_randoms.dat
#$MANGLE_DIR/bin/ransack -r10000000 waves_wide_S_full_mask.ply waves_wide_S_full_mask_randoms.dat