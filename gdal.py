#!/usr/bin/env python
from _common import generateWrappers

DOCKER_IMAGE = 'geodata/gdal:latest'
TOOLS = [
	'gdalinfo',
	'gdal_translate',
	'gdaladdo',
	'gdalwarp',
	'gdaltindex',
	'gdalbuildvrt',
	'gdal_contour',
	'gdaldem',
	'gdal_rasterize',
	'gdaltransform',
	'gdal_grid',
	'gdallocationinfo',
	'gdalsrsinfo',
	'gdalmanage'
]

# Generate the wrappers
generateWrappers(DOCKER_IMAGE, TOOLS)
