# Content-Based Movie Recommendation System

This is a simple content-based movie recommendation system using TF-IDF and cosine similarity. It takes a short text description of your preferred movies and suggests similar movies from a dataset based on the genre and description.

## Dataset

The dataset used in this system is a CSV file named `movies.csv` from https://github.com/LearnDataSci/articles/blob/master/Python%20Pandas%20Tutorial%20A%20Complete%20Introduction%20for%20Beginners/IMDB-Movie-Data.csv It includes columns such as:

- `Title`: The title of the movie.
- `Genre`: The genre(s) of the movie.
- `Description`: A short description of the movie.


To use this system, you need to ensure that the `movies.csv` file is in the same directory as the script.


### Virtual Environment and Setup
It's recommended to set up a virtual environment for this project to manage dependencies. Use the following commands to create a virtual environment and
install dependencies:

For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
```
### Running the Program
To run the program, use the following command template:

For macOS/Linux:
```bash
python recommend.py "Some user description"
```

### Results
Here is an example of the program running with a sample user query:

```bash
python recommend.py "I like action movies set in space"
```
Output:
```bash 
Top Recommendations:
1. Interstellar (Similarity Score: 0.1172)
2. Independence Day: Resurgence (Similarity Score: 0.1093)
3. Star Trek Beyond (Similarity Score: 0.1022)
```


