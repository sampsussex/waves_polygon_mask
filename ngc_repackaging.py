#!/usr/bin/env python
# coding: utf-8
import os
import csv

def polygon_signed_area(vertices):
    """Compute signed area using planar approximation (RA, Dec in degrees).
    >0 => counterclockwise (left-handed), <0 => clockwise (right-handed)."""
    if len(vertices) < 3:
        return 0.0
    area = 0.0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]
        area += (x2 - x1) * (y2 + y1)
    return area / 2.0


def append_csv_files_as_polygons(folder_path, output_file_n, output_file_s):
    """
    Combine CSV files containing RA,Dec vertices into MANGLE-ready ASCII input.
    - Each polygon is separated by a blank line.
    - Adds 'r' prefix only if polygon is left-handed (CCW), so MANGLE reverses it.
    - Keeps full floating-point precision from input CSVs.
    - Repeats the first vertex at the end of each polygon to ensure closure.
    """
    polygons_north = []
    polygons_south = []

    for filename in sorted(os.listdir(folder_path)):
        if not filename.endswith('.csv'):
            continue

        file_path = os.path.join(folder_path, filename)
        vertices = []

        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)

            # Determine RA/Dec columns (skip optional index)
            if header and header[0].lower() in ['index', '', '0']:
                ra_col, dec_col = 1, 2
            else:
                ra_col, dec_col = 0, 1

            for row in reader:
                if not row or len(row) <= max(ra_col, dec_col):
                    continue
                try:
                    ra = float(row[ra_col])
                    dec = float(row[dec_col])
                except ValueError:
                    continue
                # Wrap RA into [0, 360)
                if ra < 0:
                    ra += 360.0
                vertices.append((ra, dec))

        if not vertices:
            continue

        # Ensure polygon is closed by repeating the first vertex
        if vertices[0] != vertices[-1]:
            vertices.append(vertices[0])

        # Determine orientation: CCW (area > 0) means left-handed
        area = polygon_signed_area(vertices)
        needs_reverse = area > 0.0  # CCW -> left-handed -> prefix 'r'

        # Convert vertices back to strings with full precision
        vertex_strs = [f"{ra} {dec}" for ra, dec in vertices]
        polygon_line = ('r ' if needs_reverse else '') + ' '.join(vertex_strs)

        # Split by Dec of first vertex (north/south)
        first_dec = vertices[0][1]
        if first_dec > -15:
            polygons_north.append(polygon_line)
        else:
            polygons_south.append(polygon_line)

    # Write outputs with blank lines between polygons
    with open(output_file_n, 'w', encoding='ascii') as f_n:
        f_n.write('\n\n'.join(polygons_north))
        f_n.write('\n')

    with open(output_file_s, 'w', encoding='ascii') as f_s:
        f_s.write('\n\n'.join(polygons_south))
        f_s.write('\n')


# Example usage
folder_path = '23-06-25_masked_objects_list/Masking/MaskPolygons_v1'
output_file_n = 'input_data/ngc_n.dat'
output_file_s = 'input_data/ngc_s.dat'

append_csv_files_as_polygons(folder_path, output_file_n, output_file_s)
print(f"Combined polygons written to {output_file_n} and {output_file_s}")
