#! /bin/bash
PROJECT_FOLDER=~/zugprojekt/
DATA_FOLDER="${PROJECT_FOLDER}kartendaten/"
SCRIPTS_FOLDER="${PROJECT_FOLDER}scripts/"
INFILE=germany-latest.o5m
OUTFILE=osmium_railway_routes_reduced

osmium tags-filter ${DATA_FOLDER}${INFILE} \
	--expressions=${SCRIPTS_FOLDER}osmium_railway_filter\
	-o ${DATA_FOLDER}${OUTFILE}.osm -v

osmtogeojson ${DATA_FOLDER}${OUTFILE}.osm > ${DATA_FOLDER}${OUTFILE}.geojson

sed -i -e "1i var train_routes =" ${DATA_FOLDER}${OUTFILE}.geojson

#	--drop="author" \
#	--drop-key="gauge" \
#	--drop-key="voltage" \
#	--drop-key="frequency" \
	
