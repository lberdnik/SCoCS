import re
import json

class Container:
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.current_container = set()

    def add(self, *keys):
        if keys:
            for key in keys:
                if key not in self.current_container:
                    self.current_container.add(key)
            print("Elements added successfully!")
        else:
            print("Nothing to add")

    def remove(self, key):
        if key in self.current_container:
            self.current_container.discard(key)
        else:
            print(f'No "{key}" in this container. Nothing to delete')

    def find(self, *keys):
        if keys:
            found = False
            for key in keys:
                if key in self.current_container:
                    found = True
                    print(f'Element {key} found')
            if not found:
                print("No such elements")
        else:
            print("Nothing to find")


    def list(self):
        if self.current_container:
            print("All elements of container: ")
            for key in self.current_container:
                print(key)
        else:
            print("Container is empty")

    def grep(self, regex):
        pattern = re.compile(regex)
        found = False
        for key in self.current_container:
            if pattern.findall(key):
                found = True
                print(key)
        
        if not found:
            print("No such elements")

    def save(self):
        filename = f'{self.current_user}.json'
        with open(filename, 'w') as f:
            json.dump(list(self.current_container), f)
        print("Container saved to file")

    def load(self, file=None):
        if file is None:
            filename = f'{self.current_user}.json'
        else:
            filename = f'{file}'
        
        try:
            with open(filename, 'r') as f:
                elements_list = json.load(f)
                for el in elements_list:
                    self.current_container.add(el)
            print("Container loaded from file")
        except FileNotFoundError:
            print(f'Cannot load {filename}: file not found')

    def switch(self, username):
        try:
            filename = f'{username}.json'
            open(filename, 'r')
            self.current_user = username
            choice = input(f'Welcome back, {username}!\nDo you want to load your saved container? (Yes/No): ')
            
            while choice.lower() != 'yes' and choice.lower()!= 'no':
                choice = input('Incorrect input! Try again')

            if choice.lower() == 'yes':
                print(f'Loading container for {username}')
                self.load()
            else:
                self.current_container = set()
        except FileNotFoundError:
            choice = input(f'Hello, {username}!\nDo you want to load container from file? (Yes/No): ')
            self.current_user = username
            
            while choice.lower() != 'yes' and choice.lower()!= 'no':
                choice = input('Incorrect input! Try again')
            
            if choice.lower() == 'yes':
                file = input("Input file name (it should be in this directory): ")
                filename = str(file)
                try:
                    open(filename, 'r')
                    self.current_user = username
                    self.users[self.current_user] = self.current_container
                except FileNotFoundError:
                    print(f'Hello, {username}! Creating a new container')
                    self.current_container = set()
                self.load(file=filename)
            else:
                self.current_container = set()