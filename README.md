# waves_polygon_mask
A repo for mangle code for generating waves masks.
This code will generate mangle masks for the waves regions. You must have mangle installed from: https://space.mit.edu/~molly/mangle/. Please note mangle currently does not run on apple silicon.

The python scripts have already been run, but if needed you can rerun them. If you do, some manual edits are required for the ngc dat files. These are detailed below. These scripts output the repacked star/ngc/ghost masks in a mangle friendly format. The outputs are the '*.dat' files. You must unzip the large file 23-06-25_masked_objects_list/Masking/gaiastarmaskwaves.csv.zip before running the python code for generating the starmask dat file. 

To run the code, run the shell scripts. They must be run in order; make_waves_wide_rects.sh, make_masks.sh, combine_masks_main.sh. combine_mask_permutations.sh can be run to generate different permuations of the mask, swapping in or out stars, ngcs etc. The main mask will be saved as waves_wide_(N/S)_full_mask.ply in the home directory here, and the permuations will be saved in final_masks/.

To alter the compoisition of the mask, change the pixelize command in combine_masks.sh. In this command all the masks are added to the rectangle window. Remove/add as you wish. The default is the 'full mask', i.e. Window-starmask-ghostmask-ngcmask(-extramask for waves-S).

The 'old_radius_rule' files use the older rules for starmasking, that originate in GAMA dr4 (Bellstedt+2020). There are no seperate ghostmasks for this older version. 

Finally, it is important to note that one custom starmask (in 'ngc_s.dat') has an altered mask in these files. This is the mask covered by the coordinates at the bottom of this readme. We removed the first vertex, and this allows mangle to accept the coordinates. 

Additionally, some of the other NGC masks have an 'r' infront of them in the dat files. This is because for mangle vertices must be supplied in a counterclockwise fashion. These vertices are given clockwise, and so mangle demands an r be placed infront. Mangle will raise this as an error if you run the files without changing them.

Coords of alterted NGC. 
12.8079466751452 -34.0415904616558 12.7831777385283 -34.0495473349402 12.7670770024823 -34.0649366696386 12.7599021107783 -34.0757610555881 12.7652825611636 -34.0986212005406 12.7754591790667 -34.11327664894 12.7915729794916 -34.124084445202 12.7886075728582 -34.1296829907285 12.7664628878019 -34.1273662408748 12.7472632573874 -34.1201787884075 12.7328423012578 -34.1108339952082 12.7213439888796 -34.0923996826255 12.7211274342094 -34.0707418456473 12.7268365677775 -34.05528742605 12.7376684338986 -34.0446640123143 12.75618190299 -34.0336280189763 12.7729558841024 -34.0297725459863 12.7933640732484 -34.0305128015403 12.8067077217364 -34.0375334091509

