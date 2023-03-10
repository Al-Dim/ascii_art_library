# ascii_art_library

A library for converting an image to ascii art (simple text and html).

Developed by AlDim (2023).

# Examples

Generate a simple ascii from a file named "test.png", declare that the generated ascii
will have 200chars width, don't use any custom chars and use the default (0) chars.
Print the generated ascii.

import ascii_art_library as aal

ascii_art = aal.aal_convert_image_to_ascii("test.png", 200, "", aal.ASCII_CHARS_STYLE_0)

print (ascii_art)


Generate a html ascii from a file named "test.png", declare that the generated ascii
will have 200chars width, don't use any custom chars and use the default (0) chars.
Save the generated ascii as <test.html> file, that can be open to a browser.

import ascii_art_library as aal

ascii_art = aal.aal_convert_image_to_ascii_html("test.png", 200, "", aal.ASCII_CHARS_STYLE_0)

text_file = open("test.html", "w")

text_file.write(ascii_art)

text_file.close()
