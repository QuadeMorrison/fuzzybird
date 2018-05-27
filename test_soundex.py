from soundex import encode_word


def test():
    print(encode_word("Robbert") == "r163", "Double letter")
    print(encode_word("Robebert") == "r116", "Vowel between double letter")
    print(encode_word("Ashcroft") == "a261", "H between consonants")
    print(encode_word("Aswcroft") == "a261", "W between consonants")
    print(encode_word("tr") == "t600", "Less than 3 letters encoded")
    print(encode_word("Pfister") == "p236",
          "First letter has the same encoding as the second")


test()
