from flask import Flask, jsonify, render_template, request
import pandas as pd

app = Flask(__name__)

# Cargar la base de datos de recetas (asegúrate de poner la ruta correcta)
url = "https://raw.githubusercontent.com/TU_USUARIO/TU_REPO/main/conversacion_recetas.csv"
df = pd.read_csv(url, encoding="utf-8", sep=";")
  
print(df.head())    # Esto imprimirá las primeras 5 filas del DataFrame


@app.route("/")
def index():
    return render_template("index.html", recetas=df.to_dict(orient="records"))

@app.route("/buscar", methods=["GET"])
def buscar():
    consulta = request.args.get("q", "").lower()
    if consulta:
        resultados = df[df["Título"].str.lower().str.contains(consulta, na=False)]
    else:
        resultados = df
    return jsonify(resultados.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)

