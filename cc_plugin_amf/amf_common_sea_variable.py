#!/usr/bin/env python
"""
cc_plugin_amf.amf_common_sea_variable

Compliance Test Suite: Check common sea variable in AMF files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ncas"

# Import checklib
import checklib.register.nc_file_checks_register as check_package


class AMFCommonSeaVariableCheck(BaseNCCheck):
    register_checker = True
    name = 'amf-common_sea_variable'


    def setup(self, ds):
        pass

    
    def check_varattrs1(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'platform_roll_angle', 'pyessv_namespace': 'common_sea_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype1(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'platform_roll_angle'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs2(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'hour', 'pyessv_namespace': 'common_sea_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype2(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'int32', 'var_id': 'hour'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs3(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'platform_orientation', 'pyessv_namespace': 'common_sea_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype3(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'platform_orientation'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs4(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'year', 'pyessv_namespace': 'common_sea_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype4(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'int32', 'var_id': 'year'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs5(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'platform_yaw_angle', 'pyessv_namespace': 'common_sea_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype5(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'platform_yaw_angle'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs6(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'platform_course', 'pyessv_namespace': 'common_sea_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype6(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'platform_course'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs7(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'day_of_year', 'pyessv_namespace': 'common_sea_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype7(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'day_of_year'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs8(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'longitude', 'pyessv_namespace': 'common_sea_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype8(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'longitude'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs9(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'platform_yaw_rate', 'pyessv_namespace': 'common_sea_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype9(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'platform_yaw_rate'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs10(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'platform_pitch_angle', 'pyessv_namespace': 'common_sea_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype10(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'platform_pitch_angle'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs11(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'platform_roll_rate', 'pyessv_namespace': 'common_sea_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype11(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'platform_roll_rate'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs12(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'platform_speed_wrt_sea_water', 'pyessv_namespace': 'common_sea_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype12(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'platform_speed_wrt_sea_water'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs13(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'time', 'pyessv_namespace': 'common_sea_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype13(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'time'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs14(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'latitude', 'pyessv_namespace': 'common_sea_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype14(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'latitude'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs15(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'month', 'pyessv_namespace': 'common_sea_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype15(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'int32', 'var_id': 'month'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs16(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'platform_pitch_rate', 'pyessv_namespace': 'common_sea_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype16(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'platform_pitch_rate'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs17(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'day', 'pyessv_namespace': 'common_sea_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype17(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'int32', 'var_id': 'day'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    