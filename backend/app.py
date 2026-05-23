from flask import Flask, jsonify, Response
from flask_cors import CORS
from database import get_connection
import json

app = Flask(__name__)
CORS(app)

def geojson_response(geojson_data):
    return Response(
        json.dumps(geojson_data, indent=4),
        mimetype="application/geo+json"
    )

@app.route("/")
def home():
    return jsonify({
        "message": "GmE 205 Laboratory 7 Flask API is running.",
        "available_endpoints": [
            "/api/parcels",
            "/api/parcels.geojson",
            "/api/roads",
            "/api/roads.geojson",
            "/api/layers"
        ],
        "qgis_recommended_endpoints": [
            "http://127.0.0.1:5000/api/parcels.geojson",
            "http://127.0.0.1:5000/api/roads.geojson"
        ]
    })

@app.route("/api/layers")
def get_layers():
    return jsonify({
        "layers": [
            {
                "name": "parcels",
                "endpoint": "/api/parcels.geojson",
                "geometry_type": "MultiPolygon",
                "crs": "EPSG:4326"
            },
            {
                "name": "roads",
                "endpoint": "/api/roads.geojson",
                "geometry_type": "MultiLineString",
                "crs": "EPSG:4326"
            }
        ]
    })

@app.route("/api/parcels")
@app.route("/api/parcels.geojson")
def get_parcels():
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT
            ASS_ACTUAL,
            ASS_CLASSI,
            ST_AsGeoJSON(ST_Force2D(geom)) AS geometry
        FROM parcels;
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        features = []

        for row in rows:
            feature = {
                "type": "Feature",
                "properties": {
                    "ASS_ACTUAL": row[0],
                    "ASS_CLASSI": row[1]
                },
                "geometry": json.loads(row[2])
            }
            features.append(feature)

        geojson = {
            "type": "FeatureCollection",
            "name": "parcels",
            "features": features
        }

        return geojson_response(geojson)

    except Exception as error:
        return jsonify({
            "error": "Failed to load parcel data.",
            "details": str(error)
        }), 500

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

@app.route("/api/roads")
@app.route("/api/roads.geojson")
def get_roads():
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT
            R_CLASS,
            S_Type,
            "road condi",
            ST_AsGeoJSON(ST_Force2D(geom)) AS geometry
        FROM roads;
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        features = []

        for row in rows:
            feature = {
                "type": "Feature",
                "properties": {
                    "R_CLASS": row[0],
                    "S_Type": row[1],
                    "ROAD_CONDI": row[2]
                },
                "geometry": json.loads(row[3])
            }
            features.append(feature)

        geojson = {
            "type": "FeatureCollection",
            "name": "roads",
            "features": features
        }

        return geojson_response(geojson)

    except Exception as error:
        return jsonify({
            "error": "Failed to load road data.",
            "details": str(error)
        }), 500

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    app.run(debug=True)