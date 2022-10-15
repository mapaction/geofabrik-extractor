# Geofabrik Extractor

Extract zipped data from Geofabrik, sort and rename into MapActions naming conventions and folder structure

## Instructions
- Go to the [Geofabrik Download website](https://download.geofabrik.de)
- Navigate to the country page of interest, and download the zipped shapefile. For example, for [Austria](https://download.geofabrik.de/europe/austria.html), download austria-latest-free.shp.zip

Usage: ``python3 geofabrik_to_mapaction.py path/to/your/zipfile.zip``

For example, ``python3 geofabrik_to_mapaction.py /Users/cate/git/data/country_data/sudan/sudan-latest-free.zip`` results in folder structure containing renamed shapefiles as below:
