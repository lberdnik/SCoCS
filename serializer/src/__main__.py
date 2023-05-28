import sys
from .factory import Factory
def main():
    args = sys.argv

    if len(args) != 5:
        print("Invalid amount of args")
        exit()

    _, filepath_from, filepath_to, format_from, format_to = args

    # if format_from == format_to:
    #     print("Formats cant be equal")
    #     exit()

    try:
        source_serializer = Factory.create_serializer(format_from)
        result_serializer = Factory.create_serializer(format_to)
    except Exception as err:
        print(err)
        exit()

    try:
        with open(filepath_from) as file_from, open(filepath_to, "w") as file_to:
            deserialized_object = source_serializer.load(file_from)
            result_serializer.dump(deserialized_object, file_to)
    except Exception as err:
        print(err)
        exit()


if __name__ == '__main__':
    main()