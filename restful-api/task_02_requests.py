import requests
import csv


def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post['title'])
        else:
            print('failed to fetch post')


def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()

        structured_post = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        csv_columns = ["id", "title", "body"]

        with open("posts.csv", "w", newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)

        writer.writeheader()

        for post in structured_post:
            writer.writerow(post)

        print("Data has been written to posts.csv successfully.")
    else:
        print("Failed to fetch posts. Status code")


fetch_and_print_posts()
fetch_and_save_posts()