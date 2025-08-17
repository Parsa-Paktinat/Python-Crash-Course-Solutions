def make_album(artist_name, album_title, number_of_songs=None):
    """Returns a ditionary about this album."""
    album = {'Artist': artist_name.title(), 'Title': album_title.title()}
    if number_of_songs:
        album['Number of songs'] = number_of_songs
    return album

while True:
    print("Enter your album artist and name:")
    print("(Enter 'q' to quit)")

    a_artist = input("Enter album artist: ")
    if a_artist == "q":
        break

    a_title = input("Enter album title: ")
    if a_title == "q":
        break

    album = make_album(a_artist, a_title)
    print(f"\nYour album dictionary:\n{album}\n")