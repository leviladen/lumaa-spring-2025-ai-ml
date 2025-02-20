import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import argparse

def load_dataset():
    # Load the dataset and concatenate genre and description for each movie
    dataset = pd.read_csv("movies.csv")
    dataset["text"] = dataset["Genre"] + " " + dataset["Description"] 
    return dataset

def recommend_movies(user_query, dataset, top_n=3):
    # Use TF-IDF to vectorize the text data
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2))  
    tfidf_matrix = vectorizer.fit_transform(dataset["text"])
    user_tfidf = vectorizer.transform([user_query])
    # Calculate cosine similarity between user input and all movies
    similarities = cosine_similarity(user_tfidf, tfidf_matrix).flatten()
    # Sort the movies by similarity score
    top_indices = similarities.argsort()[-top_n:][::-1]
    recommendations = dataset.iloc[top_indices]
    # Return the top recommendations and their similarity scores
    return recommendations, similarities[top_indices]

def main():
    # Parse command-line arguments and load the dataset
    parser = argparse.ArgumentParser(description="Content-Based Movie Recommendation System")
    parser.add_argument("query", type=str, help="User input description of preferred movies.")
    args = parser.parse_args()
    dataset = load_dataset()
    # Get the top movie recommendations
    recommendations, scores = recommend_movies(args.query, dataset)
    # Print the top recommendations and their similarity scores
    print("Top Recommendations:")
    for idx, (title, score) in enumerate(zip(recommendations["Title"], scores)):
        print(f"{idx+1}. {title} (Similarity Score: {score:.4f})")

if __name__ == "__main__":
    main()

