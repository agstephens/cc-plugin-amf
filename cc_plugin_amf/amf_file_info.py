#!/usr/bin/env python
"""
cc_plugin_amf.amf_file_info

Compliance Test Suite: Check file names and external information about AMF files
"""

import os
from netCDF4 import Dataset

# Import base objects from compliance checker
from compliance_checker.base import Result, GenericFile

# Restrict which vocabs will load (for efficiency)
os.environ["ESSV_VOCABS_ACTIVE"] = "ncas"

# Import checklib
import checklib.register.file_checks_register as check_package

class AMFFileInfoCheck(object):
    register_checker = True
    name = 'amf-file-info'
    supported_ds = [GenericFile, Dataset]


    def setup(self, fpath):
        pass

    
    def check_fi01(self, ds):
        return check_package.FileSizeCheck(kwargs={'threshold': 2, 'strictness': 'soft'},
                                                    level="MEDIUM",
                                                    vocabulary_ref="")(ds.filepath())
    
    def check_fi02(self, ds):
        return check_package.FileSizeCheck(kwargs={'threshold': 4, 'strictness': 'hard'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds.filepath())
    
    def check_fi03(self, ds):
        return check_package.FileNameStructureCheck(kwargs={'delimiter': '_', 'extension': '.nc'},
                                                    level="HIGH",
                                                    vocabulary_ref="")(ds.filepath())
    