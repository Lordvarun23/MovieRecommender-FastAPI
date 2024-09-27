const API_BASE_URL = 'http://127.0.0.1:8000';

async function searchMovie() {
    const query = document.getElementById('movieInput').value;
    if (!query) return;

    try {
        const response = await fetch(`${API_BASE_URL}/movies/?query=${query}`);
        const data = await response.json();

        displaySearchResults(data);
    } catch (error) {
        console.error('Error fetching search results:', error);
    }
}

async function getRecommendations() {
    const movie = document.getElementById('recommendInput').value;
    if (!movie) return;

    try {
        const response = await fetch(`${API_BASE_URL}/recommend/${movie}`);
        const data = await response.json();

        displayRecommendations(data.recommendations);
    } catch (error) {
        console.error('Error fetching recommendations:', error);
    }
}

function displaySearchResults(results) {
    const searchResultsDiv = document.getElementById('searchResults');
    searchResultsDiv.innerHTML = '';

    results.forEach(movie => {
        const movieCard = document.createElement('div');
        movieCard.classList.add('movie-card');
        movieCard.innerHTML = `
            <h3>${movie.title}</h3>
            <p>${movie.genres}</p>
        `;
        searchResultsDiv.appendChild(movieCard);
    });
}

function displayRecommendations(recommendations) {
    const recommendResultsDiv = document.getElementById('recommendResults');
    recommendResultsDiv.innerHTML = '';

    Object.keys(recommendations).forEach(movie => {
        const movieCard = document.createElement('div');
        movieCard.classList.add('movie-card');
        movieCard.innerHTML = `
            <h3>${movie}</h3>
            <p>Similarity Score: ${recommendations[movie].toFixed(2)}</p>
        `;
        recommendResultsDiv.appendChild(movieCard);
    });
}
