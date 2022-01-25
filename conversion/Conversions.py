#Algorithm to convert Hexadecimal number to Octal and vice versa
#Note: To convert hexadecimal to octal and vice versa, first the number
#      must be converted to a binary number as an intermediary operation
def main():
    menu = """
    Conversion
    1.Hexadecimal to Octal
    2.Octal to Hexadecimal
    3.Exit
    """
    argument = True
    while argument == True:
        print(menu)
        opt = int(input("Select option of conversion:"))

        if opt == 1:
            print("Enter hexadecimal number:")
            value = input()
            size = len(value)
            i = 0
            newnum = ""

            while i < size:
                if value[i] == '0':
                    newnum = newnum + "0000"
                elif value[i] == '1':
                    newnum = newnum + "0001"
                elif value[i] == '2':
                    newnum = newnum + "0010"
                elif value[i] == '3':
                    newnum = newnum + "0011"
                elif value[i] == '4':
                    newnum = newnum + "0100"
                elif value[i] == '5':
                    newnum = newnum + "0101"
                elif value[i] == '6':
                    newnum = newnum + "0110"
                elif value[i] == '7':
                    newnum = newnum + "0111"
                elif value[i] == '8':
                    newnum = newnum + "1000"
                elif value[i] == '9':
                    newnum = newnum + "1001"
                elif value[i] == 'A' or value[i] == 'a':
                    newnum = newnum + "1010"
                elif value[i] == 'B' or value[i] == 'b':
                    newnum = newnum + "1011"
                elif value[i] == 'C' or value[i] == 'c':
                    newnum = newnum + "1100"
                elif value[i] == 'D' or value[i] == 'd':
                    newnum = newnum + "1101"
                elif value[i] == 'E' or value[i] == 'e':
                    newnum = newnum + "1110"
                elif value[i] == 'F' or value[i] == 'f':
                    newnum = newnum + "1111"
                i = i + 1
            print("Hexadecimal number in Binary:", newnum)

            binary = int(newnum)
            octal = 0
            mul = chk = 1
            onum = ""
            while binary != 0:
                rem = binary % 10
                octal = octal + (rem * mul)
                if chk % 3 == 0:
                    onum = onum + str(octal)
                    mul = chk = 1
                    octal = 0
                else:
                    mul = mul * 2
                    chk = chk + 1
                binary = int(binary / 10)

            if chk != 1:
                onum = onum + str(octal)

            print("Binary number in Octal: ", onum[::-1])

        elif opt == 2:
            print("Enter octal number:")
            octnum = int(input())
            rev = 0
            x = 0

            while octnum != 0:
                rem = octnum % 10
                if rem > 7:
                    x = 1
                    break
                rev = rem + (rev * 10)
                octnum = int(octnum / 10)

            if x == 0:
                octnum = rev
                binary = ""

                while octnum!=0:
                    rem = octnum % 10
                    if rem == 0:
                        binary = binary + "000"
                    elif rem == 1:
                        binary = binary + "001"
                    elif rem == 2:
                        binary = binary + "010"
                    elif rem == 3:
                        binary = binary + "011"
                    elif rem == 4:
                        binary = binary + "100"
                    elif rem == 5:
                        binary = binary + "101"
                    elif rem == 6:
                        binary = binary + "110"
                    elif rem == 7:
                        binary = binary + "111"
                    octnum = int(octnum/10)
                print("Octal number in Binary:", binary)

            bnum = int(binary)
            hexa = i = 0
            temp = k = 1
            hnum = []
            while bnum != 0:
                rem = bnum % 10
                hexa = hexa + (rem * temp)
                if k % 4 == 0:
                    if hexa < 10:
                        hexa = hexa + 48
                        val = chr(hexa)
                        hnum.insert(i, val)
                    else:
                        hexa = hexa + 55
                        val = chr(hexa)
                        hnum.insert(i, val)
                    temp = 1
                    hexa = 0
                    k = 1
                    i = i + 1
                else:
                    temp = temp * 2
                    k = k + 1
                bnum = int(bnum / 10)

            if k != 1:
                hexa = hexa + 48
                val = chr(hexa)
                hnum.insert(i, val)
            if k == 1:
                i = i - 1

            print("Binary number in Hexadecimal: ", end="")
            while i >= 0:
                print(end=hnum[i])
                i = i - 1
            print()

        elif opt == 3:
            argument = False

        else:
            print("Choose a valid option")


if __name__ == '__main__':
    main()
