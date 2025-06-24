# Mangle code to generate graphics format files from mangle polygon files. 
# This code won't make plots directly. 

# Point to mangle directory
export MANGLE_DIR="/research/astro/gama/loveday/sw/mangle2.2"


#Waves N
$MANGLE_DIR/bin/poly2poly -og12 waves_wide_N_full_mask.ply plots/waves_wide_N_full_mask_graphics.dat
$MANGLE_DIR/bin/poly2poly -og12 mangle_masks/starmask_n_reg.ply plots/starmask_n_reg_graphics.dat
$MANGLE_DIR/bin/poly2poly -og12 mangle_masks/ghostmask_n_reg.ply plots/ghostmask_n_reg_graphics.dat
$MANGLE_DIR/bin/poly2poly -og12 mangle_masks/ngc_n_reg.ply plots/ngc_n_reg_graphics.dat


#Waves S
$MANGLE_DIR/bin/poly2poly -og12 waves_wide_S_full_mask.ply plots/waves_wide_S_full_mask_graphics.dat
$MANGLE_DIR/bin/poly2poly -og12 mangle_masks/starmask_s_reg.ply plots/starmask_s_reg_graphics.dat
$MANGLE_DIR/bin/poly2poly -og12 mangle_masks/ghostmask_s_reg.ply plots/ghostmask_s_reg_graphics.dat
$MANGLE_DIR/bin/poly2poly -og12 mangle_masks/ngc_s_reg.ply plots/ngc_s_reg_graphics.dat
$MANGLE_DIR/bin/poly2poly -og12 mangle_masks/extra_source_s_reg.ply plots/extra_source_s_reg_graphics.dat
