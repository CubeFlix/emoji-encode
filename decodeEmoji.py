#!python3
#
# Converts (almost) all ASCII text to it's corresponding emoji in unicode. For instance,
# the letter a will turn into u\1F600 or the happy smiling emoji.
# By Kevin Chen

asciiChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 .\/\"'();!@#$%,&*\n"
emojiStart = 128512

def decode(text):
    """Decodes unicode emojis into ASCII text. """

    decoded = ""

    for char in text:
        decimal = ord(char)
        decoded = decoded + asciiChars[decimal - emojiStart]

    return decoded

def decodeBytes(data):
    """Decodes binary unicode emojis into ASCII text. """

    text = data.decode('utf-8')

    decoded = ""

    for char in text:
        decimal = ord(char)
        decoded = decoded + (asciiChars[decimal - emojiStart])

    return decoded





