#!/usr/bin/env python
# coding: utf-8
import os
import csv

# Simple code to reformat csv files from Sabine and split output into ngc_n.dat and ngc_s.dat
def append_csv_files_as_polygons(folder_path, output_file_n, output_file_s):
    # Lists to store polygons
    polygons_north = []
    polygons_south = []
    
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            polygon_vertices = []
            
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader)
                
                # Determine column indices
                if header[0].lower() in ['index', '', '0']:
                    ra_col, dec_col = 1, 2
                else:
                    ra_col, dec_col = 0, 1
                
                # Collect vertices
                for row in reader:
                    ra, dec = row[ra_col], row[dec_col]
                    polygon_vertices.append(f"{ra} {dec}")
            
            # Parse Dec of first vertex
            first_vertex_dec = float(polygon_vertices[0].split()[1])
            polygon_line = ' '.join(polygon_vertices)
            
            if first_vertex_dec > -15:
                polygons_north.append(polygon_line)
            else:
                polygons_south.append(polygon_line)
    
    # Write north file
    with open(output_file_n, 'w', encoding='ascii') as f_n:
        f_n.write('\n'.join(polygons_north))

    # Write south file
    with open(output_file_s, 'w', encoding='ascii') as f_s:
        f_s.write('\n'.join(polygons_south))


# Example usage:
folder_path = '23-06-25_stellar_ngc_lists/Masking/MaskPolygons_v1'
output_file_n = 'ngc_n.dat'
output_file_s = 'ngc_s.dat'

append_csv_files_as_polygons(folder_path, output_file_n, output_file_s)


#On these lines add an r infront, so it is the right way round for mangle: 
##rdmask: at line 57 of Sabines_NGCS/sabines_ngcs.dat: warning: polygon 0 may have its vertices ordered left- instead of right-handedly
#rdmask: at line 61 of Sabines_NGCS/sabines_ngcs.dat: warning: polygon 0 may have its vertices ordered left- instead of right-handedly
#rdmask: at line 71 of Sabines_NGCS/sabines_ngcs.dat: warning: polygon 0 may have its vertices ordered left- instead of right-handedly



#Also, polygon number 13 - at RA 12.76 DEC -34.048 has had the first point clipped from the original selection. The low separation between it and the final point seems to have been causing issues with MANGLE. Also have put an r infront for the same reason as above

