def tracklist(**tracks):
    for artist in tracks:
        print(artist)
        for album, track in tracks[artist].items():
            print('ALBUM: {} TRACK: {}'.format(album, track))


