#!/usr/bin/env python
"""
cc_plugin_amf.amf_ncas_radar_standard_v1_variable

Compliance Test Suite: Check ncas radar standard v1 variable in AMF files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ncas"

# Import checklib
import checklib.register.nc_file_checks_register as check_package


class AMFNcasRadarStandardV1VariableCheck(BaseNCCheck):
    register_checker = True
    name = 'amf-ncas_radar_standard_v1_variable'


    def setup(self, ds):
        pass

    
    def check_varattrs1(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'radar_antenna_gain_v', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype1(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float', 'var_id': 'radar_antenna_gain_v'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs2(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'radar_antenna_gain_h', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype2(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float', 'var_id': 'radar_antenna_gain_h'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs3(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'grid_mapping', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype3(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'int', 'var_id': 'grid_mapping'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs4(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'follow_mode', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype4(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'char', 'var_id': 'follow_mode'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs5(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'altitude', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype5(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'double', 'var_id': 'altitude'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs6(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'radar_rx_bandwidth', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype6(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float', 'var_id': 'radar_rx_bandwidth'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs7(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'status_xml', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype7(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'char', 'var_id': 'status_xml'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs8(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'latitude', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype8(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'double', 'var_id': 'latitude'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs9(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'radar_beam_width_v', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype9(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float', 'var_id': 'radar_beam_width_v'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs10(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'sweep_mode', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype10(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'char', 'var_id': 'sweep_mode'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs11(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'prt_mode', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype11(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'char', 'var_id': 'prt_mode'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs12(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'altitude_agl', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype12(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'double', 'var_id': 'altitude_agl'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs13(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'sweep_number', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype13(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'int', 'var_id': 'sweep_number'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs14(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'time_coverage_start', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype14(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'char', 'var_id': 'time_coverage_start'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs15(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'radar_beam_width_h', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype15(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float', 'var_id': 'radar_beam_width_h'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs16(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'polarization_mode', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype16(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'char', 'var_id': 'polarization_mode'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs17(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'primary_axis', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype17(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'char', 'var_id': 'primary_axis'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs18(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'time_coverage_end', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype18(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'char', 'var_id': 'time_coverage_end'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs19(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'fixed_angle', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype19(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float', 'var_id': 'fixed_angle'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs20(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'longitude', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype20(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'double', 'var_id': 'longitude'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs21(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'volume_number', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype21(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'int', 'var_id': 'volume_number'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs22(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'platform_type', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype22(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'char', 'var_id': 'platform_type'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs23(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'frequency', 'pyessv_namespace': 'ncas_radar_standard_v1_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype23(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float', 'var_id': 'frequency'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    