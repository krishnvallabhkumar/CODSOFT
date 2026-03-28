
movies_db = [
    {"title": "The Dark Knight", "genres": ["Action", "Crime", "Drama"]},
    {"title": "Inception", "genres": ["Action", "Adventure", "Sci-Fi"]},
    {"title": "The Matrix", "genres": ["Action", "Sci-Fi"]},
    {"title": "The Godfather", "genres": ["Crime", "Drama"]},
    {"title": "Pulp Fiction", "genres": ["Crime", "Drama"]},
    {"title": "Toy Story", "genres": ["Animation", "Adventure", "Comedy"]},
    {"title": "The Lion King", "genres": ["Animation", "Adventure", "Drama"]},
    {"title": "Interstellar", "genres": ["Adventure", "Drama", "Sci-Fi"]},
    {"title": "Gladiator", "genres": ["Action", "Adventure", "Drama"]},
    {"title": "Spirited Away", "genres": ["Animation", "Adventure", "Family"]},
    {"title": "Parasite", "genres": ["Comedy", "Drama", "Thriller"]},
    {"title": "Avengers: Endgame", "genres": ["Action", "Adventure", "Sci-Fi"]}
]

def calculate_similarity(genres1, genres2):
    """Calculates Jaccard Similarity between two sets of genres."""
    set1 = set(genres1)
    set2 = set(genres2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)

def get_recommendations(user_movie):
    target_movie = next((m for m in movies_db if m["title"].lower() == user_movie.lower()), None)
    
    if not target_movie:
        return None

    scores = []
    for movie in movies_db:
        if movie["title"].lower() != user_movie.lower():
            score = calculate_similarity(target_movie["genres"], movie["genres"])
            scores.append((movie["title"], score, movie["genres"]))
    
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:3]  

def main():
    print("Welcome to the Simple Movie Recommendation System!")
    print("Available movies in our database:")
    for m in movies_db:
        print(f"- {m['title']}")
    
    while True:
        user_input = input("\nEnter a movie you like from the list above (or 'exit' to quit): ").strip()
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
            
        recommendations = get_recommendations(user_input)
        
        if recommendations:
            print(f"\nBecause you liked '{user_input}', you might also like:")
            for title, score, genres in recommendations:
                if score > 0:
                    print(f"- {title} (Similarity Score: {score:.2f}, Genres: {', '.join(genres)})")
                else:
                    print(f"- {title} (General Recommendation, Genres: {', '.join(genres)})")
        else:
            print("Sorry, that movie is not in our database. Please try another one.")

if __name__ == "__main__":
    main()