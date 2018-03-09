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
    author_email         = "joe.singleton@stfc.ac.uk",
    url                  = "https://github.com/joesingo/cc-plugin-amf",
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
            'amf-acoustic_backscatter_winds_variable = cc_plugin_amf.amf_acoustic_backscatter_winds_variable:AMFAcousticBackscatterWindsVariableCheck',
            'amf-aerosol_backscatter_radial_winds_variable = cc_plugin_amf.amf_aerosol_backscatter_radial_winds_variable:AMFAerosolBackscatterRadialWindsVariableCheck',
            'amf-aerosol_backscatter_variable = cc_plugin_amf.amf_aerosol_backscatter_variable:AMFAerosolBackscatterVariableCheck',
            'amf-aerosol_concentration_variable = cc_plugin_amf.amf_aerosol_concentration_variable:AMFAerosolConcentrationVariableCheck',
            'amf-aerosol_extinction_variable = cc_plugin_amf.amf_aerosol_extinction_variable:AMFAerosolExtinctionVariableCheck',
            'amf-aerosol_no3_so4_nh3_org_concentration_variable = cc_plugin_amf.amf_aerosol_no3_so4_nh3_org_concentration_variable:AMFAerosolNo3So4Nh3OrgConcentrationVariableCheck',
            'amf-aerosol_optical_depth_variable = cc_plugin_amf.amf_aerosol_optical_depth_variable:AMFAerosolOpticalDepthVariableCheck',
            'amf-aerosol_size_distribution_variable = cc_plugin_amf.amf_aerosol_size_distribution_variable:AMFAerosolSizeDistributionVariableCheck',
            'amf-ch4_concentration_variable = cc_plugin_amf.amf_ch4_concentration_variable:AMFCh4ConcentrationVariableCheck',
            'amf-cloud_base_variable = cc_plugin_amf.amf_cloud_base_variable:AMFCloudBaseVariableCheck',
            'amf-co2_concentration_variable = cc_plugin_amf.amf_co2_concentration_variable:AMFCo2ConcentrationVariableCheck',
            'amf-co_concentration_variable = cc_plugin_amf.amf_co_concentration_variable:AMFCoConcentrationVariableCheck',
            'amf-co_h2_concentration_variable = cc_plugin_amf.amf_co_h2_concentration_variable:AMFCoH2ConcentrationVariableCheck',
            'amf-common_air_variable = cc_plugin_amf.amf_common_air_variable:AMFCommonAirVariableCheck',
            'amf-common_land_variable = cc_plugin_amf.amf_common_land_variable:AMFCommonLandVariableCheck',
            'amf-common_sea_variable = cc_plugin_amf.amf_common_sea_variable:AMFCommonSeaVariableCheck',
            'amf-depolarisatio_ratio_variable = cc_plugin_amf.amf_depolarisatio_ratio_variable:AMFDepolarisatioRatioVariableCheck',
            'amf-dew_point_variable = cc_plugin_amf.amf_dew_point_variable:AMFDewPointVariableCheck',
            'amf-flux_components_variable = cc_plugin_amf.amf_flux_components_variable:AMFFluxComponentsVariableCheck',
            'amf-flux_estimates_variable = cc_plugin_amf.amf_flux_estimates_variable:AMFFluxEstimatesVariableCheck',
            'amf-halocarbon_concentration_variable = cc_plugin_amf.amf_halocarbon_concentration_variable:AMFHalocarbonConcentrationVariableCheck',
            'amf-liquid_water_content_variable = cc_plugin_amf.amf_liquid_water_content_variable:AMFLiquidWaterContentVariableCheck',
            'amf-mean_co2_h2o_variable = cc_plugin_amf.amf_mean_co2_h2o_variable:AMFMeanCo2H2oVariableCheck',
            'amf-mean_winds_profiles_variable = cc_plugin_amf.amf_mean_winds_profiles_variable:AMFMeanWindsProfilesVariableCheck',
            'amf-mean_winds_variable = cc_plugin_amf.amf_mean_winds_variable:AMFMeanWindsVariableCheck',
            'amf-n2o_sf6_concentration_variable = cc_plugin_amf.amf_n2o_sf6_concentration_variable:AMFN2oSf6ConcentrationVariableCheck',
            'amf-ncas_radar_standard_v1_variable = cc_plugin_amf.amf_ncas_radar_standard_v1_variable:AMFNcasRadarStandardV1VariableCheck',
            'amf-nox_noxy_concentration_variable = cc_plugin_amf.amf_nox_noxy_concentration_variable:AMFNoxNoxyConcentrationVariableCheck',
            'amf-o2n2_concentration_ratio_variable = cc_plugin_amf.amf_o2n2_concentration_ratio_variable:AMFO2n2ConcentrationRatioVariableCheck',
            'amf-o3_conccentration_profile_variable = cc_plugin_amf.amf_o3_conccentration_profile_variable:AMFO3ConccentrationProfileVariableCheck',
            'amf-o3_concentration_variable = cc_plugin_amf.amf_o3_concentration_variable:AMFO3ConcentrationVariableCheck',
            'amf-o3_photolysis_frequencies_variable = cc_plugin_amf.amf_o3_photolysis_frequencies_variable:AMFO3PhotolysisFrequenciesVariableCheck',
            'amf-oh_concentration_variable = cc_plugin_amf.amf_oh_concentration_variable:AMFOhConcentrationVariableCheck',
            'amf-peroxyacetyl_nitrate_concentration_variable = cc_plugin_amf.amf_peroxyacetyl_nitrate_concentration_variable:AMFPeroxyacetylNitrateConcentrationVariableCheck',
            'amf-radiation_variable = cc_plugin_amf.amf_radiation_variable:AMFRadiationVariableCheck',
            'amf-rain_lwc_velocity_reflectivity_variable = cc_plugin_amf.amf_rain_lwc_velocity_reflectivity_variable:AMFRainLwcVelocityReflectivityVariableCheck',
            'amf-size_concentration_spectra_variable = cc_plugin_amf.amf_size_concentration_spectra_variable:AMFSizeConcentrationSpectraVariableCheck',
            'amf-snr_winds_variable = cc_plugin_amf.amf_snr_winds_variable:AMFSnrWindsVariableCheck',
            'amf-so2_concentration_variable = cc_plugin_amf.amf_so2_concentration_variable:AMFSo2ConcentrationVariableCheck',
            'amf-soil_variable = cc_plugin_amf.amf_soil_variable:AMFSoilVariableCheck',
            'amf-solar_actinic_flux_variable = cc_plugin_amf.amf_solar_actinic_flux_variable:AMFSolarActinicFluxVariableCheck',
            'amf-sonde_variable = cc_plugin_amf.amf_sonde_variable:AMFSondeVariableCheck',
            'amf-surface_met_variable = cc_plugin_amf.amf_surface_met_variable:AMFSurfaceMetVariableCheck',
            'amf-tgm_concentration_variable = cc_plugin_amf.amf_tgm_concentration_variable:AMFTgmConcentrationVariableCheck'
        ]
    }
)

