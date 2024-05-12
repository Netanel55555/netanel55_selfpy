def my_mp4_playlist(file_path, new_song):
    file = open(file_path, "r+")
    mp3_data = file.read()
    mp3_lines = mp3_data.split("\n")
    add_lines = 0

    mp3_items = []
    for element in mp3_lines:
        mp3_items.append(element.split(";"))

    file.seek(0)
    file.truncate()

    if len(mp3_items) < 3:
        add_lines = 3 - len(mp3_items)

    while add_lines > 0:
        file.write("\n")
        add_lines -= 1

    mp3_items[2][0] = new_song

    for song, artists, duration, _ in mp3_items:
        file.write(f"{song};{artists};{duration}\n")
    file.close()


my_mp4_playlist(r"/home/netanel55/PycharmProjects/sigitSelfHomework/songs.txt", "Python Love Story")