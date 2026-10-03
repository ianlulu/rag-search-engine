import argparse
import json


def main() -> None:
    #print("Hello from rag-search-engine!")
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            # print the search query here
            print(f"Searching for: {args.query}")
        case _:
            parser.print_help()

    with open("data/movies.json") as f:
        movie_data = json.load(f)
    results = []

    for movie in movie_data["movies"]:
        if args.query.lower() in movie["title"].lower():
            results.append(movie["title"])

    for i, movie in enumerate(results[:5], start = 1):
        print(f"{i}. {movie}")


if __name__ == "__main__":
    main()
