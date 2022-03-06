import letters

try:
    with open("Text_to_transform.txt", mode="r") as text:
        text_to_transform = text.read()
    morse_text = ""
    for n in range(0, len(text_to_transform)):
        morse_letter = text_to_transform[n].lower()
        try:
            if n != len(text_to_transform)-1:
                if morse_letter == " ":
                    morse_text += "    "
                else:
                    morse_text += f"{letters.morse_dict[morse_letter]}   "
            else:
                if morse_letter == " ":
                    morse_text += "    "
                else:
                    morse_text += letters.morse_dict[morse_letter]
        except KeyError:
            print(f"Symbol {morse_letter} in not present in Morse Code.")

    with open("Morse_text.txt", mode="w") as text:
        text.write(morse_text)

except FileNotFoundError:
    print("File 'Text_to_transform.txt' with inputs is not found. Please create a file with text you would like to "
          "transform to the Morse Code.")
