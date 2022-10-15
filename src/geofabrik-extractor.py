import os
import shutil
import zipfile
from pathlib import Path
import urllib.request, json 
import ntpath
import argparse
import warnings
import re


def unzip(src_zip_file, dst_folder):
    """
    Unzips a zip file to the given location.

    Inputs:
        - src_zip_file (zip): Path to a zip file
        - dst_folder (str): Path to the destination folder
    Returns:
        - None
    """
    with zipfile.ZipFile(src_zip_file, 'r') as src:
        src.extractall(dst_folder)


def create_folder_structure(output_folder):
    """
    Create subfolders within a given output folder, using the MapAction naming conventions.

    Inputs:
        - output_folder (str): Path to the desired output folder

    Returns:
        - None
    """
    ma_folder_list = ["229_stle", "232_tran", "221_phys", "222_pois", "206_bldg", "218_land"]

    for ma_folder in ma_folder_list:
        dst_path = os.path.join(output_folder, ma_folder)
        if not os.path.exists(dst_path):
            os.makedirs(dst_path)


def extract_country_name(path_to_zip):
    """
    Get country name code from zip file name

    Inputs:
        - path_to_zip (str): Path to a zip file

    Returns:
        - country_text (str): The substring from the filename relating to the country name.
    """

    file_containing_country_name = Path(path_to_zip).stem

    print(f"> Extracting information for {file_containing_country_name}")

    suffix_to_remove = '-latest-free.shp'

    if suffix_to_remove in file_containing_country_name:
        country_text = file_containing_country_name.replace(suffix_to_remove, '')

    else:
        country_text = file_containing_country_name
        warnings.warn("The expected naming convention, 'country-name-latest-free.shp.zip', was not found. "
                      "This may result in unexpected behaviour.")
    return country_text


def use_regex(input_text):
    """
    Check that the input string matches the expected pattern for GeoFabrik shapefiles

    Inputs:
        - input_text (str):
    Returns:
        - bool
    """

    pattern = re.compile(r"^([A-Za-z0-9]+(_[A-Za-z0-9]+)+)\.[a-zA-Z]+$", re.IGNORECASE)
    return pattern.match(input_text)


def country_codes_from_geofabrik_country_name(geofabrik_country_name):
    alpha3_country_codes = []
    alpha2_country_codes = []
    with urllib.request.urlopen("https://download.geofabrik.de/index-v1-nogeom.json") as url:
        data = json.load(url)
        for feature in data['features']:
            if (feature['properties']['id'] == geofabrik_country_name): 
                if (feature['properties'].get("iso3166-1:alpha2", None) is not None):
                    if type(feature['properties']['iso3166-1:alpha2']) == type([]):
                        alpha2_country_codes = feature['properties']['iso3166-1:alpha2']
                    else:
                        alpha2_country_codes.append(feature['properties']['iso3166-1:alpha2'])

    for alpha2Code in alpha2_country_codes:
        alpha3_country_codes.append(alpha3code(alpha2Code))

    return (alpha3_country_codes)

def alpha3code(alpha2_country_code):
    """
    Returns alpha-3 country code for a given alpha-3 country code

    Inputs:
        - alpha-2 country code (str):
    Returns:
        - alpha-3 code (str)
    """
    alpha3Code = None
    found = False
    urlPath = "https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.json"
    with urllib.request.urlopen(urlPath) as url:
        data = json.load(url)

        for row in data:
            if (row['alpha-2'] == alpha2_country_code):
                return row['alpha-3'].lower()

    return (alpha3Code)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zipped folder downloaded from Geofabrik.")
    parser.add_argument("-z", "--zip", type=str, help="Zipped folder downloaded from Geofabrik.", default=None)
    parser.add_argument("-o", "--outdir", nargs='?', type=str, help="Folder in which to output the processed data.")
    args = parser.parse_args()

    if args.zip is not None:
        zip_filepath = args.zip
        zip_folder = os.path.dirname(zip_filepath)

    if args.outdir:
        output_root = os.path.join(args.outdir, 'processed')
    else:
        output_root = os.path.join(zip_folder, 'processed')

    unzip(zip_filepath, "temp_folder")
    create_folder_structure(output_root)

    extracted_file_list = []
    for root, dirs, files in os.walk(os.path.abspath("temp_folder")):
        for file in files:
            if use_regex(file):
                extracted_file_list.append(os.path.join(root, file))
            else:
                print(f"> Found file named '{file}', this file will not be processed.")

    print(f'> Found {len(extracted_file_list)} files correctly...processing')

    country_name = extract_country_name(zip_filepath)

    country_codes = country_codes_from_geofabrik_country_name(country_name)

    for country_code in (country_codes):
        print(" ")
        print("> Processing: " + country_name + " (" + country_code.upper() + ") to: " + (output_root.replace('\\', '/')))

        # Declare file names
        settlename = country_code + "_stle_stl_pt_s0_osm_pp_settlements"
        settlepyname = country_code + "_stle_stl_py_s0_osm_pp_settlements"
        roadname = country_code + "_tran_rds_ln_s0_osm_pp_roads"
        railname = country_code + "_tran_rrd_ln_s0_osm_pp_railways"
        traffptname = country_code + "_tran_trf_pt_s0_osm_pp_traffic"
        traffpyname = country_code + "_tran_trf_py_s0_osm_pp_traffic"
        transptname = country_code + "_tran_trn_pt_s0_osm_pp_transport"
        transpyname = country_code + "_tran_trn_py_s0_osm_pp_transport"
        waterwaysname = country_code + "_phys_riv_ln_s0_osm_pp_rivers"
        waterbodiesname = country_code + "_phys_lak_py_s0_osm_pp_waterbodies"
        naturalptname = country_code + "_phys_nat_pt_s0_osm_pp_natural"
        naturalpyname = country_code + "_phys_nat_py_s0_osm_pp_natural"
        powptname = country_code + "_pois_rel_pt_s0_osm_pp_placeofworship"
        powpyname = country_code + "_pois_rel_py_s0_osm_pp_placeofworship"
        poisptname = country_code + "_pois_poi_pt_s0_osm_pp_pointsofinterest"
        poispyname = country_code + "_pois_poi_py_s0_osm_pp_pointsofinterest"
        bldgname = country_code + "_bldg_bdg_py_s0_osm_pp_buildings"
        landname = country_code + "_land_lnd_py_s0_osm_pp_landuse"

        for filepath in extracted_file_list:
            filename, ext = ntpath.splitext(ntpath.basename(filepath))

            if filename == "gis_osm_places_free_1":
                dst = os.path.join(output_root, "229_stle", settlename + ext)
                shutil.copy(filepath, dst)

            elif filename == "gis_osm_places_a_free_1":
                dst = os.path.join(output_root, "229_stle", settlepyname + ext)
                shutil.copy(filepath, dst)

            elif filename == "gis_osm_railways_free_1":
                dst = os.path.join(output_root, "232_tran", railname + ext)
                shutil.copy(filepath, dst)

            elif filename == "gis_osm_roads_free_1":
                dst = os.path.join(output_root, "232_tran", roadname + ext)
                shutil.copy(filepath, dst)

            elif filename == "gis_osm_traffic_free_1":
                dst = os.path.join(output_root, "232_tran", traffptname + ext)
                shutil.copy(filepath, dst)

            elif filename == "gis_osm_traffic_a_free_1":
                dst = os.path.join(output_root, "232_tran", traffpyname + ext)
                shutil.copy(filepath, dst)

            elif filename == "gis_osm_transport_free_1":
                dst = os.path.join(output_root, "232_tran", transptname + ext)
                shutil.copy(filepath, dst)

            elif filename == "gis_osm_transport_a_free_1":
                dst = os.path.join(output_root, "232_tran", transpyname + ext)
                shutil.copy(filepath, dst)

            elif filename == "gis_osm_water_a_free_1":
                dst = os.path.join(output_root, "221_phys", waterbodiesname + ext)
                shutil.copy(filepath, dst)

            elif filename == "gis_osm_waterways_free_1":
                dst = os.path.join(output_root, "221_phys", waterwaysname + ext)
                shutil.copy(filepath, dst)

            elif filename == "gis_osm_natural_free_1":
                dst = os.path.join(output_root, "221_phys", naturalptname + ext)
                shutil.copy(filepath, dst)

            elif filename == "gis_osm_natural_a_free_1":
                dst = os.path.join(output_root, "221_phys", naturalpyname + ext)
                shutil.copy(filepath, dst)

            elif filename == "gis_osm_pofw_free_1":
                dst = os.path.join(output_root, "222_pois", powptname + ext)
                shutil.copy(filepath, dst)

            elif filename == "gis_osm_pofw_a_free_1":
                dst = os.path.join(output_root, "222_pois", powpyname + ext)
                shutil.copy(filepath, dst)

            elif filename == "gis_osm_pois_free_1":
                dst = os.path.join(output_root, "222_pois", poisptname + ext)
                shutil.copy(filepath, dst)

            elif filename == "gis_osm_pois_a_free_1":
                dst = os.path.join(output_root, "222_pois", poispyname + ext)
                shutil.copy(filepath, dst)

            elif filename == "gis_osm_buildings_a_free_1":
                dst = os.path.join(output_root, "206_bldg", bldgname + ext)
                shutil.copy(filepath, dst)

            elif filename == "gis_osm_landuse_a_free_1":
                dst = os.path.join(output_root, "218_land", landname + ext)
                shutil.copy(filepath, dst)

    shutil.rmtree("temp_folder", ignore_errors=False, onerror=None)
    print("> Process complete.")
