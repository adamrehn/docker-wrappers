Docker Wrappers
===============

The Python files in this repository generate a series of small wrapper scripts for various software packages. The generated wrapper scripts are designed to be run by [docker-script](https://github.com/adamrehn/docker-script), **which needs to be installed and available in the system PATH.** Generated wrapper scripts are placed in the following location, which should also be added to the system PATH:

- Under Windows: `%HOMEDRIVE%\%HOMEPATH%\.docker-wrappers`
- Under macOS and Linux: `$HOME/.docker-wrappers`

These wrappers make it simple to use command-line applications directly from within Docker containers, without needing to install the relevant packages and dependencies on the host. When a new version of a given piece of software is released, the previous Docker image for that software can simply be deleted and replaced with its updated counterpart, simplifying both upgrading and uninstallation.

This is particularly helpful when working with software for which packages are either missing or infrequently updated, and provides a consistent experience under Windows, macOS, and Linux.


Emscripten Wrappers
-------------------

**Generate using:** `python3 ./emscripten.py`

**Docker image:** [trzeci/emscripten](https://hub.docker.com/r/trzeci/emscripten/)

**Generated wrappers:**

- `em++`
- `em-config`
- `emar`
- `emcc`
- `emcmake`
- `emconfigure`
- `emmake`
- `emranlib`
- `emrun`
- `emscons`


GDAL Wrappers
-------------

**Generate using:** `python3 ./gdal.py`

**Docker image:** [geodata/gdal](https://hub.docker.com/r/geodata/gdal/)

**Generated wrappers:**

- `gdalinfo`
- `gdal_translate`
- `gdaladdo`
- `gdalwarp`
- `gdaltindex`
- `gdalbuildvrt`
- `gdal_contour`
- `gdaldem`
- `gdal_rasterize`
- `gdaltransform`
- `gdal_grid`
- `gdallocationinfo`
- `gdalsrsinfo`
- `gdalmanage`
