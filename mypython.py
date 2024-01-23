import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import pandas as pd
import numpy as np

# Generate random data
np.random.seed(42)
n_points = 50
data = pd.DataFrame({
    'latitude': np.random.uniform(-90, 90, n_points),
    'longitude': np.random.uniform(-180, 180, n_points),
    'value': np.random.randint(1, 100, n_points)
})

# Create a GeoDataFrame from the DataFrame
geometry = [Point(lon, lat) for lon, lat in zip(data['longitude'], data['latitude'])]
geo_df = gpd.GeoDataFrame(data, geometry=geometry, crs='EPSG:4326')

# Download world map shapefile from GeoPandas datasets
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Plot the world map
fig, ax = plt.subplots(figsize=(10, 6))
world.plot(ax=ax, color='lightgray')

# Plot the data points on the map
geo_df.plot(ax=ax, markersize=data['value'], color='red', alpha=0.7, legend=True)

# Customize the plot
plt.title('Data Visualization on Map')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()