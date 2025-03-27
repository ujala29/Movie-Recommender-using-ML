# Movie Recommender System

A Streamlit-based movie recommendation system that suggests similar movies based on user input.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/movie-recommender.git
   ```
2. Navigate to the project directory:
   ```
   cd movie-recommender
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
2. The app will open in your default web browser.
3. Select a movie from the dropdown or type a movie name in the text input.
4. Click the "Recommend" button to see the top 10 recommended movies.

## API

The app uses the TMDB (The Movie Database) API to fetch movie poster images. You'll need to provide your own API key in the `app.py` file:

```python
# api key of tmbd= 6a1d1f27bce9b7aa5f3f9dd4b0a723c1
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Testing

No specific testing framework has been set up for this project. You can manually test the app by running it and verifying the recommended movies are accurate.
