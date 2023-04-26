from container import Container
from constants import COMMANDS_HELP
from json import JSONDecodeError #WHAT

class CLI:

    def __init__(self):
        self.container = Container()

    def run(self):
        print("Welcome to CLI program!")
        username = input("Enter your username: ")
        self.container.switch(username=username)

        while True:
            command = input("Type command. Type 'help' to see all available commands\n")
            command_split = command.split()
            try:
                if command_split[0] == "add":
                    # if len(command_split) == 1:
                    #     print("Too few arguments for command 'add <key> [key, …]'")
                    # else:
                        self.container.add(*command_split[1:])
                elif command_split[0] == "remove":
                    if len(command_split) == 1:
                        print("Too few arguments for command 'remove <key>'")
                    elif len(command_split) > 2:
                        print("Too many arguments for command 'remove <key>'")
                    else:
                        self.container.remove(command_split[1])
                elif command_split[0] == "find":
                    if len(command_split) == 1:
                        print("Too few arguments for command 'find <key> [key, …]'")
                    else:
                        self.container.find(command_split[1:])
                elif command_split[0] == "list":
                    self.container.list()
                elif command_split[0] == "grep":
                    if len(command_split) > 2:
                        print("Too many arguments for command 'grep <regex>'")
                    else:
                        self.container.grep(command_split[1])
                elif command_split[0] == "switch":
                    if len(command_split) > 1:
                        print("Too many arguments for command. Expected - 0")
                    else:
                        choice = input(f'Do you want to save your container? (Yes/No): ')

                        while choice.lower() != 'yes' and choice.lower() != 'no':
                            choice = input('Incorrect input! Try again')

                        if choice == 'no':
                            self.container.current_container = set()
                        else:
                            print(f'Saving container for {self.container.current_user}')
                        self.container.users[self.container.current_user] = self.container.current_container                     

                        new_username = input("Enter the new username: ")
                        self.container.switch(new_username)
                elif command_split[0] == "save":
                    if len(command_split) > 1:
                        print("Too many arguments for command. Expected - 0")
                    else:
                        self.container.save()
                elif command_split[0] == "load":
                    if len(command_split) > 1:
                        print("Too many arguments for command. Expected - 0")
                    else:
                        self.container.load()
                elif command_split[0] == "help":
                    if len(command_split) > 1:
                        print("Too many arguments for command. Expected - 0")
                    else:
                        print(COMMANDS_HELP)
                elif command_split[0] == "exit":
                    if len(command_split) > 1:
                        print("Too many arguments for command")
                    else:
                        choice = input(f'Do you want to save your container? (Yes/No): ')

                        while choice.lower() != 'yes' and choice.lower() != 'no':
                            choice = input('Incorrect input! Try again')

                        if choice == 'no':
                            self.container.current_container = set()
                        else:
                            print(f'Saving container for {self.container.current_user}.')
                            self.container.users[self.container.current_user] = self.container.current_container
                            self.container.save()
                        print("Exiting CLI program")
                        break
                else:
                    print(f'{command_split[0]} is not a command')
            except IndexError:
                print("Command wasn't found")
            except KeyError:
                print("The key wasn't found.")
            except FileNotFoundError:
                print("The file is not found.")
            except JSONDecodeError:
                print("The file is broken.")