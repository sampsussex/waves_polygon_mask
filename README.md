# waves_polygon_mask
A repo for mangle code for generating waves masks.
This code will generate polygon masks (as defined in the mangle documentation) for the waves wide regions. This masks may then be used for generating random catalogoes of sources in the waves regions. The workflow outlined is; 1) Put input data in a format that mangle expects using python scripts. 2) Run mangle commands on the reformatted input data to generate masks and then 4) combine them together. An optional stage 4) is to run a single command on a mask to generate randoms and an option stage 5) is to run a different command (and accompaning python script) to calculate the area of the survey windows. 

This code will generate mangle masks for the waves regions. You must have mangle installed from: https://space.mit.edu/~molly/mangle/. Please note mangle currently does not run on apple silicon.

The python scripts have already been run, but if needed you can rerun them. If you do, some manual edits are required for the ngc dat files. These are detailed below. These scripts output the repacked star/ngc/ghost masks in a mangle friendly format. The outputs are the '*.dat' files. You must unzip the large file 23-06-25_masked_objects_list/Masking/gaiastarmaskwaves.csv.zip before running the python code for generating the starmask dat file. 

To run the code, run the shell scripts. They must be run in order; make_waves_wide_rects.sh, make_masks.sh, combine_masks_main.sh. combine_mask_permutations.sh can be run to generate different permuations of the mask, swapping in or out stars, ngcs etc. The main mask will be saved as waves_wide_(N/S)_full_mask.ply in the home directory here, and the permuations will be saved in final_masks/.

To alter the compoisition of the mask, change the pixelize command in combine_masks.sh. In this command all the masks are added to the rectangle window. Remove/add as you wish. The default is the 'full mask', i.e. Window-starmask-ghostmask-ngcmask(-extramask for waves-S).

The 'old_radius_rule' files use the older rules for starmasking, that originate in GAMA dr4 (Bellstedt+2020). There are no seperate ghostmasks for this older version. 

Additionally, some of the other NGC masks have an 'r' infront of them in the dat files. This is because for mangle vertices must be supplied in a counterclockwise fashion. These vertices are given clockwise, and so mangle demands an r be placed infront. Mangle will raise this as an error if you run the files without changing them.

As for the get_area.sh and sum_area.py scripts, run them in that order. The get area.sh script simply runs the command for mangle to find the area of each polygon that describes the full mask, and the python script then reads the new file with areas and sums them together. 
