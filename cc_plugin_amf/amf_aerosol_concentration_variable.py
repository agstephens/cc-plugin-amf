#!/usr/bin/env python
"""
cc_plugin_amf.amf_aerosol_concentration_variable

Compliance Test Suite: Check aerosol concentration variable in AMF files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ncas"

# Import checklib
import checklib.register.nc_file_checks_register as check_package


class AMFAerosolConcentrationVariableCheck(BaseNCCheck):
    register_checker = True
    name = 'amf-aerosol_concentration_variable'


    def setup(self, ds):
        pass

    
    def check_varattrs1(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'qc_flag', 'pyessv_namespace': 'aerosol_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype1(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'byte', 'var_id': 'qc_flag'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs2(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'number_concentration_of_ambient_aerosol_particles_in_air', 'pyessv_namespace': 'aerosol_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype2(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'number_concentration_of_ambient_aerosol_particles_in_air'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    