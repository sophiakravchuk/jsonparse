import json


def read_js(filename):
    """
    (str) -> dct
    Reads the file
    """
    with open(filename) as f:
        js = json.load(f)
    f.close()
    return js


def get_path(js):
    """
    Gets the part of dict and returns it
    """
    global path
    if isinstance(js, str) or isinstance(js, int):
        return json.dumps(js, indent=2)
    is_list = False
    if isinstance(js, dict):
        keyslist = list(js.keys())
        print("Choose one of the next keys in your json file:")
        for key in range(len(keyslist)):
            print(str(key + 1) + ") " + keyslist[key])

    elif isinstance(js, list) or isinstance(js, tuple):
        is_list = True
        print("Next part of json file is a list. \nPlease choose the number of list element: ", end="")
        print("0 - " + str(len(js) - 1))
    n = input("\n\nEnter the key or press Enter to get a part of your json file:")
    if n == "":
        return json.dumps(js, indent=2)
    else:
        try:
            n = int(n)

            if is_list:
                path = path + "[" + str(n) + "]"
                js = js[n]
            else:
                if len(path) > 0:
                    path = path + "."
                path = path + keyslist[n-1]
                js = js[keyslist[n - 1]]
        except:
            if len(path) > 0:
                path = path + "."
            path = path + keyslist[n]
            js = js[n]
        return get_path(js)


if __name__ == "__main__":
    filename = input("Enter the name of json file:")
    # filename = "twitter1.json"
    js = read_js(filename)
    path = ""
    val = get_path(js)
    print(path, end=":   ")
    print(val)
