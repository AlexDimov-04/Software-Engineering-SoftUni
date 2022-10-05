def add_songs(*args):
    result = ''
    songs_dict = {}
    for el in args:
        song_name = el[0]
        lyrics = el[1]
        if song_name not in songs_dict:
            songs_dict[song_name] = ''
            for txt in lyrics:
                songs_dict[song_name] += txt + '\n'
        else:
            for txt in lyrics:
                songs_dict[song_name] += txt + '\n'

    for name, text in songs_dict.items():
        result += f'- {name}' + '\n'
        if text:
            result += text

    return result
