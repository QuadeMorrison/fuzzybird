import re

encoding = dict.fromkeys(['b', 'f', 'p', 'v'], 1)
encoding.update(dict.fromkeys(['c', 'g', 'j', 'k', 'q', 's', 'x',
                               'z'], 2))
encoding.update(dict.fromkeys(['d', 't'], 3))
encoding.update(dict.fromkeys(['l'], 4))
encoding.update(dict.fromkeys(['m', 'n'], 5))
encoding.update(dict.fromkeys(['r'], 6))

def encode_word(word):
    word = word.lower()
    encoded_word = ""
    num_encoded = 0
    last_was_vowel = False
    last_was_h_or_w = False

    for i, c in enumerate(word):
        if i == 0:
            encoded_word += str(c)
            if c not in encoding:
                last_was_vowel = True
        #elif num_encoded == 3:
           #break
        elif c in encoding:
            encoded_char = encoding[c]

            # Should skip duplicate characters
            # unless they are seperated by a vowel
            if not last_was_vowel:
                # Characters seperated by h or w should be encoded as one
                # number
                if last_was_h_or_w:
                    last_was_h_or_w = False
                    continue
                elif encoding[word[i - 1]] == encoded_char:
                    continue

            encoded_word += str(encoded_char)
            num_encoded += 1
            last_was_vowel = False
        # Characters seperated by h or w should be encoded as one number
        elif c == 'h' or c == 'w':
            last_was_h_or_w = True
            last_was_vowel = False
        # The letter must be a vowel
        else:
            last_was_vowel = True

    return encoded_word


def encode_str(str, pipe_together = False):
    encoded_str = ""

    for word in str.split(' '):
        encoded_str += encode_word(word)
        if pipe_together:
            encoded_str += ".*"

    return encoded_str if not pipe_together else encoded_str[0:-1]


def encode_phrases(phrases):
    return list(map(lambda phrase: encode_str(phrase), phrases))


def match_raw(str, phrases, encoded_phrases=False):
    encoded_str = encode_str(str, True)
    matching_phrases = []

    if not encoded_phrases:
        encoded_phrases = list(map(lambda phrase: encode_str(phrase), phrases))

    for i, phrase in enumerate(encoded_phrases):
        score = len(set(re.findall(encoded_str, phrase)))

        if score > 0:
            matching_phrases.append((phrases[i], score))

    return sorted(set(matching_phrases), key=lambda match: match[1], reverse=True)


def match(str, phrases, encoded_phrases=False):
    return [text[0] for text in match_raw(str, phrases, encoded_phrases)]
    #return sorted(matching_phrases)

