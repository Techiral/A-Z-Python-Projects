pip install skyfield
from skyfield.api import load, Topos
from datetime import datetime

# Load planetary ephemerides data
eph = load('de421.bsp')

# Create a date object for a specific date and time
date_time = datetime(2023, 1, 1, 12, 0, 0)

# Set a geographic location (e.g., latitude and longitude of New York City)
new_york = Topos(latitude_degrees=40.7128, longitude_degrees=-74.0060)

# Fetch the positions of the moon and the sun at the specified date and location
ts = load.timescale()
t = ts.utc(date_time.year, date_time.month, date_time.day, date_time.hour, date_time.minute, date_time.second)

earth, moon, sun = eph['earth'], eph['moon'], eph['sun']
topocentric = (earth + new_york).at(t)
astrometric = topocentric.observe(moon).apparent()

# Print the moon's position data
print(f"Date and Time: {date_time}")
print(f"Moon's Azimuth: {astrometric.apparent().altaz()[0].degrees:.2f} degrees")
print(f"Moon's Altitude: {astrometric.apparent().altaz()[1].degrees:.2f} degrees")

