movieFile=input("Enter File Name To decode: ").split(".")
for name in movieFile:
    if not name.isnumeric():
        for character in name:
            if character=="0":
                character="O"
            if character=="4":
                character="a"
            if character=="3":
                character="e"
            if character=="1":
                character="i"
            if character=="7":
                character="u"
            print(character,end="")
        print(end=" ")
    else:
        break