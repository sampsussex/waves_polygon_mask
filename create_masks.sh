# Mangle code for applying starmask to waves n and s regions

# Point to mangle directory
export MANGLE_DIR="/research/astro/gama/loveday/sw/mangle2.2"

echo 0 > zero #zero referenced in weighting later on.

# Create mangle masks, zero weighted, for gaia stars in waves n and s
$MANGLE_DIR/bin/weight -ic1 -zzero starmask_waves_n.dat mangle_masks/starmask_n_reg.ply
$MANGLE_DIR/bin/weight -ic1 -zzero starmask_waves_s.dat mangle_masks/starmask_s_reg.ply

# Create mangle masks, zero weighted, for the extra sources in waves s. This is the large GC and star. 

$MANGLE_DIR/bin/weight -ic1 -zzero extra_waves_s_sources.dat mangle_masks/extra_source_s_reg.ply

# Create mangle masks, zero weighted, for ngcs in waves and s
$MANGLE_DIR/bin/weight -iv -zzero ngcs_n.dat mangle_masks/ngc_n_reg.ply
$MANGLE_DIR/bin/weight -iv -zzero ngcs_s.dat mangle_masks/ngc_s_reg.ply

