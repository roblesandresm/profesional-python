def delete_duplicated(some_list):
    new_list = []
    for item in some_list:
        if type(item) == str:
            new_list.append(item.lower())
        else:
            new_list.append(item)
    
    return set(new_list)

def run():
    my_list = ["Perro",  "perro", 12, 12, 4, 5, "Hola"]
    print(delete_duplicated(my_list))

if __name__ == "__main__":
    run()