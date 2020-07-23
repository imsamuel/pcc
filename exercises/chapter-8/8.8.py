"""
8-8. User Albums: 
Start with your program from Exercise 8-7. Write a while loop that allows users 
to enter an album’s artist and title. Once you have that information, call 
make_album() with the user’s input and print the dictionary that’s created. Be 
sure to include a quit value in the while loop.
"""


def make_album(artist, title, capacity=None):
    """Return an album using the given properties."""
    album = {"artist": artist, "title": title}
    if capacity:
        album["capacity"] = capacity
    return album


while True:
    title = input("Enter an album's title ('q' to quit): ")
    if title == "q":
        break
    artist = input("Enter the album's artist: ")
    print(make_album(artist, title))
