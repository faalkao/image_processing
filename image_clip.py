"""
This is code to clip a multiple spectral satellite image, created by Duong
2020/05/30
"""
from osgeo import gdal
import os
from PIL import Image
inputPath = './data/other/'
outputPath = './data/other/'
shp_clip = './data/other/AOI_L8.shp'

bandList = [band for band in os.listdir(inputPath) if band[-8:]=='L8_2.tif'] #last 8 characters of the band
for band in bandList:
    print(outputPath+band[:-4]+'_clip'+band[-4:])
    options = gdal.WarpOptions(cutlineDSName=shp_clip, cropToCutline=True)
    outBand = gdal.Warp(srcDSOrSrcDSTab=inputPath+band,
                        destNameOrDestDS=outputPath+band[:-4]+'_clip'+band[-4:],
                        options=options
                        )
    outBand=None
