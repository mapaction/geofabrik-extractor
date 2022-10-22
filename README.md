# Geofabrik Extractor

Extract zipped data from Geofabrik, sort and rename into MapActions naming conventions and folder structure.

## Usage

There are two options for usage, either with a pre-downloaded zip file containing country data from Geofabrik, or using 
the ISO code of the country of interest. 

The optional parameter `--outdir` can be specified in either case, setting the desired output folder for processed 
files.

### Using a downloaded zipped file
- Go to the [Geofabrik Download website](https://download.geofabrik.de)
- Navigate to the country page of interest, and download the zipped shapefile. For example, for [Austria](https://download.geofabrik.de/europe/austria.html), download austria-latest-free.shp.zip

Usage:
```commandline
python3 geofabrik-extractor.py --zip path/to/your/zipfile.zip
```
The output folder can optionally be specified with the `--outdir` parameter:

```commandline
python3 geofabrik-extractor.py --zip path/to/your/zipfile.zip --outdir path/to/outdir
```
For example:
   ``python3 geofabrik-extractor.py --zip /Users/cate/git/data/country_data/sudan/sudan-latest-free.zip`` 
   
This would produce a folder named `/processed` in folder structure containing renamed shapefiles as below:


```
processed
│
└───206_bldg
│   │   sdn_bldg_bdg_py_s0_osm_pp_buildings.shp
│
└───218_land
│   │   sdn_land_lnd_py_s0_osm_pp_landuse.shp
│
└───221_phys
│   │   sdn_phys_lak_py_s0_osm_pp_waterbodies.shp
│   │   sdn_phys_nat_pt_s0_osm_pp_natural.shp
│   │   sdn_phys_nat_py_s0_osm_pp_natural.shp
│   │   sdn_phys_riv_ln_s0_osm_pp_rivers.shp
│
└───222_pois
│   │   sdn_pois_poi_pt_s0_osm_pp_pointsofinterest.shp
│   │   sdn_pois_poi_py_s0_osm_pp_pointsofinterest.shp
│   │   sdn_pois_rel_pt_s0_osm_pp_placeofworship.shp
│   │   sdn_stle_stl_pt_s0_osm_pp_settlements.shp
│
└───229_stle
│   │   sdn_stle_stl_py_s0_osm_pp_settlements.shp
│
└───232_tran
    │   sdn_tran_rds_ln_s0_osm_pp_roads.shp
    │   sdn_tran_rrd_ln_s0_osm_pp_railways.shp
    │   sdn_tran_trf_pt_s0_osm_pp_traffic.shp
    │   sdn_tran_trf_py_s0_osm_pp_traffic.shp
    │   sdn_tran_trn_pt_s0_osm_pp_transport.shp
    │   sdn_tran_trn_py_s0_osm_pp_transport.shp

```


### Using an ISO Country Code

Pass a two or three letter ISO Country Code to the script to automatically download and extract the data.

Usage: 
```
python3 geofabrik-extractor.py --iso MNE
```
The output folder can optionally be specified with the `--outdir` parameter:

```commandline
python3 geofabrik-extractor.py --iso MNE --outdir path/to/outdir
```