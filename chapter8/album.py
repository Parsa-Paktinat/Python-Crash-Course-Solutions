def make_album(artist_name, album_title, number_of_songs=None):
    """Returns a ditionary about this album."""
    album = {'Artist': artist_name.title(), 'Title': album_title.title()}
    if number_of_songs:
        album['Number of songs'] = number_of_songs
    return album

album1 = make_album('Tataloo', 'Jahannam')
album2 = make_album('Bahram', 'Sokoot')
album3 = make_album('MR Shajarian', 'Zemestan')
album4 = make_album('Moer', "Taassob", 4)
album5 = make_album('Tataloo', '78', 25)
print(album1)
print(album2)
print(album3)
print(album4)
print(album5)
