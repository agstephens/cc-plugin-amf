#!/usr/bin/env python
"""
cc_plugin_amf.amf_rain_lwc_velocity_reflectivity_variable

Compliance Test Suite: Check rain lwc velocity reflectivity variable in AMF files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ncas"

# Import checklib
import checklib.register.nc_file_checks_register as check_package


class AMFRainLwcVelocityReflectivityVariableCheck(BaseNCCheck):
    register_checker = True
    name = 'amf-rain_lwc_velocity_reflectivity_variable'


    def setup(self, ds):
        pass

    
    def check_varattrs1(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'attenuated_radar_reflectivity', 'pyessv_namespace': 'rain_lwc_velocity_reflectivity_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype1(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'attenuated_radar_reflectivity'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs2(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'radar_reflectivity', 'pyessv_namespace': 'rain_lwc_velocity_reflectivity_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype2(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'radar_reflectivity'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs3(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'path_integrated_attenuation', 'pyessv_namespace': 'rain_lwc_velocity_reflectivity_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype3(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'path_integrated_attenuation'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs4(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'altitude', 'pyessv_namespace': 'rain_lwc_velocity_reflectivity_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype4(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'altitude'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs5(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'rainfall_rate', 'pyessv_namespace': 'rain_lwc_velocity_reflectivity_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype5(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'rainfall_rate'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs6(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'qc_flag', 'pyessv_namespace': 'rain_lwc_velocity_reflectivity_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype6(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'byte', 'var_id': 'qc_flag'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs7(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'rainfall_velocity', 'pyessv_namespace': 'rain_lwc_velocity_reflectivity_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype7(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'rainfall_velocity'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs8(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'rain_liquid_water_content', 'pyessv_namespace': 'rain_lwc_velocity_reflectivity_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype8(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'rain_liquid_water_content'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    