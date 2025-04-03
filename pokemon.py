from flask import Flask, render_template, request, Response, jsonify
from database import (
    get_pokemons,
    random_pokemons_limit,
    show_pokemon,
    search_pokemon,
    increment_count,
    get_count,
)
import matplotlib.pyplot as plt
import matplotlib, japanize_matplotlib
from io import BytesIO

matplotlib.use("Agg")

app = Flask(__name__)


@app.route("/")
def index():
    # 全件取得したい場合
    # pokemons = get_pokemons()
    # ランダム取得したい場合
    pokemons = random_pokemons_limit(30)
    return render_template("index.html", pokemons=pokemons)


@app.route("/show/<int:id>")
def show(id):
    pokemon = show_pokemon(id)
    increment_count(id)  # pokemon['id']
    return render_template("show.html", pokemon=pokemon)


@app.route("/search")
def search():
    name = request.args["name"]
    pokemon = search_pokemon(name)
    increment_count(pokemon["id"])
    return render_template("show.html", pokemon=pokemon)


# @app.route("/ranking")
# def ranking():
#     rankings = get_count()

#     pokemon_names = []
#     pokemon_count = []

#     for ranking in rankings:
#         pokemon_names.append(ranking["name"])

#     for ranking in rankings:
#         pokemon_count.append(ranking["count"])

#     plt.figure(figsize=(10, 6))
#     plt.bar(pokemon_names, pokemon_count, color="skyblue")
#     plt.title("ポケモン検索ランキング")
#     plt.xlabel("ポケモン名")
#     plt.ylabel("検索回数")
#     plt.xticks(rotation=45, ha="right")
#     plt.tight_layout()

#     img = BytesIO()
#     plt.savefig(img, format="png")
#     img.seek(0)
#     plt.close()

#     return Response(img, mimetype="image/png")


@app.route("/ranking")
def ranking():
    rankings = get_count()
    return jsonify([{"name": ranking["name"], "count": ranking["count"]} for ranking in rankings])


if __name__ == "__main__":
    app.run(port=8000, debug=True)
