#!/usr/bin/env python
"""
cc_plugin_amf.amf_common_land_dimension

Compliance Test Suite: Check common land variable in AMF files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ncas"

# Import checklib
import checklib.register.nc_file_checks_register as check_package


class AMFCommonLandDimensionCheck(BaseNCCheck):
    register_checker = True
    name = 'amf-common_land_dimension'


    def setup(self, ds):
        pass

    
    def check_dim1(self, ds):
        return check_package.NetCDFDimensionCheck(kwargs={'dim_id': 'time', 'pyessv_namespace': 'common_land_dimension'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)

    def check_dim2(self, ds):
        return check_package.NetCDFDimensionCheck(kwargs={'dim_id': 'latitude', 'pyessv_namespace': 'common_land_dimension'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)

    def check_dim3(self, ds):
        return check_package.NetCDFDimensionCheck(kwargs={'dim_id': 'longitude', 'pyessv_namespace': 'common_land_dimension'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)

