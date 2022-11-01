def MakeArray(text):
    array = text.readlines()
    temparr = []
    x = 0
    for element in array:
        temparr.append(parse(array[x]))
        x += 1
    array = temparr
    return array


def parse(string):
    array = []
    foot = -1
    x = 0
    for char in string:
        if char == "," or char == "\n":
            if string.find("\n")>0:
                string.replace("\n",'')
            array.append(string[foot + 1:x])
            foot = x
        x += 1
    return array
