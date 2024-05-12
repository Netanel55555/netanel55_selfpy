from pydantic.v1.datetime_parse import parse_duration


def get_most_frequent_artist(artist_list):
    max_frequency = 0
    artist_name = ""

    for artist in artist_list:
        artist_frequency = artist_list.count(artist)
        if artist_frequency > max_frequency:
            max_frequency = artist_frequency
            artist_name = artist

    return artist_name


def my_mp3_playlist(file_path):
    input_file = open(file_path, "r")
    mp3_data = input_file.read()
    mp3_lines = mp3_data.split("\n")
    artist_list = []
    out_put = []

    mp3_items = []
    for element in mp3_lines:
        mp3_items.append(element.split(";"))

    current_max = 0
    longest_song_name = str()
    for songs in mp3_items:
        artist_list.append(songs[1])
        duration = parse_duration(songs[2])
        total_seconds = duration.total_seconds()

        if current_max < total_seconds:
            current_max = total_seconds
            longest_song_name = songs[0]

    out_put = [longest_song_name, len(mp3_items), get_most_frequent_artist(artist_list)]

    tuple_output = tuple(out_put)
    return tuple_output


print(my_mp3_playlist("/home/netanel55/PycharmProjects/sigitSelfHomework/songs.txt"))
