#!/usr/bin/env python
"""
cc_plugin_amf.amf_common_variables

Compliance Test Suite: Check common variables in AMF files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ncas"

# Import checklib
import checklib.register.nc_file_checks_register as check_package


class AMFCommonVariablesCheck(BaseNCCheck):
    register_checker = True
    name = 'amf-common-variables'


    def setup(self, ds):
        pass

    
    def check_varattrs01(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'time'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_varattrs02(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'day_of_year'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_varattrs03(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'year'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_varattrs04(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'month'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_varattrs05(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'day'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_varattrs06(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'hour'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_varattrs07(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'minute'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_varattrs08(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'second'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype01(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'time'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_vartype02(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'day_of_year'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_vartype03(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'int32', 'var_id': 'year'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_vartype04(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'int32', 'var_id': 'month'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_vartype05(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'int32', 'var_id': 'day'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_vartype06(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'int32', 'var_id': 'hour'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_vartype07(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'int32', 'var_id': 'minute'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_vartype08(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'second'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    