#!/usr/bin/env python
"""
cc_plugin_amf.amf_global_attrs_stationary

Compliance Test Suite: Check stationary platform global attributes in AMF files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ncas"

# Import checklib
import checklib.register.nc_file_checks_register as check_package


class AMFGlobalAttrsStationaryCheck(BaseNCCheck):
    register_checker = True
    name = 'amf-global-attrs-stationary'


    def setup(self, ds):
        pass

    
    def check_gas01(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'platform_location'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gas02(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'platform_height'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    