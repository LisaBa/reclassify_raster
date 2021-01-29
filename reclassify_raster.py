import numpy as np
import glob
import os
import rasterio as rio
import matplotlib.pyplot as plt


class RasterReclassification:
    def __init__(self, image_folder: str, export_folder: str, file_type=".tif"):
        self.image_folder = image_folder
        self.file_type = file_type
        self.export_folder = export_folder

    def reclassify(self, new_value=0):
        image_list = [
            f for f in os.listdir(self.image_folder) if f.endswith(self.file_type)
        ]

        for image in image_list:
            # Load image into numpy array
            with rio.open(os.path.join(self.image_folder, image)) as src:
                img = src.read()

                # Replace all values other than 0 with the set value
                img = np.where(img > 0, new_value, 0)
                print(img.shape)

                # Safe reclassified raster
                with rio.Env():

                    # Write an array as a raster band to a new 8-bit file. For
                    # the new file's profile, we start with the profile of the source
                    profile = src.profile

                    # And then change the band count to 1, set the
                    # dtype to uint8, and specify LZW compression.
                    profile.update(dtype=rio.uint8, count=1, compress="lzw")

                    with rio.open(
                        os.path.join(self.export_folder, image), "w", **profile
                    ) as dst:
                        dst.write(img.astype(rio.uint8))
