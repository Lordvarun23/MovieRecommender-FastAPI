from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import pandas as pd


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

movie_ratings = pd.merge(ratings, movies, on='movieId')

user_movie_matrix = movie_ratings.pivot_table(index='userId', columns='title', values='rating')
user_movie_matrix.fillna(0, inplace=True)

# Calculate movie similarity
similarity_matrix = cosine_similarity(user_movie_matrix.T)
movie_sim_df = pd.DataFrame(similarity_matrix, index=user_movie_matrix.columns, columns=user_movie_matrix.columns)

# API to get recommendations
@app.get("/recommend/{movie_name}")
async def recommend_movies(movie_name: str):
    if movie_name not in movie_sim_df.columns:
        print(movie_name)
        print(user_movie_matrix.columns)
        raise HTTPException(status_code=404, detail="Movie not found")
    print(movie_name)
    print(user_movie_matrix.columns)
    similar_movies = movie_sim_df[movie_name].sort_values(ascending=False)[1:11]
    return {"recommendations": similar_movies.to_dict()}

# API to search for a movie
@app.get("/movies/")
async def search_movies(query: str):
    results = movies[movies['title'].str.contains(query, case=False, na=False)]
    if results.empty:
        raise HTTPException(status_code=404, detail="No movies found")
    return results[['movieId', 'title', 'genres']].to_dict(orient="records")

# Serve the HTML file
@app.get("/", response_class=HTMLResponse)
async def serve_homepage():
    with open("static/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
