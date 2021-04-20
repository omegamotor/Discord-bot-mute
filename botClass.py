import json
import time


class MyBotMute:
    dataFile = "data.txt"
    run = True

    def __init__(self):
        self.data = []
        print("----------------------------------------------------------------------------")
        print("Witaj w Programie wyciszającym zbyt niestosownego gracza")
        print("Sprawdzam czy configuracja jest ustawiona...")
        is_file = self.check_data()
        if is_file == False:
            print("Configuracja istnieje")

        while self.run:
            self.menu()

    def menu(self):
        print("----------------------------------------------------------------------------")
        print("Wciśnij 1 aby włączyć program")
        print("Wciśnij 2 aby skonfigurować program")
        print("Wciśnij 3 aby przeczytać instrukcję")
        print("Wciśnij 4 aby zmienić tylko token Bota")
        print("Wciśnij 5 aby zamknąć program")
        val = input("Czekam: ")
        self.do_something(val)

    def check_data(self):
        try:
            self.read_file()
        except IOError:
            print("Brak configuracji proszę ją utworzyć")
            time.sleep(2)
            self.write_file()
            return False
        finally:
            open(self.dataFile).close()
            return True

    def do_something(self, what):
        if what == '1':
            #run bot
            import bot
        elif what == '2':
            self.config_bot()
        elif what == '3':
            self.instruction()
        elif what == '4':
            # write_new_bot_token()
            self.read_file()
        elif what == '5':
            self.run = False
            exit()

    def read_file(self):
        p = self.read()
        print("----------------------------------------------------------------------------")
        print("Id głównego kanału: " + p.get('idSilentChannel'))
        print('Id wyciszonego kanału: ' + p.get('idSilentChannel'))
        print('Przycisk do wyciszenia: ' + p.get('muteButton'))
        print('Przycisk do odciszenia: ' + p.get('unMuteButton'))
        print('TOKEN: ' + p.get('TOKEN'))

    def read(self):
        config = {}
        with open(self.dataFile) as json_file:
            data = json.load(json_file)
            for p in data['config']:
                config['idMainChannel'] = p['idMainChannel']
                config['idSilentChannel'] = p['idSilentChannel']
                config['muteButton'] = p['muteButton']
                config['unMuteButton'] = p['unMuteButton']
                config['TOKEN'] = p['TOKEN']
        return config

    def instruction(self):
        print("----------------------------------------------------------------------------")
        print("Bot po aktywacji staje się aktywny na serwerze")
        print("Po wpisaniu komendy !m @nazwa_gracza zostaje aktywowany skrypt")
        print("Jeśli podczas jego działania naciśniesz")
        with open(self.dataFile) as json_file:
            data = json.load(json_file)
            for p in data['config']:
                print("----------------------------------------------------------------------------")
                print(p['muteButton'] + " - Użytkownik zostanie wyciszony")
                print(p['unMuteButton'] + " - Użytkownik zostanie odciszony")
        print("- - Program zakończy działanie")
        input("Naciśnij enter...")

    def config_bot(self):
        self.write_file()
        self.read_file()

    def write_file(self):
        new_config = {}
        print("----------------------------------------------------------------------------")
        new_config['id_main_channel'] = input('Podaj id głównego kanału: ')
        new_config['id_silent_channel'] = input('Podaj id wyciszonego kanału: ')
        new_config['mute_button'] = input('Podaj przycisk do wyciszania: ')
        new_config['unmute_button'] = input('Podaj przycisk do odciszania: ')
        new_config['token'] = input('Podaj tokenBota(Sprawdź na stronie bota): ')
        self.write(new_config)

    def write(self, param):
        data = {}
        data['config'] = []
        data['config'].append({
            'idMainChannel': param.get('id_main_channel'),
            'idSilentChannel': param.get('id_silent_channel'),
            'muteButton': param.get('mute_button'),
            'unMuteButton': param.get('unmute_button'),
            'TOKEN': param.get('token')
        })
        with open(self.dataFile, 'w') as outfile:
            json.dump(data, outfile)