#Innocentive Challenge: 5D GeoSpatial Analysis

There are 2 pythons files that make up the solution for this challenge
(1)txt2parq.py
Open this file and enter the file path for input .asc file.
Save the file, open command terminal in the folder and run: python txt2parq.py
The output file will be saved in same folder by name 'output.parquet'
(2)five_D_geo_analysis.py
Open this file and enter the file path for input .asc file.
Save the file, open command terminal in the folder and run: 
panel serve --show --port 5009 five_D_geo_analysis.py
Within 1 to 2 minutes(for largest dataset), the Dashboard will be launched and loaded
on a new tab of the web-browser.

Onscreen Filters:
Map Layer: Helps to change the color-shade of the map from the given choices.
D : Physical property dimension given in the dataset.
Intensity : 5th column from dataset.
Lattitude, Longitude: x100000 the original Lat/Long values for correct-geo-plotting.
