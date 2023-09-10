import folium

# Create a map centered at a certain location (e.g., Tucson, Arizona)
m = folium.Map(location=[32.2226, -110.9747], zoom_start=5)

# List of locations and coordinates
locations = {
    
    "Nacogdoches, Texas": {
        "coords": [31.6035, -94.6554],
        "note": "Kid meets the Judge and Toadvine."
    },
    
    "Bexar, Texas (San Antonio)": {
        "coords": [29.4241, -98.4936],
        "note": "The Kid meets Sgt Captain White who wants to raid Sonora."
    },

    "Castroville, Texas (west of San Antonio)": {
        "coords": [29.3551, -98.8786],
        "note": "First town Kid and Capt. White's filibusters pass through before soldiers start dying"
    },
    

    "Plain of pumice stone (estimated)": {
        "coords": [27.0, -101.707],
        "note": "Where the filibusters start dying from disease, then are annihilated by the Comanche."
    },

    "Bolson de Mapimi": {
        "coords": [26.5, -103.0],
        "note": "Where Kid meets up with 8 survivors of the Comanche battle."
    },

    "Small towns in chapter 5 (estimated)": {
        "coords": [27, -103.5],
        "note": "Near to where Kid sees aftermath of Comanche massacre and is arrested."
    },
      
    "Chihuahua City, Mexico": {
        "coords": [28.6353, -106.0889],
        "note": "Kid, arrested, meets Toadvine again, and is recruited into Glanton's gang."
    },

    "Corralitos, fictional town, and camp near Casas Grandes river (estimated)": {
        "coords": [28.5, -106.8],
        "note": "Glanton's gang stays with the Governor, allows a magician family to trail them, and sees a massacre of Apaches."
    },
    
    "Janos": {
        "coords": [31.433, -108.3833],
        "note": "Glanton shoots an Apache woman and Juan Miguel (McGill) scalps her. Nearby they find an Apache meat camp."
    },

    "lake of gypsum": {
        "coords": [32.7799, -106.3257],
        "note": "Horses go blind from sunlight."
    },

    "area near (presumed) San Andres Mountains (estimated)": {
        "coords": [33.0, -107.0],
        "note": "Glanton gang finds four survivors of Apache attack and a young mute boy, who is later killed (presumably by the Judge)."
    },

    "Villages of the Gillenos (estimated 120 miles south of gypsum)": {
        "coords": [31.7799, -106],
        "note": "Massacre of the Gilenos."
    },

    "Town of Gallego (estimated)": {
        "coords": [30.0, -107.0],
        "note": "Skirmishes with the Apaches before arriving in Chihuaha City."
    },

    "Chihuahua City, Mexico": {
        "coords": [28.6353, -106.0889],
        "note": "Gang is invited to a feast at governor's home, then degrade into a multi-day debauchery."
    },
      
    "Coyame": {
        "coords": [29.9119, -104.1551],
        "note": "Gang stays for three days, all the while abusing the locals."
    },

    "Three days south of Hueco Tanks (estimated)": {
        "coords": [30.0, -106.0],
        "note": "Gang slaughters the Tiguas."
    },

    "Carrizal": {
        "coords": [28.3950, -105.3403],
        "note": "Ruined town the gang passes through."
    },

    "Chihuahua City, Mexico": {
        "coords": [28.6353, -106.0889],
        "note": "Gang comes back but is promptly escorted out of town by Mexican soldiers."
    },

    "Nacori (estimated)": {
        "coords": [29.610, -109.0203],
        "note": "Village the gang passes through, they will return in a month and slaughter everyone in the area.\n This first time, they get into a fight and kill and scalp 40 Mexicans"
    },

    "site of battle with Mexican soldiers": {
        "coords": [29.0, -107.2],
        "note": "Gang after killing Mexican soldiers hunts down the rest to prevent them from telling Chihuahua City."
    },

    "Chihuahua City, Mexico": {
        "coords": [28.6353, -106.0889],
        "note": "Gang is paid out (unwittingly) for scalps of Mexican soldiers. Then a bounty is issued for Galnton's head a week later."
    },

    "Jesus Maria (estimated)": {
        "coords": [28.6, -106.8],
        "note": "Gang debauches themselves until multiple shootouts break out, killing several members."
    },

    "Ures": {
        "coords": [29.433, -110.4034],
        "note": "Now Dec 2, 1849, gang gets another contract to hunt Apache."
    },

    "Mountains where snow is falling (estimated)": {
        "coords": [29.7, -109.0],
        "note": "Kid is chased and shot at by the Mexican army."
    },

    "Mountains where snow is falling (estimated)": {
        "coords": [29.7, -109.0],
        "note": "Kid is chased and shot at by the Mexican army."
    },

    "Santa Cruz (estimated)": {
        "coords": [31.1211, -110.9443],
        "note": "Quick overnight stay."
    },

    "San José de Tumacacori": {
        "coords": [31.5568, -111.0481],
        "note": "The finds two hermits, killing one."
    },

    "Tucson": {
        "coords": [32.2226, -110.9747],
        "note": "After encountering Apache and injuring a horse, the gang goes to Tucson for Whiskey and encounters the 'imbecile'.\n The gang kills a barman, and a young girl is kidnapped and murdered (again, presumably by the judge)"
    },

    "Colorado River crossing point (estimated)": {
        "coords": [33.0, -115.0],
        "note": "Gang conspires with Yuma to take the crossing, then betray and kill the Yuma, enslave Sonorans. Then Yuma finally annihilate the gang, including Glanton himself."
    },

    "Alamo Mucho (estimated)": {
        "coords": [31.0, -116.0],
        "note": "Kid and Tobin fight off the Apache, then encounter the judge and the imbecile."
    },

    "San Felipe (estimated)": {
        "coords": [31.02, -114.8366],
        "note": "Campf of the Diegueño Indians, who feed the Kid and Tobin"
        
    },
    
    "San Diego": {
        "coords": [32.7157, -117.1611],
        "note": "Final stop for Kid and Tobin. Kid, arrested, converses with the Judge. Then he is released by bribing a corporal."
    },

    "Los Angeles": {
        "coords": [34.0522, -118.2437],
        "note": "In his last scene as the Kid, Kid sees Toadvine and Davy Brown hanged. He buys Brown's ear necklace"
    },
}


# Create a list to store the coordinates for the trail
trail_coords = []

# Add markers and trail coordinates for each location
for location_index, (location_name, info) in enumerate(locations.items(), start=1):
    coords = info["coords"]  # Extract coordinates from the dictionary
    note = info["note"]      # Extract note from the dictionary
    trail_coords.append(coords)  # Add coordinates to the trail
    
    # Add marker for each location
    marker = folium.Marker(coords, tooltip=location_name, popup=f"{location_index}: {note}", parse_html=True)
    marker.add_to(m)

# Draw the trail line using PolyLine with options
folium.PolyLine(
    locations=trail_coords,
    color="blue",          # Line color
    weight=2,              # Line weight
    opacity=0.9,           # Line opacity (0 to 1)
    dash_array="5, 5",     # Dash pattern (length of dashes and gaps)
).add_to(m)

# Save the map to an HTML file
m.save("trail_map_with_options.html")

print("Map saved as 'trail_map_with_options.html'")