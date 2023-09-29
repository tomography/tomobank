import sys
import os
import numpy as np
from PIL import Image


def load_tiff_dir(dirname):
    tiff_files = [f for f in os.listdir(dirname) if f.endswith('.tiff')]

    tiff_files.sort()

    tiff_arrays = []

    for tiff_file in tiff_files:
        tiff_path = os.path.join(dirname, tiff_file)
        
        with Image.open(tiff_path) as tiff_stack:
            tiff_array = np.array(tiff_stack)
            tiff_arrays.append(tiff_array)
    return tiff_arrays;

if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        
        projections = load_tiff_dir(filename)

        ##add your code here






