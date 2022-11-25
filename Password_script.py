import os
from cryptography.fernet import Fernet
class Password_manager:
    def __init__(self, pass_to_enter= '' ,app = '' , write_pass = '' , location = ''):
        # todo parola pentru fiecare nume scris
        self.folder_name = 'passwords_' + input('Numele persoanei care vrea sa gestioneze parolele: ') + '.txt'
        self.pass_to_enter  = pass_to_enter
        self.app = app
        self.write_pass = write_pass
        self.location = location
        self.mesaj = ''
        self.define_key = Fernet.generate_key()
        if os.path.exists('filekey.key') == False:
            with open('filekey.key', 'wb') as filekey:
                filekey.write(self.define_key)
        with open('filekey.key', 'rb') as filekey:
            self.actual_key = filekey.read()
        self.fernet = Fernet(self.actual_key)

    @staticmethod
    def menu():
        option = ''
        while option != '1' and option != '2' and option != '3':
            option = input('1. Salvati o parola\n'
                           '2. Alege aplicatia pentru care vrei sa vezi parola\n'
                           '3. Vezi toate parolele\n'
                           'Alege una din optiuni: ')
        return option

    def search_file(self):
        if self.location != '':
            try:
                os.chdir(self.location)
                for dirs, folders, files in os.walk(os.getcwd()):
                    for file in files:
                        if self.folder_name in file:
                            return True
                return False
            except:
                print("locatie gresita")
                return False
        else:
            for dirs, folders, files in os.walk(os.getcwd()):
                for file in files:
                    if self.folder_name in file:
                        return True
            return False


    def create_file(self):
        with open(self.folder_name, 'w') as f:
            pass

    def app_define(self):
        self.app = input('Alege aplicatia: ')

    def password_define(self):
        self.password = input("Care este parola aplicatiei: ")

    def write_password(self):
        with open(self.folder_name , 'a') as text:
            text.write(self.app + " : " + self.password + '\n')

    def read_all_pass(self, mode = ''):
        if mode == '':
            with open(self.folder_name, 'r') as text:
                texts = text.readlines()
                print('='*30)
                for linie in texts:
                    print(linie.strip())
                print('='*30)
                return texts
        elif mode == 'crypt':
            with open(self.folder_name, 'rb') as text:
                texts = text.read()
                return texts
        else:
            print('ERROR')

    def read_specific_pass(self):
        with open(self.folder_name, 'r') as text:
            texts = text.readlines()
            for line in texts:
                if self.app in line:
                    print('='*30)
                    print(line.strip())
                    print('='*30)
                    return texts
            print('Nu exista parola pentru aplicatia ' + self.app)
            return False

    def encrypt(self):
        all_data_binary = self.read_all_pass('crypt')
        encrypted = self.fernet.encrypt(all_data_binary)
        with open(self.folder_name , 'wb') as crypted :
            crypted.write(encrypted)

    def decrypt(self):
        all_data_crypted = self.read_all_pass('crypt')
        decrypted1 = self.fernet.decrypt(all_data_crypted)
        with open(self.folder_name , 'wb') as decrypted :
            decrypted.write(decrypted1)

    def verify_if_decrypyed(self):
        try:
            data = self.read_all_pass('crypt')
            if data == b'':
                return True
            return False
        except:
            return True
    def automatization(self):
        intrat = 'N'
        if self.search_file() == False:
            self.create_file()
        if self.verify_if_decrypyed() == False:
            self.decrypt()
        while intrat == 'N':
            raspuns_meniu = self.menu()
            if raspuns_meniu == '1':
                self.app_define()
                self.password_define()
                self.write_password()
            elif raspuns_meniu == '2':
                self.app_define()
                self.read_specific_pass()
            else:
                self.read_all_pass()
            intrat = input('Vrei sa iesi? [Y/N]: ').upper()
            while intrat != 'N':
                if intrat == 'Y':
                    self.encrypt()
                    break
                intrat = input('Vrei sa iesi? [Y/N]: ').upper()


if __name__ == "__main__":
    Nicu = Password_manager()
    Nicu.automatization()