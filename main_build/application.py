from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from time import sleep, time
from random import randint

app = Flask(__name__)


@app.route("/")
def index():
    pkmn = []
    pkmn_src = ""
    initial_display = 1

    initial_page = requests.get("https://pikalytics.com/pokedex/gen8ou/")
    soup = BeautifulSoup(initial_page.content, 'html.parser')

    start_time = time()
    sleep(randint(1, 2))
    elapsed_time = time() - start_time

    # first_pkmn = soup.find('a', class_="pokedex_entry").get('href')
    pkmnlist = soup.find_all('a', class_="pokedex_entry", limit=initial_display)

    img_locate = soup.find_all('img', id="header_icon", limit=1)

    for element in pkmnlist:
        start_time = time()
        sleep(randint(1, 2))
        elapsed_time = time() - start_time
        fpokemon = element.get('href')
        pkmn.append(fpokemon)
        print(f"{elapsed_time} seconds")

    for item in img_locate:
        start_time = time()
        sleep(randint(1, 2))
        elapsed_time = time() - start_time
        f_img = item.get('src')
        pkmn_src = f"https://pikalytics.com{f_img}"

    return render_template("index.html", pkmn=pkmn, pkmn_src=pkmn_src)


@app.route("/new-pokemon", methods=["POST"])
def show_new_pokemon():
    pokemon = []
    new_poke = "adda"
    main_poke = "yare"

    initial_page = requests.get("https://pikalytics.com/pokedex/gen8ou/")
    soup = BeautifulSoup(initial_page.content, 'html.parser')
    # soup = BeautifulSoup('<ul class="list gen8ou"></ul>', 'html.parser')

    start_time = time()
    sleep(randint(1, 2))
    elapsed_time = time() - start_time

    next_pkmn = soup.find_all('a', class_="pokedex_entry", limit=1)

    for element in next_pkmn:
        start_time = time()
        sleep(randint(1, 2))
        elapsed_time = time() - start_time
        fpokemon = element.get('href')
        new_poke = fpokemon
        print(f"{elapsed_time} seconds")

    main_poke = main_display_pokemon(new_poke)

    return main_poke


# @app.route("/main_pkmn", methods=["POST"])
def main_display_pokemon(new_poke):
    pkmn = []
    pkmn_name = ""

    page = requests.get(f"https://pikalytics.com{new_poke}")
    soup = BeautifulSoup(page.content, 'html.parser')

    names = soup.find_all('div', class_="inline-block content-div-header-font", limit=1)

    for element in names:
        start_time = time()
        sleep(randint(1, 2))
        elapsed_time = time() - start_time
        fpokemon = element.text.strip()
        pkmn.append(fpokemon)
        pkmn_name = fpokemon
        print(f"{elapsed_time} seconds")

    print(pkmn_name)
    return pkmn_name
