country = input("Type a country name. ").lower()# Add country name
visits = int(input("How many times have you visited? ")) # Number of visits
list_of_cities = eval(input("How many cities in the country have you visited? Separate them with a comma please. ")) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(country_add,visits_add, list_of_cities_add):
  travel_log.append({
    "country": country_add,
    "visits": visits_add,
    "cities": list_of_cities_add
  })

# Do not change the code below 👇
add_new_country(country_add= country, visits_add= visits, list_of_cities_add= list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city is {travel_log[2]['cities'][1]}.")