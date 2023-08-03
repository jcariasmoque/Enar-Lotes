import pandas as pd
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Cargar los datos desde el archivo Excel
df = pd.read_excel("data.xlsx")

@app.route("/", methods=["GET", "POST"])
def search_name_by_lote():
    if request.method == "POST":
        lote = request.form["lote"]
        result = df.loc[df["lote"] == int(lote), "fecha"].values.tolist()
        if result:
            # Convertir el timestamp a una fecha legible
            fecha_consultada = datetime.fromtimestamp(int(result[0]) / 1e9)
            
            # Obtener la fecha actual
            fecha_actual = datetime.now()

            # Calcular la diferencia de días
            diferencia_dias = (fecha_actual - fecha_consultada).days

            return render_template("result.html", 
                                   result=fecha_consultada.strftime("%Y-%m-%d"),
                                   fecha_actual=fecha_actual.strftime("%Y-%m-%d"),
                                   diferencia_dias=diferencia_dias)
        else:
            return render_template("result.html", result="Lote no encontrado")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
