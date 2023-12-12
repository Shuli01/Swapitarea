import requests

# a) ¿En cuántas películas aparecen planetas cuyo clima sea árido?
response = requests.get('https://swapi.dev/api/planets/')
planets = response.json()['results']
arid_planets = [planet for planet in planets if 'arid' in planet['climate']]
arid_planet_films = sum([len(planet['films']) for planet in arid_planets])
print(f'Planetas con clima árido aparecen en {arid_planet_films} películas.')

# b) ¿Cuántos Wookies aparecen en la sexta película?
response = requests.get('https://swapi.dev/api/films/6/')
film = response.json()
characters = film['characters']
wookies = 0
for character_url in characters:
    character = requests.get(character_url).json()
    if character['species'] and 'Wookie' in character['species'][0]:
        wookies += 1
print(f'Hay {wookies} Wookies en la sexta película.')

# c) ¿Cuál es el nombre de la aeronave más grande en toda la saga?
response = requests.get('https://swapi.dev/api/starships/')
starships = response.json()['results']
largest_starship = max(starships, key=lambda starship: starship['length'])
print(f'La aeronave más grande es {largest_starship["name"]}.')
