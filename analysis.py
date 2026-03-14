
'''METEORITE LANDINGS ANALYSIS'''

#import json  #for handling JSON data from the downloaded dataset.
import requests 
from collections import Counter 

# This function performs the analysis of the meteorite landings.
def analysis():
    url = "https://dmachek.github.io/meteorites-homework/meteorite_landings.json"

    # It loads the JSON data 
    data = requests.get(url).json()  
    # calculate the total number of entries
    all_entries = len(data) 

    # To find the most massive meteorite
    max_mass = 0
    max_mass_name = ""

    # Some masses may be missing, so filtering will be a good idea.
    for meteorite in data:
        try:
            # Converting mass to float, if it fails, it will be detected by the exception block.
            mass = float(meteorite.get("mass", 0))
            if mass > max_mass:
               max_mass = mass
               max_mass_name = meteorite.get("name", "Unknown")
        except ValueError:
            continue

    # Finding the most frequent year of meteorite landings.
    years = []
    for meteorite in data:
        year_str = meteorite.get("year")
        if year_str:
            # Some years may include time, keep only the year part will be easy for counting.
            year_only = year_str.split("-")[0]
            if year_only.isdigit():
                years.append(int(year_only))

    # Count frequency of each year and find the most common one.
    year_counts = Counter(years)
    most_common_year, counts = year_counts.most_common(1)[0]

    # Printing the overall results.
    print(f"Total number of entries: {all_entries}") 
    print(f"Name and mass of the most massive meteorite: {max_mass_name} , Mass: {max_mass} g")
    print(f"Most frequent year: {most_common_year} , {counts} entries")

#calling the function to perform the action.
analysis()
