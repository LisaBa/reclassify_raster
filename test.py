from reclassify_raster import RasterReclassification as RR
import matplotlib.pyplot as plt
import numpy
import rasterio as rio
import os

files = (
    "C:/Users/Lisapisa/Documents/Master/Masterthesis/01-Raster/samples_negative/labels"
)
exp = "C:/Users/Lisapisa/Documents/Master/Masterthesis/01-Raster/samples_negative_edited/labels"

# new = RR(files, exp)
# new.reclassify(new_value=0)

# Check created TIF file
with rio.open(os.path.join(exp, "000000591.tif")) as src:
    img = src.read()
plt.imshow(img.squeeze())
plt.show()
