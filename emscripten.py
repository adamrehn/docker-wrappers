#!/usr/bin/env python
from _common import generateWrappers

EMSCRIPTEN_VERSION = '1.37.3'
DOCKER_IMAGE = 'trzeci/emscripten:sdk-tag-{}-64bit'.format(EMSCRIPTEN_VERSION)
TOOLS = [
	'em++',
	'em-config',
	'emar',
	'emcc',
	'emcmake',
	'emconfigure',
	'emmake',
	'emranlib',
	'emrun',
	'emscons'
]

# Generate the wrappers
generateWrappers(DOCKER_IMAGE, TOOLS)
