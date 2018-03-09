#!/usr/bin/env python
"""
cc_plugin_amf.amf_aerosol_no3_so4_nh3_org_concentration_variable

Compliance Test Suite: Check aerosol no3 so4 nh3 org concentration variable in AMF files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ncas"

# Import checklib
import checklib.register.nc_file_checks_register as check_package


class AMFAerosolNo3So4Nh3OrgConcentrationVariableCheck(BaseNCCheck):
    register_checker = True
    name = 'amf-aerosol_no3_so4_nh3_org_concentration_variable'


    def setup(self, ds):
        pass

    
    def check_varattrs1(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'mass_concentration_of_organics_in_ ambient_aerosol_particles_in_air', 'pyessv_namespace': 'aerosol_no3_so4_nh3_org_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype1(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'mass_concentration_of_organics_in_ ambient_aerosol_particles_in_air'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs2(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'qc_flag_org', 'pyessv_namespace': 'aerosol_no3_so4_nh3_org_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype2(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'byte', 'var_id': 'qc_flag_org'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs3(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'mass_concentration_of_nitrate_in_ambient_aerosol_particles_in_air', 'pyessv_namespace': 'aerosol_no3_so4_nh3_org_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype3(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'mass_concentration_of_nitrate_in_ambient_aerosol_particles_in_air'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs4(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'qc_flag_no3', 'pyessv_namespace': 'aerosol_no3_so4_nh3_org_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype4(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'byte', 'var_id': 'qc_flag_no3'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs5(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'mass_concentration_of_sulfate_in_ambient_aerosol_particles_in_air', 'pyessv_namespace': 'aerosol_no3_so4_nh3_org_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype5(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'mass_concentration_of_sulfate_in_ambient_aerosol_particles_in_air'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs6(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'qc_flag_so4', 'pyessv_namespace': 'aerosol_no3_so4_nh3_org_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype6(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'byte', 'var_id': 'qc_flag_so4'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs7(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'qc_flag_nh3', 'pyessv_namespace': 'aerosol_no3_so4_nh3_org_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype7(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'byte', 'var_id': 'qc_flag_nh3'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs8(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'mass_concentration_of_ammonium_in_ ambient_aerosol_particles_in_air', 'pyessv_namespace': 'aerosol_no3_so4_nh3_org_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype8(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'mass_concentration_of_ammonium_in_ ambient_aerosol_particles_in_air'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    