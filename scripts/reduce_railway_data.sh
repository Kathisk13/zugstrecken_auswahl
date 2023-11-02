#! /bin/bash
PROJECT_FOLDER=~/zugprojekt/
DATA_FOLDER="${PROJECT_FOLDER}kartendaten/"
SCRIPTS_FOLDER="${PROJECT_FOLDER}scripts/"
INFILE=germany-latest.o5m
OUTFILE=railway_routes_reduced

osmfilter32 ${DATA_FOLDER}${INFILE} \
	--parameter-file=${SCRIPTS_FOLDER}railway_filter\
	--out-o5m -o=${DATA_FOLDER}${OUTFILE}.o5m

osmconvert64 ${DATA_FOLDER}${OUTFILE}.o5m -o=${DATA_FOLDER}${OUTFILE}.osm

osmtogeojson ${DATA_FOLDER}${OUTFILE}.osm > ${DATA_FOLDER}${OUTFILE}.geojson

sed -i -e "1i var train_routes =" ${DATA_FOLDER}${OUTFILE}.geojson

#	--drop="author" \
#	--drop-key="gauge" \
#	--drop-key="voltage" \
#	--drop-key="frequency" \
	
