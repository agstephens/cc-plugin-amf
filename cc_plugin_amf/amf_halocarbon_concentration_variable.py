#!/usr/bin/env python
"""
cc_plugin_amf.amf_halocarbon_concentration_variable

Compliance Test Suite: Check halocarbon concentration variable in AMF files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ncas"

# Import checklib
import checklib.register.nc_file_checks_register as check_package


class AMFHalocarbonConcentrationVariableCheck(BaseNCCheck):
    register_checker = True
    name = 'amf-halocarbon_concentration_variable'


    def setup(self, ds):
        pass

    
    def check_varattrs1(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'mole_fraction_of_bromodichloromethane_in_air', 'pyessv_namespace': 'halocarbon_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype1(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'mole_fraction_of_bromodichloromethane_in_air'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs2(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'qc_flag_ch2icl', 'pyessv_namespace': 'halocarbon_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype2(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'byte', 'var_id': 'qc_flag_ch2icl'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs3(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'mole_fraction_of_bromoform_in_air', 'pyessv_namespace': 'halocarbon_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype3(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'mole_fraction_of_bromoform_in_air'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs4(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'qc_flag_chbrcl2', 'pyessv_namespace': 'halocarbon_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype4(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'byte', 'var_id': 'qc_flag_chbrcl2'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs5(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'mole_fraction_of_dibromomethane_in_air', 'pyessv_namespace': 'halocarbon_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype5(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'mole_fraction_of_dibromomethane_in_air'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs6(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'mole_fraction_of_methyl_iodide_in_air', 'pyessv_namespace': 'halocarbon_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype6(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'mole_fraction_of_methyl_iodide_in_air'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs7(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'mole_fraction_of_bromochloromethane_in_air', 'pyessv_namespace': 'halocarbon_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype7(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'mole_fraction_of_bromochloromethane_in_air'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs8(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'mole_fraction_of_diiodomethane_in_air', 'pyessv_namespace': 'halocarbon_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype8(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'mole_fraction_of_diiodomethane_in_air'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs9(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'qc_flag_ccl4', 'pyessv_namespace': 'halocarbon_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype9(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'byte', 'var_id': 'qc_flag_ccl4'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs10(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'qc_flag_chbr3', 'pyessv_namespace': 'halocarbon_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype10(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'byte', 'var_id': 'qc_flag_chbr3'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs11(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'qc_flag_ch2i2', 'pyessv_namespace': 'halocarbon_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype11(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'byte', 'var_id': 'qc_flag_ch2i2'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs12(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'qc_flag_ch3i', 'pyessv_namespace': 'halocarbon_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype12(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'byte', 'var_id': 'qc_flag_ch3i'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs13(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'mole_fraction_of_carbon_tetrachloride_in_air', 'pyessv_namespace': 'halocarbon_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype13(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'mole_fraction_of_carbon_tetrachloride_in_air'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs14(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'mole_fraction_of_chloroform_in_air', 'pyessv_namespace': 'halocarbon_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype14(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'mole_fraction_of_chloroform_in_air'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs15(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'qc_flag_chcl3', 'pyessv_namespace': 'halocarbon_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype15(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'byte', 'var_id': 'qc_flag_chcl3'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs16(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'qc_flag_ch2br2', 'pyessv_namespace': 'halocarbon_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype16(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'byte', 'var_id': 'qc_flag_ch2br2'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_varattrs17(self, ds):
        return check_package.NCVariableMetadataCheck(kwargs={'var_id': 'mole_fraction_of_chloroiodomethane_in_air', 'pyessv_namespace': 'halocarbon_concentration_variable'},
                                                    level="HIGH",
                                                    vocabulary_ref="ncas:amf")(ds)
    
    def check_vartype17(self, ds):
        return check_package.VariableTypeCheck(kwargs={'dtype': 'float64', 'var_id': 'mole_fraction_of_chloroiodomethane_in_air'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    