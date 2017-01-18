# -*- coding: utf-8 -*-
from __future__ import print_function

# this is the test function set for splat photometry functions

# imports - internal
import copy
import glob
import os
# # imports - external
import numpy
from astropy import units as u            # standard units
from astropy import constants as const        # physical constants in SI units
from astropy import coordinates as coord      # coordinate conversion
from astropy.io import fits
from numpy.testing.utils import assert_allclose

# splat functions and constants
from splat.initialize import *
from splat.utilities import *
import splat
#import splat as splat

# things to test
# isNumber 


#####################
# TESTING FUNCTIONS #
#####################


def test_refoutputs():
# shortRef
# longRef
# veryLongRef
    pass

def test_bibtex_retrieval():
# getBibTex
# getBibTexOnline
    pass

def test_parse_bibtex():
# bibTexParser
    pass

