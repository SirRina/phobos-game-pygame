'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_AMD_framebuffer_sample_positions'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_AMD_framebuffer_sample_positions',error_checker=_errors._error_checker)
GL_ALL_PIXELS_AMD=_C('GL_ALL_PIXELS_AMD',0xFFFFFFFF)
GL_PIXELS_PER_SAMPLE_PATTERN_X_AMD=_C('GL_PIXELS_PER_SAMPLE_PATTERN_X_AMD',0x91AE)
GL_PIXELS_PER_SAMPLE_PATTERN_Y_AMD=_C('GL_PIXELS_PER_SAMPLE_PATTERN_Y_AMD',0x91AF)
GL_SUBSAMPLE_DISTANCE_AMD=_C('GL_SUBSAMPLE_DISTANCE_AMD',0x883F)
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,arrays.GLfloatArray)
def glFramebufferSamplePositionsfvAMD(target,numsamples,pixelindex,values):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLfloatArray)
def glGetFramebufferParameterfvAMD(target,pname,numsamples,pixelindex,size,values):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLfloatArray)
def glGetNamedFramebufferParameterfvAMD(framebuffer,pname,numsamples,pixelindex,size,values):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint,arrays.GLfloatArray)
def glNamedFramebufferSamplePositionsfvAMD(framebuffer,numsamples,pixelindex,values):pass