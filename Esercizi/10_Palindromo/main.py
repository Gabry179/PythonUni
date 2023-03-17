def trova_palindromo():
    for i in range(1000, 9999):
        if(int(str(i)[0]) == int(str(i)[3]) and int(str(i)[1]) == int(str(i)[2])):
            print(i)

trova_palindromo()