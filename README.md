# GmE 205 – Laboratory 7  
## From PostGIS to REST API to GIS Clients

# Laboratory Overview

This laboratory focused on creating a complete spatial data pipeline using PostGIS, Flask REST API, GeoJSON, and QGIS. Spatial data stored in PostGIS was accessed through Python and served as GeoJSON using Flask API endpoints. The GeoJSON services were then loaded into QGIS as GIS client layers.

The workflow implemented in this laboratory is:

```text
PostGIS Database
↓
Flask REST API
↓
GeoJSON Response
↓
QGIS Client
```

---

# Technologies Used

- Python
- Flask
- Flask-CORS
- PostgreSQL
- PostGIS
- psycopg2
- python-dotenv
- QGIS
- GitHub

# Folder Structure

```text
gme205-lab7
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── test_connection.py
│   └── .env
├── screenshots/
├── .gitignore
├── README.md
└── requirements.txt
```

# Required Screenshots

The following screenshots are included in the `screenshots/` folder:

1. Parcel table in PostGIS  
2. Roads table in PostGIS  
3. Flask root endpoint  
4. /api/parcels GeoJSON output  
5. /api/roads GeoJSON output  
6. Parcel API layer in QGIS  
7. Roads API layer in QGIS  
8. Attribute table of one API layer  
9. Styled parcel layer  

# README Reflection Questions

## 1. What role does PostGIS play in this architecture?

PostGIS serves as the spatial database where the parcel and road geometries are stored together with their attributes. It provides the spatial functions needed to manage and query GIS data.

## 2. What role does Flask play in this laboratory?

Flask acts as the REST API service that connects the PostGIS database to GIS clients. It retrieves spatial data and returns it as GeoJSON through API endpoints.

## 3. Why is GeoJSON useful for spatial web services?

GeoJSON is useful because it is lightweight, easy to read, and widely supported by GIS software and web applications. It allows spatial data to be transferred easily over the web.

## 4. How does ST_AsGeoJSON() support distributed GIS?

`ST_AsGeoJSON()` converts spatial geometries from PostGIS into GeoJSON format so they can be shared through web services and accessed by different GIS clients remotely.

## 5. Why is QGIS considered a heavy client?

QGIS is considered a heavy client because it performs processing, rendering, analysis, and visualization locally on the user’s machine instead of relying only on the server.

## 6. Why is a REST API better than manually exporting shapefiles?

A REST API allows users to access updated spatial data directly from the source without repeatedly exporting files manually. It also supports real-time sharing and easier interoperability.

## 7. How does this laboratory demonstrate distributed geospatial computing?

This laboratory demonstrates distributed geospatial computing because the database, API server, and GIS client work as separate systems that communicate with each other through network services.

## 8. What advantages does service-based GIS architecture provide?

Service-based GIS architecture improves interoperability, centralized data management, accessibility, and scalability because multiple applications can access the same services.

## 9. How does this architecture support scalability in spatial systems?

This architecture supports scalability because additional users, datasets, and GIS applications can connect to the same API services without changing the overall system structure.

# Repository Link

https://github.com/alzulueta/gme205-lab7