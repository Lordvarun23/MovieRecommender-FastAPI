# Movie Recommendation System with FastAPI

This project is a simple movie recommendation system built using **FastAPI** as the backend, with a collaborative filtering recommendation approach using cosine similarity. The system recommends movies based on a user's input and provides a cool, aesthetic custom UI using HTML and CSS.

## Features

- Search for a movie from the dataset.
- Get recommendations for similar movies based on a selected movie.
- Aesthetic and interactive custom frontend.
- FastAPI backend for high-performance APIs.
- Simple and easy-to-deploy structure.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Frontend](#frontend)
- [Deployment](#deployment)
- [Technologies Used](#technologies-used)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/movie-recommendation-system.git
    cd movie-recommendation-system
    ```

2. **Set up a virtual environment (optional but recommended)**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Download MovieLens dataset**:
   Download the necessary dataset files (`movies.csv` and `ratings.csv`) and place them in the root directory. You can download them from [MovieLens](https://grouplens.org/datasets/movielens/).

## Usage

1. **Run the FastAPI server**:

    ```bash
    uvicorn main:app --reload
    ```

    The app will be available at `http://127.0.0.1:8000`.

2. **Access the Frontend**:

    Open a web browser and visit `http://127.0.0.1:8000/` to access the custom UI.

## API Endpoints

1. **Movie Recommendations**:
   - **Endpoint**: `/recommend/{movie_name}`
   - **Method**: GET
   - **Description**: Returns a list of movie recommendations based on the input movie.
   - **Example**: `http://127.0.0.1:8000/recommend/Inception`

2. **Search for Movies**:
   - **Endpoint**: `/movies/`
   - **Method**: GET
   - **Query Parameter**: `query` (the movie name or part of it)
   - **Description**: Searches for movies matching the input query.
   - **Example**: `http://127.0.0.1:8000/movies/?query=toy`

## Frontend

The UI is served from the FastAPI app and located in the `static/` directory. It includes:

- **index.html**: The main HTML page.
- **styles.css**: Custom CSS for a visually appealing UI.
- **script.js**: JavaScript for making API calls to fetch and display movie data.

### Directory Structure

```bash
├── main.py               # FastAPI application
├── movies.csv            # MovieLens dataset (movies)
├── ratings.csv           # MovieLens dataset (ratings)
├── requirements.txt       # Python dependencies
├── static/
│   ├── index.html         # Frontend HTML file
│   ├── styles.css         # CSS for styling
│   └── script.js          # JavaScript for client-side interactions
└── README.md             # Project documentation
