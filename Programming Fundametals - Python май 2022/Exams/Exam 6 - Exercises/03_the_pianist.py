def create_pieces(pieces_dict, number):
    for _ in range(number):
        data = input().split('|')
        piece_name = data[0]
        composer = data[1]
        key = data[2]

        pieces_dict[piece_name] = {'composer': composer, 'key': key}

    return pieces_dict


def additional_pieces_data(pieces_dict):

    while True:
        command = input().split('|')
        if command[0] == "Stop":
            break

        if command[0] == "Add":
            piece_name = command[1]
            composer = command[2]
            key = command[3]
            if piece_name not in pieces_dict:
                pieces_dict[piece_name] = {'composer': composer, 'key': key}
                print(f"{piece_name} by {composer} in {key} added to the collection!")
            else:
                print(f"{piece_name} is already in the collection!")

        elif command[0] == "Remove":
            piece_name = command[1]
            if piece_name in pieces_dict:
                del pieces_dict[piece_name]
                print(f"Successfully removed {piece_name}!")
            else:
                print(f"Invalid operation! {piece_name} does not exist in the collection.")

        elif command[0] == "ChangeKey":
            piece_name = command[1]
            new_key = command[2]
            if piece_name in pieces_dict:
                pieces_dict[piece_name]['key'] = new_key
                print(f"Changed the key of {piece_name} to {new_key}!")
            else:
                print(f"Invalid operation! {piece_name} does not exist in the collection.")

    return pieces_dict


def final_result(pieces_dict):
    for element in pieces_dict:
        print(f"{element} -> Composer: {pieces_dict[element]['composer']}, Key: {pieces_dict[element]['key']}")


def the_pianist(number):
    pieces_dict = {}

    create_pieces(pieces_dict, number)
    additional_pieces_data(pieces_dict)
    final_result(pieces_dict)


n = int(input())
the_pianist(n)
