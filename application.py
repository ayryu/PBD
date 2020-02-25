from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

app = Flask(__name__)


@app.route("/")
def index():
    pokemon = []
    initialpage = requests.get("https://pikalytics.com/pokedex/gen8ou/")

    soup = BeautifulSoup(initialpage.content, 'html.parser')
    # pkmnlist = soup.find_all('span', class_="pokemon-name", limit=1)
    pkmnlist = soup.find_all('a', class_="ss_entry pokedex_entry", limit=2)

    for element in pkmnlist:
        # fpokemon = element.text.strip()
        fpokemon = element.get('href')
        pokemon.append(fpokemon)
    
    return render_template("index.html", pokemon=pokemon)

