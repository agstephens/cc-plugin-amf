#!/usr/bin/env python
"""
cc_plugin_amf.amf_global_attrs_mobile_ship

Compliance Test Suite: Check mobile (ship) platform global attributes in AMF files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ncas"

# Import checklib
import checklib.register.nc_file_checks_register as check_package


class AMFGlobalAttrsMobileShipCheck(BaseNCCheck):
    register_checker = True
    name = 'amf-global-attrs-mobile-ship'


    def setup(self, ds):
        pass

    
    def check_gams01(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'start_location'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gams02(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'end_location'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    