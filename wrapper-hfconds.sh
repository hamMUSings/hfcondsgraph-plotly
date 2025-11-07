#!/bin/bash
while $true:

do
	./hfconds-get-format.sh
	python3 sunburst-conds.py
	magick ./output/hfconds.png  -gravity Center -crop 700x394+0+0 +repage ./output/rwb_1.png
	magick mogrify -format jpg ./output/rwb_1.png
	rm ./output/rwb_1.png
	python3 space_weather_conds.py
	sleep 1h
done
