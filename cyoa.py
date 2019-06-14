import sys
import os


def game(file):
    room = "start"
    with open(file,"r") as f:
        story = f.read()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        room = room_data(story,room)


def room_data(story,room):
    room_start = "[{}]".format(room)
    room_end = "[/{}]".format(room)
    room_data = story[story.find(room_start)+len(room_start)+1:story.find(room_end)]
    new_room = print_room_text(room_data)
    return new_room


def print_room_text(room_data):
    text_start = room_data.find("{")+1
    text_end = room_data.find("}")
    room_text = room_data[text_start:text_end]
    print(room_text)
    new_room = choices(room_data)
    return new_room


def choices(room_data):
    num_list =  list()
    room_list = list()
    text_list = list()
    choices_start = room_data.find("(c)")+3
    choices_end = room_data.find("(/c)")
    choices = room_data[choices_start:choices_end]
    choice_list = choices.split("\n")
    choice_list.pop(0)
    choice_list.pop()
    if choice_list == []:
        exit()
    for index,choice_data in enumerate(choice_list, start=1):
        room,choice = choice_data.split(":")
        num_list.append(str(index))
        room_list.append(room)
        text_list.append(choice)

    for i in range(0,len(num_list)):
        print("{}){}".format(num_list[i],text_list[i]))

    while True:
        selection = input("\nSelect:")
        if num_list.count(selection) == 0:
            print("[ERROR]Please try again")
        else:
            return room_list[num_list.index(selection)]
        

    return input()
    

if  __name__ == "__main__":
    g_pos = sys.argv.count("-g")
    file = sys.argv[g_pos+1]
    game(file)