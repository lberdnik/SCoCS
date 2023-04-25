import re
import json

""" add <key> [key, …]  add one or more elements to the container (if the element is already in there then don’t add);
remove <key>  delete key from container;
find  <key> [key, …] check if the element is presented in the container, print each found or “No such elements” if nothing is;
list print all elements of container;
grep <regex>  check the value in the container by regular expression, print each found or “No such elements” if nothing is;
save/load  save container to file/load container from file;
switch  switches to another user. """


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
            print("All elements of container:")
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
        filename = f''

    def load(self, file=None):
        pass

    def switch(self, username):
        pass