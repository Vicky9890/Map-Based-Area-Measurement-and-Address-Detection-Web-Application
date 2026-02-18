from flask import Flask, render_template, request, jsonify
from pyproj import Geod
import requests

app = Flask(__name__)

geod = Geod(ellps="WGS84")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate-area", methods=["POST"])
def calculate_area():
    data = request.json
    coordinates = data.get("coordinates", [])

    if len(coordinates) < 3:
        return jsonify({"error": "Invalid polygon"}), 400

    lats = []
    lngs = []
    for p in coordinates:
        lats.append(p[0])
        lngs.append(p[1])

    area, _ = geod.polygon_area_perimeter(lngs, lats)
    area = abs(area)

    centroid_lat = sum(lats) / len(lats)
    centroid_lng = sum(lngs) / len(lngs)

    try:
        response = requests.get(
            "https://nominatim.openstreetmap.org/reverse",
            params={
                "lat": centroid_lat,
                "lon": centroid_lng,
                "format": "json"
            },
            headers={
                "User-Agent": "MapAreaCalculator/1.0"
            },
            timeout=10
        )
        address = response.json().get("display_name", "Address not found") \
        if response.status_code == 200 else "Address not found"
    except:
        address = "Address lookup failed"

    return jsonify({
        "address": address,
        "area_square_meters": round(area, 2),
        "area_square_feet": round(area * 10.7639, 2)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
