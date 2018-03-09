#!/usr/bin/env python
"""
cc_plugin_amf.amf_flux_components_variable

Compliance Test Suite: Check flux components variable in AMF files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ncas"

# Import checklib
import checklib.register.nc_file_checks_register as check_package


class AMFFluxComponentsVariableCheck(BaseNCCheck):
    register_checker = True
    name = 'amf-flux_components_variable'


    def setup(self, ds):
        pass

    
    def check_varattrs1(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'humidity_mixing_ratio', 'pyessv_namespace': 'flux_components_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype1(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'humidity_mixing_ratio'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs2(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'eastward_wind', 'pyessv_namespace': 'flux_components_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype2(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'eastward_wind'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs3(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'upward_air_velocity', 'pyessv_namespace': 'flux_components_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype3(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'upward_air_velocity'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs4(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'northward_wind', 'pyessv_namespace': 'flux_components_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype4(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'northward_wind'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs5(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'mole_concentration_of_water_vapor_in_air', 'pyessv_namespace': 'flux_components_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype5(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'mole_concentration_of_water_vapor_in_air'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs6(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'sonic_temperature_theta', 'pyessv_namespace': 'flux_components_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype6(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'sonic_temperature_theta'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs7(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'mole_concentration_of_carbon_dioxide_in_air', 'pyessv_namespace': 'flux_components_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype7(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'mole_concentration_of_carbon_dioxide_in_air'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs8(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'air_pressure', 'pyessv_namespace': 'flux_components_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype8(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'air_pressure'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs9(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'eastward_wind_rotated_to_run', 'pyessv_namespace': 'flux_components_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype9(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'eastward_wind_rotated_to_run'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs10(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'specific_humidity', 'pyessv_namespace': 'flux_components_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype10(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'specific_humidity'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs11(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'licor_temperature', 'pyessv_namespace': 'flux_components_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype11(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'licor_temperature'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs12(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'run_length', 'pyessv_namespace': 'flux_components_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype12(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'run_length'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs13(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'start_of_run', 'pyessv_namespace': 'flux_components_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype13(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'start_of_run'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs14(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'sonic_air_temperature', 'pyessv_namespace': 'flux_components_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype14(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'sonic_air_temperature'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs15(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'water_vapor_partial_pressure_in_air', 'pyessv_namespace': 'flux_components_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype15(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'water_vapor_partial_pressure_in_air'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs16(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'number_of_samples_in_run', 'pyessv_namespace': 'flux_components_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype16(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'number_of_samples_in_run'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    