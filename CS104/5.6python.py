import requests # type: ignore
import json


def get_summary(book, chapter):
    apiUrl = f"https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/{book.lower().replace(' ', '')}/{chapter}"

    response = requests.get(apiUrl)

    # check if it exists
    if response.status_code == 200:
        jsonData = response.json()
        if "chapter" in jsonData:
            return jsonData["chapter"].get("summary", "No summary available.")
        else:
            return "Chapter not found."
    else:
        return "Book or chapter not found."


def main():
    print("Welcome to the Book of Mormon Summary Tool!")

    while True:

        book = input("Which book of the Book of Mormon would you like? ").strip()

        chapter = input(f"Which chapter of {book} are you interested in? ").strip()

        summary = get_summary(book, chapter)

        print(f"Summary of {book} chapter {chapter}:")
        print(summary)

        # Ask the user if they want to view another summary
        another = input("Would you like to view another (Y/N)? ").strip().upper()

        if another != "Y":
            break

    print("Thank you for using Book of Mormon Summary Tool!")


# Run the main function
if __name__ == "__main__":
    main()
