import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.widgets import Slider

# Load datasets
hospital_data = pd.read_csv('data\\Capstone\\Hospital_data.csv')
covid_data = pd.read_csv('data\\Capstone\\time_series_covid19_confirmed_US.csv')
airport_data = pd.read_csv('data\\Capstone\\us-airports.csv')

print(hospital_data.columns)
print(covid_data.columns)

# Extract relevant columns from covid_data
covid_data = covid_data[['FIPS', 'Combined_Key', 'Province_State'] + 
                        list(covid_data.columns[11:])]

# Merge hospital_data and covid_data on FIPS code
merged_data = pd.merge(hospital_data, covid_data, on='FIPS', how='inner')

# Convert date columns to datetime objects
date_columns = list(merged_data.columns[11:])
for col in date_columns:
    merged_data[col] = pd.to_datetime(merged_data[col])

# Function to update map based on selected date
def update_map(val):
    date = slider.val
    plt.cla()  # Clear current plot
    
    # Filter data for the selected date
    selected_date = merged_data[['Combined_Key', 'Lat', 'Long_', date.strftime('%m/%d/%Y')]]
    
    # Create a GeoDataFrame from the filtered data
    gdf = gpd.GeoDataFrame(selected_date, geometry=gpd.points_from_xy(selected_date.Long_, selected_date.Lat))
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    
    # Plotting the world map
    ax = world.plot(figsize=(10, 6), color='white', edgecolor='black')
    
    # Plotting COVID-19 cases on the map
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1)
    gdf.plot(ax=ax, cax=cax, marker='o', color='red', markersize=5)
    
    # Set plot title and color bar label
    ax.set_title(f'COVID-19 Cases on {date.strftime("%m/%d/%Y")}')
    cax.set_title('Cases')
    
    plt.show()

# Create initial plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
initial_date = merged_data.columns[-1]  # Use the last date as initial date

# Slider setup
ax_slider = plt.axes([0.15, 0.1, 0.7, 0.03], facecolor='lightgoldenrodyellow')
slider = Slider(ax_slider, 'Date', mdates.date2num(datetime.strptime(initial_date, '%m/%d/%Y')), 
                mdates.date2num(datetime.now()), valinit=mdates.date2num(datetime.now()))

# Update map based on slider value
slider.on_changed(update_map)

# Show initial map
update_map(0)

plt.show()
