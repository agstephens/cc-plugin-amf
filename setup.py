from __future__ import with_statement
import sys

from setuptools import setup, find_packages

from cc_plugin_amf import __version__

def readme():
    with open('README.md') as f:
        return f.read()

reqs = [line.strip() for line in open('requirements.txt')]

setup(name                 = "cc-plugin-amf",
    version              = __version__,
    description          = "Compliance Checker AMF plugin",
    long_description     = readme(),
    license              = 'BSD License',
    author               = "Ag Stephens",
    author_email         = "ag.stephens@stfc.ac.uk",
    url                  = "https://github.com/ukcp-data/cc-plugin-amf",
    packages             = find_packages(),
    install_requires     = reqs,
    classifiers          = [
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: BSD Software License',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering',
        ],
    entry_points         = {
        'compliance_checker.suites': [
            'amf-file-info = cc_plugin_amf.amf_file_info:AMFFileInfoCheck',
            'amf-global-attrs = cc_plugin_amf.amf_global_attrs:AMFGlobalAttrsCheck',
            'amf-common-variables = cc_plugin_amf.amf_common_variables:AMFCommonVariablesCheck'
        ]
    }
)

