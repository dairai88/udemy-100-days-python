"""Exception Handling"""

try:
    file = open("a_file.txt", encoding="utf-8")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", encoding="utf-8", mode="w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} is not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")
