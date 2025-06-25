# Mangle code for applying starmask to waves n and s regions

# Point to mangle directory
export MANGLE_DIR="/research/astro/gama/loveday/sw/mangle2.2"

echo 0 > zero #zero referenced in weighting later on.

# Create mangle masks, zero weighted, for gaia stars in waves n and s
$MANGLE_DIR/bin/weight -ic1 -zzero input_data/starmask_waves_n.dat mangle_masks/starmask_n_reg.ply
$MANGLE_DIR/bin/weight -ic1 -zzero input_data/starmask_waves_s.dat mangle_masks/starmask_s_reg.ply

# Create mangle masks, zero weighted, for gaia stars in waves n and s, using the old rule for radii from GAMA dr4
$MANGLE_DIR/bin/weight -ic1 -zzero input_data/starmask_waves_n_old_radius_rule.dat mangle_masks/starmask_old_radius_rule_n_reg.ply
$MANGLE_DIR/bin/weight -ic1 -zzero input_data/starmask_waves_s_old_radius_rule.dat mangle_masks/starmask_old_radius_rule_s_reg.ply

# Create mangle masks, zero weighted, for the extra sources in waves s. This is the large GC and star. 

$MANGLE_DIR/bin/weight -ic1 -zzero input_data/extra_waves_s_sources.dat mangle_masks/extra_source_s_reg.ply

# Create mangle masks, zero weighted, for ghosts in waves n and s
$MANGLE_DIR/bin/weight -ic1 -zzero input_data/ghostmask_waves_n.dat mangle_masks/ghostmask_n_reg.ply
$MANGLE_DIR/bin/weight -ic1 -zzero input_data/ghostmask_waves_s.dat mangle_masks/ghostmask_s_reg.ply



# Create mangle masks, zero weighted, for ngcs in waves and s
$MANGLE_DIR/bin/weight -iv -zzero input_data/ngc_n.dat mangle_masks/ngc_n_reg.ply
$MANGLE_DIR/bin/weight -iv -zzero input_data/ngc_s.dat mangle_masks/ngc_s_reg.ply

