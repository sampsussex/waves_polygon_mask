# Point to mangle directory
export MANGLE_DIR="/research/astro/gama/loveday/sw/mangle2.2"

#--------------------------------
# Make mask with ghosts, ngcs, extra sources. No starmask
#--------------------------------

# Combine (zero-weight) masks with (unit-weight) waves region
$MANGLE_DIR/bin/pixelize mangle_masks/waves_n_rect.ply mangle_masks/ngc_n_reg.ply mangle_masks/ghostmask_n_reg.ply temp_n_1
$MANGLE_DIR/bin/pixelize mangle_masks/waves_s_rect.ply mangle_masks/ngc_s_reg.ply mangle_masks/extra_source_s_reg.ply mangle_masks/ghostmask_s_reg.ply temp_s_1

# Snap, balkanize & unify
$MANGLE_DIR/bin/snap temp_n_1 temp_n_2
$MANGLE_DIR/bin/snap temp_s_1 temp_s_2

$MANGLE_DIR/bin/balkanize temp_n_2 temp_n_3
$MANGLE_DIR/bin/balkanize temp_s_2 temp_s_3

$MANGLE_DIR/bin/unify temp_n_3 final_masks/waves_wide_N_ghost_ngc_mask.ply
$MANGLE_DIR/bin/unify temp_s_3 final_masks/waves_wide_S_ghost_ngc_mask.ply

#Generate 1000000 randoms. 
#$MANGLE_DIR/bin/ransack -r10000000 waves_wide_N_full_mask.ply waves_wide_N_full_mask_randoms.dat
#$MANGLE_DIR/bin/ransack -r10000000 waves_wide_S_full_mask.ply waves_wide_S_full_mask_randoms.dat

#--------------------------------
# Make mask with ghosts, extra sources. No starmask or ngcs
#--------------------------------
# Combine (zero-weight) masks with (unit-weight) waves region
$MANGLE_DIR/bin/pixelize mangle_masks/waves_n_rect.ply mangle_masks/ghostmask_n_reg.ply temp_n_1
$MANGLE_DIR/bin/pixelize mangle_masks/waves_s_rect.ply mangle_masks/extra_source_s_reg.ply mangle_masks/ghostmask_s_reg.ply temp_s_1

# Snap, balkanize & unify
$MANGLE_DIR/bin/snap temp_n_1 temp_n_2
$MANGLE_DIR/bin/snap temp_s_1 temp_s_2

$MANGLE_DIR/bin/balkanize temp_n_2 temp_n_3
$MANGLE_DIR/bin/balkanize temp_s_2 temp_s_3

$MANGLE_DIR/bin/unify temp_n_3 final_masks/waves_wide_N_ghost_mask.ply
$MANGLE_DIR/bin/unify temp_s_3 final_masks/waves_wide_S_ghost_mask.ply

#--------------------------------
# Make mask with stars, extra sources. No ghosts or ngcs
#--------------------------------
# Combine (zero-weight) masks with (unit-weight) waves region
$MANGLE_DIR/bin/pixelize mangle_masks/waves_n_rect.ply mangle_masks/starmask_n_reg.ply temp_n_1
$MANGLE_DIR/bin/pixelize mangle_masks/waves_s_rect.ply mangle_masks/starmask_s_reg.ply mangle_masks/extra_source_s_reg.ply temp_s_1

# Snap, balkanize & unify
$MANGLE_DIR/bin/snap temp_n_1 temp_n_2
$MANGLE_DIR/bin/snap temp_s_1 temp_s_2

$MANGLE_DIR/bin/balkanize temp_n_2 temp_n_3
$MANGLE_DIR/bin/balkanize temp_s_2 temp_s_3

$MANGLE_DIR/bin/unify temp_n_3 final_masks/waves_wide_N_star_mask.ply
$MANGLE_DIR/bin/unify temp_s_3 final_masks/waves_wide_S_star_mask.ply

#--------------------------------
# Make mask with ngcs, extra sources. No ghosts or stars
#--------------------------------
# Combine (zero-weight) masks with (unit-weight) waves region
$MANGLE_DIR/bin/pixelize mangle_masks/waves_n_rect.ply mangle_masks/ngc_n_reg.ply temp_n_1
$MANGLE_DIR/bin/pixelize mangle_masks/waves_s_rect.ply mangle_masks/ngc_s_reg.ply mangle_masks/extra_source_s_reg.ply temp_s_1

# Snap, balkanize & unify
$MANGLE_DIR/bin/snap temp_n_1 temp_n_2
$MANGLE_DIR/bin/snap temp_s_1 temp_s_2

$MANGLE_DIR/bin/balkanize temp_n_2 temp_n_3
$MANGLE_DIR/bin/balkanize temp_s_2 temp_s_3

$MANGLE_DIR/bin/unify temp_n_3 final_masks/waves_wide_N_ngc_mask.ply
$MANGLE_DIR/bin/unify temp_s_3 final_masks/waves_wide_S_ngc_mask.ply


#--------------------------------
# Make full mask with old radius rule, no ghosts. (Previous radius rule didnt seperate out ghosts.)
#--------------------------------
# Combine (zero-weight) masks with (unit-weight) waves region
$MANGLE_DIR/bin/pixelize mangle_masks/waves_n_rect.ply mangle_masks/starmask_old_radius_rule_n_reg.ply mangle_masks/ngc_n_reg.ply temp_n_1
$MANGLE_DIR/bin/pixelize mangle_masks/waves_s_rect.ply mangle_masks/starmask_old_radius_rule_s_reg.ply mangle_masks/ngc_s_reg.ply mangle_masks/extra_source_s_reg.ply temp_s_1

# Snap, balkanize & unify
$MANGLE_DIR/bin/snap temp_n_1 temp_n_2
$MANGLE_DIR/bin/snap temp_s_1 temp_s_2

$MANGLE_DIR/bin/balkanize temp_n_2 temp_n_3
$MANGLE_DIR/bin/balkanize temp_s_2 temp_s_3

$MANGLE_DIR/bin/unify temp_n_3 final_masks/waves_wide_N_full_mask_old_radius_rule.ply
$MANGLE_DIR/bin/unify temp_s_3 final_masks/waves_wide_S_full_mask_old_radius_rule.ply

#--------------------------------
# Make mask with stars with old radius rule and extra sources. No ngcs, no ghosts. (Previous radius rule didnt seperate out ghosts.)
#--------------------------------
# Combine (zero-weight) masks with (unit-weight) waves region
$MANGLE_DIR/bin/pixelize mangle_masks/waves_n_rect.ply mangle_masks/starmask_old_radius_rule_n_reg.ply temp_n_1
$MANGLE_DIR/bin/pixelize mangle_masks/waves_s_rect.ply mangle_masks/starmask_old_radius_rule_s_reg.ply mangle_masks/extra_source_s_reg.ply temp_s_1

# Snap, balkanize & unify
$MANGLE_DIR/bin/snap temp_n_1 temp_n_2
$MANGLE_DIR/bin/snap temp_s_1 temp_s_2

$MANGLE_DIR/bin/balkanize temp_n_2 temp_n_3
$MANGLE_DIR/bin/balkanize temp_s_2 temp_s_3

$MANGLE_DIR/bin/unify temp_n_3 final_masks/waves_wide_N_star_mask_old_radius_rule.ply
$MANGLE_DIR/bin/unify temp_s_3 final_masks/waves_wide_S_star_mask_old_radius_rule.ply