'''OpenGL extension EXT.blend_func_extended

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.blend_func_extended to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides an ES version of the ARB_blend_func_extended
	functionality.
	
	Traditional OpenGL includes fixed-function blending that combines
	source colors with the existing content of a render buffer in
	a variety of ways.  A number of extensions have enhanced this
	functionality by adding further sources of blending weights and
	methods to combine them. However, the inputs to the fixed-function
	blending units are constrained to a source color (as output from
	fragment shading), destination color (as the current content of the
	frame buffer) or constants that may be used in their place.
	
	This extension adds new blending functions whereby a fragment
	shader may output two colors, one of which is treated as the
	source color, and the other used as a blending factor for either
	source or destination colors.  Furthermore, this extension increases
	orthogonality by allowing the SRC_ALPHA_SATURATE function to be used
	as the destination weight.
	
	Because of the limitations of the OpenGL ES 2.0 shading language,
	new built-in variables (gl_SecondaryFragColorEXT,
	gl_SecondaryFragDataEXT) are added to the ES 1.00 shading language
	rather than introduce more complex features for user-defined fragment
	outputs.  Because such built-in variable are deprecated in ES 3.0,
	these variables are NOT available in the OpenGL ES 3.xx shading
	language verisons.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/blend_func_extended.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.EXT.blend_func_extended import *
from OpenGL.raw.GLES2.EXT.blend_func_extended import _EXTENSION_NAME

def glInitBlendFuncExtendedEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glBindFragDataLocationEXT.name size not checked against 'name'
glBindFragDataLocationEXT=wrapper.wrapper(glBindFragDataLocationEXT).setInputArraySize(
    'name', None
)
# INPUT glGetProgramResourceLocationIndexEXT.name size not checked against 'name'
glGetProgramResourceLocationIndexEXT=wrapper.wrapper(glGetProgramResourceLocationIndexEXT).setInputArraySize(
    'name', None
)
### END AUTOGENERATED SECTION