# Steffi Hung
# GIS: Programming and Automation
# Fall 2021
# Lab 3

#

# IMPORT ALL THE THINGS!
import fiona
import random

import geopandas as gpd

from shapely.geometry.polygon import Point

#

# Create directories
sp = './lab3.gpkg'
lr = fiona.listlayers(sp)

#

# Read in files
huc08_gdf = gpd.read_file(sp, layer = lr[0])
huc12_gdf = gpd.read_file(sp, layer = lr[1])
aws_gdf = gpd.read_file(sp, layer = lr[2])

#

random.seed(0)

#

def get_samples(huc_gdf, wsName):

    """
    Runs lab 3. 
    huc_gdf should be one of the watershed gdfs from above
    wsName should be the name of the watershed for print statements and should be placed in quotes
    """

    print(f"Getting samples for {wsName}.")
    pnt_samps = {'huc': [], 'geometry': []}
    hcrs = huc_gdf.crs
    col = [column for column in huc_gdf.columns if 'HUC' in column][0]

    for idx, row in huc_gdf.iterrows():
        poly_bx = row.geometry.bounds
        poly_ex = {
            'minx': poly_bx[0], 
            'miny': poly_bx[1], 
            'maxx': poly_bx[2], 
            'maxy': poly_bx[3]
            }
        area = row.geometry.area
        sqkm = 1000000
        dns = (0.05 * area) / sqkm 
        mid = 0

        while mid < dns:
            pnt = Point(
                random.uniform(
                    poly_ex['minx'], 
                    poly_ex['maxx']
                ), 
                random.uniform(
                    poly_ex['minx'], 
                    poly_ex['maxy']
                )
            )

            if pnt.within(row.geometry):
                pnt_samps['huc'].append(row[col][:8])
                pnt_samps['geometry'].append(pnt)
                mid += 1

    ps_gdf = gpd.GeoDataFrame(pnt_samps, crs=hcrs)

    ps_aws = gpd.overlay(ps_gdf, aws_gdf, how='intersection')

    summ = ps_aws.groupby(by='huc').mean()

    for idx, row in summ.iterrows():
        rnd_s = round(row['aws0150'], 2)
        print(f"The {wsName} sampling of aws0150 for watershed {idx} was {rnd_s}.")
    print(f"Finished getting samples for {wsName}")

#

get_samples(huc08_gdf, 'HUC 08')
get_samples(huc12_gdf, 'HUC 12')
