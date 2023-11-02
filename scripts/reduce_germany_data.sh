#!/bin/bash

external_programs/osmfilter32 kartendaten/germany-latest.o5m \
	--drop="author" \
	--drop="shop="  \
	--drop="aerialways=" \
	--drop=


	-o=kartendaten/germany_reduced.osm
