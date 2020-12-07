from reclassify_raster import RasterReclassification as RR
import matplotlib.pyplot as plt
import numpy
import rasterio as rio

files = "C:/Users/Lisapisa/Documents/Master/Masterthesis/Landsberg/samples/labels/0"
exp = "C:/Users/Lisapisa/Documents/Master/Masterthesis/01-Raster/samples/labels"

new = RR(files, exp)
new.reclassify()

# Check created TIF file
# src = rio.open("example.tif")
# img = src.read()
# src.close()
# plt.imshow(img.squeeze())
# plt.show()
