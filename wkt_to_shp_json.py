import pandas as pd
import geopandas as gpd
import shapely.wkt as wkt
import csv
import os
import sys
import shutil

csv.field_size_limit(1000000)

filename = 'C:/Kartografi_Jesper/Python/veger_under_konstruksjon/new_geometry.csv'
if not os.path.isfile(filename):
    print("Error: new_geometry.csv not found.")
    sys.exit()

with open(filename) as f:
    first_line = f.readline().strip()

if not first_line:
    print("Error: new_geometry.csv is empty. This is most likely due to no new geometry since last execution of script.")
    sys.exit()

df = pd.read_csv(filename, delimiter=",", header=None)
df.columns = ['WKT', 'typeVeg', 'Kategori', 'Vegnummer']  # assign column names
df['geometry'] = df['WKT'].apply(wkt.loads)
gdf = gpd.GeoDataFrame(df, geometry='geometry')
gdf.crs = 'epsg:25833'

filename = 'C:/Kartografi_Jesper/Python/veger_under_konstruksjon/new_geometry.shp'
if os.path.isfile(filename):
    print("Warning: Existing file has been overwritten:", filename)

gdf.to_file(filename, driver='ESRI Shapefile')

# Delete the "data.csv" and "data_cleaned.csv" files
if os.path.isfile('C:\Kartografi_Jesper\Python\veger_under_konstruksjon\data_json_lastmonth.csv'):
    os.remove('C:\Kartografi_Jesper\Python\veger_under_konstruksjon\data_json_lastmonth.csv')
cleaned_file = 'C:\Kartografi_Jesper\Python\veger_under_konstruksjon\data_json.csv'
if os.path.isfile(cleaned_file):
    shutil.move(cleaned_file, 'C:\Kartografi_Jesper\Python\veger_under_konstruksjon\data_json_lastmonth.csv')
