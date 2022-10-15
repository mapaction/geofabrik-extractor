# Geofabrik Extractor

Extract zipped data from Geofabrik, sort and rename into MapActions naming conventions and folder structure

## Usage

### For Zip Files
- Go to the [Geofabrik Download website](https://download.geofabrik.de)
- Navigate to the country page of interest, and download the zipped shapefile. For example, for [Austria](https://download.geofabrik.de/europe/austria.html), download austria-latest-free.shp.zip

Usage: ``python3 geofabrik-extractor.py --zip path/to/your/zipfile.zip``

For example:
   ``python3 geofabrik-extractor.py --zip /Users/cate/git/data/country_data/sudan/sudan-latest-free.zip`` 
   
This would produce a folder named `/processed` in folder structure containing renamed shapefiles as below:

``
    /Users/cate/git/data/country_data/sudan/processed/206_bldg/sdn_bldg_bdg_py_s0_osm_pp_buildings.shp
    /Users/cate/git/data/country_data/sudan/processed/218_land/sdn_land_lnd_py_s0_osm_pp_landuse.shp
    /Users/cate/git/data/country_data/sudan/processed/221_phys/sdn_phys_lak_py_s0_osm_pp_waterbodies.shp
    /Users/cate/git/data/country_data/sudan/processed/221_phys/sdn_phys_nat_pt_s0_osm_pp_natural.shp
    /Users/cate/git/data/country_data/sudan/processed/221_phys/sdn_phys_nat_py_s0_osm_pp_natural.shp
    /Users/cate/git/data/country_data/sudan/processed/221_phys/sdn_phys_riv_ln_s0_osm_pp_rivers.shp
    /Users/cate/git/data/country_data/sudan/processed/222_pois/sdn_pois_poi_pt_s0_osm_pp_pointsofinterest.shp
    /Users/cate/git/data/country_data/sudan/processed/222_pois/sdn_pois_poi_py_s0_osm_pp_pointsofinterest.shp
    /Users/cate/git/data/country_data/sudan/processed/222_pois/sdn_pois_rel_pt_s0_osm_pp_placeofworship.shp
    /Users/cate/git/data/country_data/sudan/processed/222_pois/sdn_pois_rel_py_s0_osm_pp_placeofworship.shp
    /Users/cate/git/data/country_data/sudan/processed/229_stle/sdn_stle_stl_pt_s0_osm_pp_settlements.shp
    /Users/cate/git/data/country_data/sudan/processed/229_stle/sdn_stle_stl_py_s0_osm_pp_settlements.shp
    /Users/cate/git/data/country_data/sudan/processed/232_tran/sdn_tran_rds_ln_s0_osm_pp_roads.shp
    /Users/cate/git/data/country_data/sudan/processed/232_tran/sdn_tran_rrd_ln_s0_osm_pp_railways.shp
    /Users/cate/git/data/country_data/sudan/processed/232_tran/sdn_tran_trf_pt_s0_osm_pp_traffic.shp
    /Users/cate/git/data/country_data/sudan/processed/232_tran/sdn_tran_trf_py_s0_osm_pp_traffic.shp
    /Users/cate/git/data/country_data/sudan/processed/232_tran/sdn_tran_trn_pt_s0_osm_pp_transport.shp
    /Users/cate/git/data/country_data/sudan/processed/232_tran/sdn_tran_trn_py_s0_osm_pp_transport.shp
``

### For Zip File and Output Folder

For a pre-downloaded `zip` file, the output folder can optionally be specified with the `--outdir` parameter:

Usage: ``python3 geofabrik-extractor.py --zip path/to/your/zipfile.zip --outdir /path/to/output/folder``

For example:
   ``python3 geofabrik-extractor.py --zip /Users/cate/git/data/country_data/sudan/sudan-latest-free.zip --outdir /tmp`` 

This would produce a folder named `/processed` under the folder specified by the `--outdir` parameter:

``
    /tmp/processed/206_bldg/sdn_bldg_bdg_py_s0_osm_pp_buildings.shp
``

...
