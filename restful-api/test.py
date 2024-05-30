#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    grab = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status code: {grab.status_code}")
    """We call the built-in status_code that comes with the requests library."""

    if grab.status_code == 200:
        posts = grab.json()
        for data in posts:
            print(data["title"])
    else:
        print("Error fetching posts.")


def fetch_and_save_posts():
    url = requests.get("https://jsonplaceholder.typicode.com/posts")
    if url.status_code == 200:
        posts = url.json()

        structured_data = [
            {"id": data["id"], "title": data["title"], "body": data["body"]}
            for data in posts
        ]

        csv_list = ["id", "title", "body"]

        with open("posts.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_list)
            writer.writeheader()
            for post in structured_data:
                writer.writerow(post)

        print("The data has been written to posts.csv successfully.")
    else:
        print(f"Error fetching data. Status code: {url.status_code}")


"""Here we print the first function to fetch the posts successfully."""
fetch_and_print_posts()
fetch_and_save_posts()
