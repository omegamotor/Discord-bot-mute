from tkinter import *
import json
import time
from botClass import MyBotMute



def main():
    print("----------------------------------------------------------------------------")
    print("Witaj w Programie wyciszającym zbyt niestosownego gracza")

    print("Sprawdzam czy configuracja jest ustawiona...")
    try:
        read_file("data.txt")
    except IOError:
        print("Brak configuracji proszę ją utworzyć")
        time.sleep(2)
        write_file("data.txt")
    finally:
        open("data.txt").close()

    print("----------------------------------------------------------------------------")
    print("Wciśnij 1 aby włączyć program")
    print("Wciśnij 2 aby skonfigurować program")
    print("Wciśnij 3 aby przeczytać instrukcję")
    print("Wciśnij 4 aby zmienić tylko token Bota")
    print("Wciśnij 5 aby zamknąć program")
    val = input("Czekam: ")


    if val == '1':
        import bot
    elif val == '2':
        write_file("data.txt")
        read_file("data.txt")

    elif val == '3':
        print("----------------------------------------------------------------------------")
        print("Bot po aktywacji staje się aktywny na serwerze")
        print("Po wpisaniu komendy !m @nazwa_gracza zostaje aktywowany skrypt")
        print("Jeśli podczas jego działania naciśniesz")
        with open("data.txt") as json_file:
            data = json.load(json_file)
            for p in data['config']:
                print("----------------------------------------------------------------------------")
                print(p['muteButton'] + " - Użytkownik zostanie wyciszony")
                print(p['unMuteButton'] + " - Użytkownik zostanie odciszony")
        print("- - Program zakończy działanie")

        input("...")

    elif val == '4':
        #write_new_bot_token()
        print("Work in porgress")

    elif val == '5':
        exit()


def read_file(file):
    with open(file) as json_file:
        data = json.load(json_file)
        for p in data['config']:
            print("----------------------------------------------------------------------------")
            print('Id głównego kanału: ' + p['idMainChannel'])
            print('Id wyciszonego kanału: ' + p['idSilentChannel'])
            print('Przycisk do wyciszenia: ' + p['muteButton'])
            print('Przycisk do odciszenia: ' + p['unMuteButton'])
            print('TOKEN: ' + p['TOKEN'])


def write_file(file):
    print("----------------------------------------------------------------------------")
    id_main_channel = input('Podaj id głównego kanału: ')
    id_silent_channel = input('Podaj id wyciszonego kanału: ')
    mute_button = input('Podaj przycisk do wyciszania: ')
    unmute_button = input('Podaj przycisk do odciszania: ')
    token = input('Podaj tokenBota: ')

    data = {}
    data['config'] = []

    data['config'].append({
        'idMainChannel': id_main_channel,
        'idSilentChannel': id_silent_channel,
        'muteButton': mute_button,
        'unMuteButton': unmute_button,
        'TOKEN': token
    })


    with open(file, 'w') as outfile:
        json.dump(data, outfile)


def write_new_bot_token():
    data = {}
    data['config'] = []
    data['TOKEN'] = []


    with open("data.txt") as json_file:
        data = json.load(json_file)
        for p in data['config']:
            id_main_channel = p['idMainChannel']
            id_silent_channel = p['idSilentChannel']
            mute_button = p['muteButton']
            unmute_button = p['unMuteButton']

    data['config'].append({
        'idMainChannel': id_main_channel,
        'idSilentChannel': id_silent_channel,
        'muteButton': mute_button,
        'unMuteButton': unmute_button
    })

    token = input('Podaj tokenBota: ')
    data['config'].append({'TOKEN': token})
    with open("data.txt", 'w') as outfile:
        json.dump(data, outfile)



def take_token():
    with open("data.txt") as json_file:
        data = json.load(json_file)
        for p in data['TOKEN']:
            return p[0]




if __name__ == "__main__":
    Bot = MyBotMute()
    #print(take_token())
    #while True:
        #main()



