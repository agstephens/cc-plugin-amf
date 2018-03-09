#!/usr/bin/env python
"""
cc_plugin_amf.amf_flux_estimates_variable

Compliance Test Suite: Check flux estimates variable in AMF files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ncas"

# Import checklib
import checklib.register.nc_file_checks_register as check_package


class AMFFluxEstimatesVariableCheck(BaseNCCheck):
    register_checker = True
    name = 'amf-flux_estimates_variable'


    def setup(self, ds):
        pass

    
    def check_varattrs1(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'bowen_ratio', 'pyessv_namespace': 'flux_estimates_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype1(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'bowen_ratio'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs2(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'momentum_flux_v', 'pyessv_namespace': 'flux_estimates_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype2(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'momentum_flux_v'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs3(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'kinematic_sonic_temperature_flux', 'pyessv_namespace': 'flux_estimates_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype3(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'kinematic_sonic_temperature_flux'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs4(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'qc_flag_skew_w', 'pyessv_namespace': 'flux_estimates_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype4(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'byte', 'var_id': 'qc_flag_skew_w'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs5(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'momentum_flux_u', 'pyessv_namespace': 'flux_estimates_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype5(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'momentum_flux_u'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs6(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'upward_latent_heat_flux_in_air', 'pyessv_namespace': 'flux_estimates_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype6(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'upward_latent_heat_flux_in_air'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs7(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'qc_flag_skew_u', 'pyessv_namespace': 'flux_estimates_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype7(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'byte', 'var_id': 'qc_flag_skew_u'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs8(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'qc_flag_skew_v', 'pyessv_namespace': 'flux_estimates_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype8(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'byte', 'var_id': 'qc_flag_skew_v'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs9(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'start_of_run', 'pyessv_namespace': 'flux_estimates_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype9(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'start_of_run'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs10(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'run_length', 'pyessv_namespace': 'flux_estimates_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype10(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'run_length'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs11(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'qc_flag_kurtosis_v ', 'pyessv_namespace': 'flux_estimates_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype11(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'byte', 'var_id': 'qc_flag_kurtosis_v '},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs12(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'qc_flag_kurtosis_u ', 'pyessv_namespace': 'flux_estimates_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype12(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'byte', 'var_id': 'qc_flag_kurtosis_u '},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs13(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'buoyancy_flux', 'pyessv_namespace': 'flux_estimates_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype13(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'buoyancy_flux'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs14(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'upward_sensible_heat_flux_in_air', 'pyessv_namespace': 'flux_estimates_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype14(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'upward_sensible_heat_flux_in_air'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs15(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'qc_flag_skew_ts', 'pyessv_namespace': 'flux_estimates_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype15(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'byte', 'var_id': 'qc_flag_skew_ts'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs16(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'kinematic_humidity_flux', 'pyessv_namespace': 'flux_estimates_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype16(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'kinematic_humidity_flux'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs17(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'number_of_samples_in_run', 'pyessv_namespace': 'flux_estimates_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype17(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'number_of_samples_in_run'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    