#!/usr/bin/env python
"""
cc_plugin_amf.amf_global_attrs_common

Compliance Test Suite: Check common global attributes in AMF files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, BaseNCCheck

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ncas"

# Import checklib
import checklib.register.nc_file_checks_register as check_package


class AMFGlobalAttrsCommonCheck(BaseNCCheck):
    register_checker = True
    name = 'amf-global-attrs-common'


    def setup(self, ds):
        pass

    
    def check_gac01(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': 'CF-1\\.6', 'attribute': 'Conventions'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac02(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'source'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac03(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'instrument_manufacturer'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac04(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'instrument_model'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac05(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'serial_number'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac06(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'operational_software'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac07(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'operational_software_version'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac08(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'creator_name'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac09(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.+@.+\\..+', 'attribute': 'creator_email'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac10(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': 'https:\\/\\/amf\\.ncas\\.ac\\.uk', 'attribute': 'creator_url'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac11(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': 'NCAS, National Centre for Atmospheric Science', 'attribute': 'institution'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac12(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'processing_software'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac13(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'processing_software_version'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac14(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'calibration_sensitivity'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac15(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'calibration_certification_date'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac16(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': 'http.+', 'attribute': 'calibration_certification_url'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac17(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'sampling_interval'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac18(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'averaging_interval'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac19(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'data_set_version'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac20(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'data_product_level'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac21(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'last_revised_date'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac22(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'project'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac23(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'project_principal_investigator'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac24(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'project_principal_investigator_contact'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac25(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'licence'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac26(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'acknowledgement'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac27(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'platform_type'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac28(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'platform_name'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac29(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'title'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac30(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '(timeSeriesPoint|timeSeriesProfile|trajectory)', 'attribute': 'feature_type'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac31(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}.*', 'attribute': 'start_time'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac32(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}.*', 'attribute': 'end_time'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac33(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'location_keywords'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac34(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'history'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
    def check_gac35(self, ds):
        return check_package.GlobalAttrRegexCheck(kwargs={'regex': '.{4,}', 'attribute': 'comment'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds)
    
