
import requests


def fetch_posts():
    """Fetch posts from the API."""
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        posts = response.json()

        if not isinstance(posts, list):
            print("Unexpected API data format.")
            return []

        print(f"Successfully fetched {len(posts)} posts!")
        return posts

    except requests.exceptions.RequestException as error:
        print("Failed to fetch posts:", error)
        return []


def show_user_counts(posts):
    """Count the number of posts belonging to each user."""
    user_counts = {}

    for post in posts:
        user_id = post["userId"]
        user_counts[user_id] = user_counts.get(user_id, 0) + 1

    print("\n--- Posts Per User ---")

    for user_id, count in sorted(user_counts.items()):
        print(f"User {user_id}: {count} posts")


def filter_by_user(posts):
    """Display posts belonging to a selected user."""
    try:
        user_id = int(input("Enter user ID (1-10): "))

        matching_posts = [
            post for post in posts
            if post["userId"] == user_id
        ]

        if matching_posts:
            print(f"\nFound {len(matching_posts)} posts:")
            for post in matching_posts:
                print(f'{post["id"]}: {post["title"]}')
        else:
            print("No matching posts found.")

    except ValueError:
        print("Please enter a valid integer.")


def search_by_keyword(posts):
    """Search post titles using a keyword."""
    keyword = input("Enter a keyword: ").strip().lower()

    if not keyword:
        print("Keyword cannot be empty.")
        return

    matching_posts = []

    for post in posts:
        title = post["title"].lower()

        if keyword in title:
            matching_posts.append(post)

    if matching_posts:
        print(f"\nFound {len(matching_posts)} matching posts:")
        for post in matching_posts:
            print(f'{post["id"]}: {post["title"]}')
    else:
        print("No matching posts found.")


def main():
    posts = fetch_posts()

    if not posts:
        print("No posts available. Please check the API connection.")
        return

    while True:
        print("\n===== API DATA ANALYZER =====")
        print("1. Show total posts")
        print("2. Show posts per user")
        print("3. Filter posts by user ID")
        print("4. Search posts by keyword")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            print("Total posts:", len(posts))

        elif choice == "2":
            show_user_counts(posts)

        elif choice == "3":
            filter_by_user(posts)

        elif choice == "4":
            search_by_keyword(posts)

        elif choice == "5":
            print("Thank you for using API Data Analyzer!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
