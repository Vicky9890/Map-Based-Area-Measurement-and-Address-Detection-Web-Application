# Map Based Area Measurement and Address Detection Web Application


This project is a simple web application that allows users to:

-   Zoom & Draw a polygon area on an interactive map
-   Automatically calculate the area of the drawn shape
-   Detect the approximate address of the selected region

The application is built using **Flask (Python)** for the backend and
**Leaflet.js** for the interactive map on the frontend.


## Features

-   Interactive map interface.
-   Polygon drawing tool.
-   Automatic area calculation in:
    -   Square Meters (m²)
    -   Square Feet (ft²)
-   Reverse geocoding to detect address.
-   Responsive UI design.
-   Error handling for invalid polygons.


## Tech Stack

### Frontend

-   HTML
-   CSS
-   JavaScript
-   Leaflet.js
-   Leaflet Draw Plugin

### Backend

-   Python
-   Flask
-   PyProj (for geodesic area calculation)
-   Requests (for API calls)



## Installation & Setup

### 1. Clone the Repository

``` bash
git clone <your-repo-link>
cd <project-folder>
```

### 2. Create Virtual Environment (Optional but Recommended)

``` bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install Dependencies

``` bash
pip install -r requirements.txt
```




## Running the Application

``` bash
python app.py
```

Then open your browser and go to:

    http://127.0.0.1:5000/


## How It Works

1.  User draws a polygon on the map.
2.  Each Coordinates of polygon are sent to the Flask backend.
3.  Backend:
    -   Calculates area using **pyproj Geod**.
    -   Finds centroid of the polygon.
    -   Sends centroid to OpenStreetMap Reverse Geocoding API.
4.  Address and area are returned to the frontend.
5.  UI updates with results.



## API Used

-   **OpenStreetMap Nominatim Reverse Geocoding API** - for address
    detection.



## Dependencies 

-   Flask
-   pyproj
-   requests

Install using:

``` bash
pip install Flask pyproj requests
```


## Limitations

-   Address detection depends on OpenStreetMap accuracy.
-   Works best for reasonably sized polygons.
-   Internet connection required for reverse geocoding.


## Future Improvements

-   Multiple polygon support.
-   Export area results to PDF/CSV.
-   Improved UI/UX.
-   Support for different units (acres, hectares).

## Output

### First Interface after server run:



### Then after searching for better area:



### Draw polygon over the area:



### Final result with calculated area & address:
 
