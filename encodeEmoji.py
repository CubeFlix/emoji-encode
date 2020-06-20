#!python3
#
# Converts (almost) all ASCII text to it's corresponding emoji in unicode. For instance,
# the letter a will turn into u\1F600 or the happy smiling emoji.
# By Kevin Chen

asciiChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 .\/\"'();!@#$%,&*\n"
emojiStart = 128512

def encode(text):
    """Encodes ASCII text that falls into the asciiChars string to a unicode string."""

    encoded = ""

    for char in text:
        if not asciiChars.find(char) == -1:
            encoded = encoded + chr(emojiStart + asciiChars.find(char))

    return encoded


def encodeBytes(text):
    """Encodes ASCII text that falls into the asciiChars string to a bytes object that can be written into a file."""

    encoded = bytes()

    for char in text:
        if not asciiChars.find(char) == -1:
            encoded = encoded + chr((emojiStart + asciiChars.find(char))).encode('utf-8')

    return encoded



