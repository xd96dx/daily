
with open("hA", "r") as f:
    with open("SA", "w") as file:
        str1 = f.read()
        in_string = ""
        for s in str1:
            try:
                n = int(s)
            except BaseException as e:
                continue

            in_string += s
            if len(in_string) == 6:
                file.write(in_string+"\n")
                in_string = ""
