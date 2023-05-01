invalid_msg = "Invalid input."


def rgb_to_hex():
    # inputs
    red = int(input("Enter red (R) value: "))
    if red < 0 or red > 255:
        print(invalid_msg)
        return

    green = int(input("Enter green (G) value: "))
    if green < 0 or green > 255:
        print(invalid_msg)
        return

    blue = int(input("Enter blue (B) value: "))
    if blue < 0 or blue > 255:
        print(invalid_msg)
        return

    val = (red << 16) + (green << 8) + blue
    print(hex(val).upper()[2:])


def hex_to_rgb():
    hex_val = input("Enter the color (six hexadecimal digits): ")
    if len(hex_val) != 6:
        print(invalid_msg)
        return
    else:
        hex_val = int(hex_val, 16)

    two_hex_digits = 2 ** 8
    blue = hex_val % two_hex_digits

    hex_val = hex_val >> 8
    green = hex_val % two_hex_digits

    hex_val = hex_val >> 8
    red = hex_val % two_hex_digits

    print(f"{red}{green}{blue}")


def convert():
    while True:
        option = input("Enter 1 to convert RGB to HEX, Enter 2 to convert HEX to RGB. Enter X to Exit: ")

        if option == '1':
            print("RGB to Hex...")
            rgb_to_hex()
        elif option == '2':
            print("Hex to RGB...")
            hex_to_rgb()
        elif option.upper() == "X":
            break
        else:
            print("Error")


convert()