from PIL import Image

ASCII_CHARS_STYLE_0 = " .:coCO8@"[::-1]
ASCII_CHARS_STYLE_1 = " .:oO8@"[::-1]
ASCII_CHARS_STYLE_2 = " .'~:;!>+=icjtJY56SXDQKHNWM"[::-1]
ASCII_CHARS_STYLE_3 = " .:+j6bHM"[::-1]
ASCII_CHARS_STYLE_4 = "#"[::-1]
ASCII_CHARS_STYLE_5 = " #"[::-1]
ASCII_CHARS_STYLE_6 = "  .`,'_~-^:;" + chr(34) + "*!{}|<>()?\/=+[]icf1jltr&vneaouzsxbhdkpqygmw$IJC7LT23SV45HNUDYAP69BG0OR8QEFZKX%MW@##################"[::-1]
ASCII_CHARS_STYLE_7 = "       ......;;;;;;;======++++++iiiiiiittttttIIIIIIIYYYYYYVVVVVVXXXXXXXRRRRRRMMMMMMMWWWWWW#######################"[::-1]

def aal_hex_color_from_pixel(pixel):
    return '#{:02X}{:02X}{:02X}'.format(pixel.red, pixel.green, pixel.blue)

def aal_rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def aal_span(str_text, str_color):
    return "<span style= color:" + str_color + "; >" + str_text + "</span>"

def aal_scale_image(original_image, new_width):
    (original_width, original_height) = original_image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)
    new_image = original_image.resize((new_width, new_height))
    return new_image

def aal_convert_to_grayscale(image):
    return image.convert('L')

def aal_convert_image_to_ascii(file_path, ascii_image_width, custom_ascii_chars = "", ascii_chars_default = 0):
    
    try:
        converting_image = Image.open(file_path)
    except Exception as e:
        print(e)
        return None
    
    converting_image = aal_scale_image(converting_image,ascii_image_width)
    # colored_converting_image_pixels = converting_image.load()
    converting_image = aal_convert_to_grayscale(converting_image)
    converting_image_pixels = converting_image.load()
    (converting_image_width, converting_image_height) = converting_image.size    
    
    if len(custom_ascii_chars)>0:
        converting_ascii_chars = custom_ascii_chars
    else:
        if ascii_chars_default == 0:
            converting_ascii_chars = ASCII_CHARS_STYLE_0
        elif ascii_chars_default == 1:
            converting_ascii_chars = ASCII_CHARS_STYLE_1
        elif ascii_chars_default == 2:
            converting_ascii_chars = ASCII_CHARS_STYLE_2
        elif ascii_chars_default == 3:
            converting_ascii_chars = ASCII_CHARS_STYLE_3
        elif ascii_chars_default == 4:
            converting_ascii_chars = ASCII_CHARS_STYLE_4
        elif ascii_chars_default == 5:
            converting_ascii_chars = ASCII_CHARS_STYLE_5
        elif ascii_chars_default == 6:
            converting_ascii_chars = ASCII_CHARS_STYLE_6
        elif ascii_chars_default == 7:
            converting_ascii_chars = ASCII_CHARS_STYLE_7
        else:
            converting_ascii_chars = ASCII_CHARS_STYLE_0
    
    converting_ascii_chars_length = len(converting_ascii_chars)-1
    if converting_ascii_chars_length == 0:
        converting_ascii_chars = converting_ascii_chars + converting_ascii_chars
        converting_ascii_chars_length = len(converting_ascii_chars)-1
        converting_ascii_chars_step = 255 / converting_ascii_chars_length
    else:
        converting_ascii_chars_step = 255 / converting_ascii_chars_length

    converted_ascii_pixels = ""
    converting_ascii_image = ""
    for y in range(converting_image_height):
        for x in range(converting_image_width):
            converting_image_pixel = converting_image_pixels[x,y]
            if converting_image_pixel == 0:
                converted_ascii_pixels = converted_ascii_pixels + converting_ascii_chars[0]
            elif converting_image_pixel == 255:
                converted_ascii_pixels = converted_ascii_pixels + converting_ascii_chars[converting_ascii_chars_length]
            else:
                old_step = 0
                next_step = converting_ascii_chars_step
                for current_step in range(converting_ascii_chars_length):
                    if converting_image_pixel > old_step and converting_image_pixel <= next_step:
                        converted_ascii_pixels = converted_ascii_pixels + converting_ascii_chars[current_step]
                        break
                    old_step = next_step
                    next_step = next_step + converting_ascii_chars_step
        converting_ascii_image = converting_ascii_image + converted_ascii_pixels + "\n"
        converted_ascii_pixels = ""

    return converting_ascii_image

def aal_convert_image_to_ascii_progress(file_path, ascii_image_width, custom_ascii_chars = "", ascii_chars_default = 0):
    
    try:
        converting_image = Image.open(file_path)
    except Exception as e:
        print(e)
        return None
    
    converting_image = aal_scale_image(converting_image,ascii_image_width)
    # colored_converting_image_pixels = converting_image.load()
    converting_image = aal_convert_to_grayscale(converting_image)
    converting_image_pixels = converting_image.load()
    (converting_image_width, converting_image_height) = converting_image.size    
    
    if len(custom_ascii_chars)>0:
        converting_ascii_chars = custom_ascii_chars
    else:
        if ascii_chars_default == 0:
            converting_ascii_chars = ASCII_CHARS_STYLE_0
        elif ascii_chars_default == 1:
            converting_ascii_chars = ASCII_CHARS_STYLE_1
        elif ascii_chars_default == 2:
            converting_ascii_chars = ASCII_CHARS_STYLE_2
        elif ascii_chars_default == 3:
            converting_ascii_chars = ASCII_CHARS_STYLE_3
        elif ascii_chars_default == 4:
            converting_ascii_chars = ASCII_CHARS_STYLE_4
        elif ascii_chars_default == 5:
            converting_ascii_chars = ASCII_CHARS_STYLE_5
        elif ascii_chars_default == 6:
            converting_ascii_chars = ASCII_CHARS_STYLE_6
        elif ascii_chars_default == 7:
            converting_ascii_chars = ASCII_CHARS_STYLE_7
        else:
            converting_ascii_chars = ASCII_CHARS_STYLE_0
    
    converting_ascii_chars_length = len(converting_ascii_chars)-1
    if converting_ascii_chars_length == 0:
        converting_ascii_chars = converting_ascii_chars + converting_ascii_chars
        converting_ascii_chars_length = len(converting_ascii_chars)-1
        converting_ascii_chars_step = 255 / converting_ascii_chars_length
    else:
        converting_ascii_chars_step = 255 / converting_ascii_chars_length

    converted_ascii_pixels = ""
    converting_ascii_image = ""
    perc_current = 0
    perc_max = converting_image_height * converting_image_width
    for y in range(converting_image_height):
        for x in range(converting_image_width):
            converting_image_pixel = converting_image_pixels[x,y]
            if converting_image_pixel == 0:
                converted_ascii_pixels = converted_ascii_pixels + converting_ascii_chars[0]
            elif converting_image_pixel == 255:
                converted_ascii_pixels = converted_ascii_pixels + converting_ascii_chars[converting_ascii_chars_length]
            else:
                old_step = 0
                next_step = converting_ascii_chars_step
                for current_step in range(converting_ascii_chars_length):
                    if converting_image_pixel > old_step and converting_image_pixel <= next_step:
                        converted_ascii_pixels = converted_ascii_pixels + converting_ascii_chars[current_step]
                        break
                    old_step = next_step
                    next_step = next_step + converting_ascii_chars_step
            perc_current = perc_current + 1
            perc = (perc_current / perc_max) * 100
            print("Converting is at {}%".format(int(perc)), end='\r', flush=True)
        converting_ascii_image = converting_ascii_image + converted_ascii_pixels + "\n"
        converted_ascii_pixels = ""

    return converting_ascii_image

def aal_convert_image_to_ascii_html(file_path, ascii_image_width, custom_ascii_chars = "", ascii_chars_default = 0, font_name = "Terminal", font_size = 8, font_space = 0, font_weight = "normal", background_color = "#FFFFFF"):
    
    try:
        converting_image = Image.open(file_path)
    except Exception as e:
        print(e)
        return None
    
    converting_image = aal_scale_image(converting_image,ascii_image_width)
    colored_converting_image_pixels = converting_image.load()
    converting_image = aal_convert_to_grayscale(converting_image)
    converting_image_pixels = converting_image.load()
    (converting_image_width, converting_image_height) = converting_image.size
    
    if len(custom_ascii_chars)>0:
        converting_ascii_chars = custom_ascii_chars
    else:
        if ascii_chars_default == 0:
            converting_ascii_chars = ASCII_CHARS_STYLE_0
        elif ascii_chars_default == 1:
            converting_ascii_chars = ASCII_CHARS_STYLE_1
        elif ascii_chars_default == 2:
            converting_ascii_chars = ASCII_CHARS_STYLE_2
        elif ascii_chars_default == 3:
            converting_ascii_chars = ASCII_CHARS_STYLE_3
        elif ascii_chars_default == 4:
            converting_ascii_chars = ASCII_CHARS_STYLE_4
        elif ascii_chars_default == 5:
            converting_ascii_chars = ASCII_CHARS_STYLE_5
        elif ascii_chars_default == 6:
            converting_ascii_chars = ASCII_CHARS_STYLE_6
        elif ascii_chars_default == 7:
            converting_ascii_chars = ASCII_CHARS_STYLE_7
        else:
            converting_ascii_chars = ASCII_CHARS_STYLE_0
    
    converting_ascii_chars_length = len(converting_ascii_chars)-1
    if converting_ascii_chars_length == 0:
        converting_ascii_chars = converting_ascii_chars + converting_ascii_chars
        converting_ascii_chars_length = len(converting_ascii_chars)-1
        converting_ascii_chars_step = 255 / converting_ascii_chars_length
    else:
        converting_ascii_chars_step = 255 / converting_ascii_chars_length

    sHTML = "<html>\n<head>\n"
    sHTML = sHTML + "<meta http-equiv= content-type  content= text/html; charset=" + font_name + " >\n<style>\n"
    sHTML = sHTML + "pre {font-size:" + str(font_size) + "pt; letter-spacing:" + str(font_space) + "px; line-height:" + str(font_size) + "pt; font-weight:" + font_weight + ";}\n"
    sHTML = sHTML + "</style>\n</head>\n<body bgcolor=" + background_color + ">\n<pre>\n"
    eHTML = "</pre>\n</body>\n</html>"
    
    converted_ascii_pixels = ""
    converting_ascii_image = sHTML
    for y in range(converting_image_height):
        for x in range(converting_image_width):
            converting_image_pixel = converting_image_pixels[x,y]
            if converting_image_pixel == 0:
                converted_ascii_pixels = converted_ascii_pixels + converting_ascii_chars[0]
            elif converting_image_pixel == 255:
                converted_ascii_pixels = converted_ascii_pixels + converting_ascii_chars[converting_ascii_chars_length]
            else:
                old_step = 0
                next_step = converting_ascii_chars_step
                for current_step in range(converting_ascii_chars_length):
                    if converting_image_pixel > old_step and converting_image_pixel <= next_step:
                        try:
                            r, g, b, a = colored_converting_image_pixels[x, y]
                        except:
                            r, g, b = colored_converting_image_pixels[x, y]
                        converted_ascii_pixels = converted_ascii_pixels + aal_span(converting_ascii_chars[current_step],aal_rgb_to_hex(r,g,b))
                        break
                    old_step = next_step
                    next_step = next_step + converting_ascii_chars_step
        converting_ascii_image = converting_ascii_image + converted_ascii_pixels + "\n"
        converted_ascii_pixels = ""
    
    converting_ascii_image = converting_ascii_image + eHTML
    
    return converting_ascii_image

def aal_convert_image_to_ascii_html_progress(file_path, ascii_image_width, custom_ascii_chars = "", ascii_chars_default = 0, font_name = "Terminal", font_size = 8, font_space = 0, font_weight = "normal", background_color = "#FFFFFF"):
    
    try:
        converting_image = Image.open(file_path)
    except Exception as e:
        print(e)
        return None
    
    converting_image = aal_scale_image(converting_image,ascii_image_width)
    colored_converting_image_pixels = converting_image.load()
    converting_image = aal_convert_to_grayscale(converting_image)
    converting_image_pixels = converting_image.load()
    (converting_image_width, converting_image_height) = converting_image.size
    
    if len(custom_ascii_chars)>0:
        converting_ascii_chars = custom_ascii_chars
    else:
        if ascii_chars_default == 0:
            converting_ascii_chars = ASCII_CHARS_STYLE_0
        elif ascii_chars_default == 1:
            converting_ascii_chars = ASCII_CHARS_STYLE_1
        elif ascii_chars_default == 2:
            converting_ascii_chars = ASCII_CHARS_STYLE_2
        elif ascii_chars_default == 3:
            converting_ascii_chars = ASCII_CHARS_STYLE_3
        elif ascii_chars_default == 4:
            converting_ascii_chars = ASCII_CHARS_STYLE_4
        elif ascii_chars_default == 5:
            converting_ascii_chars = ASCII_CHARS_STYLE_5
        elif ascii_chars_default == 6:
            converting_ascii_chars = ASCII_CHARS_STYLE_6
        elif ascii_chars_default == 7:
            converting_ascii_chars = ASCII_CHARS_STYLE_7
        else:
            converting_ascii_chars = ASCII_CHARS_STYLE_0
    
    converting_ascii_chars_length = len(converting_ascii_chars)-1
    if converting_ascii_chars_length == 0:
        converting_ascii_chars = converting_ascii_chars + converting_ascii_chars
        converting_ascii_chars_length = len(converting_ascii_chars)-1
        converting_ascii_chars_step = 255 / converting_ascii_chars_length
    else:
        converting_ascii_chars_step = 255 / converting_ascii_chars_length

    sHTML = "<html>\n<head>\n"
    sHTML = sHTML + "<meta http-equiv= content-type  content= text/html; charset=" + font_name + " >\n<style>\n"
    sHTML = sHTML + "pre {font-size:" + str(font_size) + "pt; letter-spacing:" + str(font_space) + "px; line-height:" + str(font_size) + "pt; font-weight:" + font_weight + ";}\n"
    sHTML = sHTML + "</style>\n</head>\n<body bgcolor=" + background_color + ">\n<pre>\n"
    eHTML = "</pre>\n</body>\n</html>"
    
    converted_ascii_pixels = ""
    converting_ascii_image = sHTML
    
    perc_current = 0
    perc_max = converting_image_height * converting_image_width
    for y in range(converting_image_height):
        for x in range(converting_image_width):
            converting_image_pixel = converting_image_pixels[x,y]
            if converting_image_pixel == 0:
                converted_ascii_pixels = converted_ascii_pixels + converting_ascii_chars[0]
            elif converting_image_pixel == 255:
                converted_ascii_pixels = converted_ascii_pixels + converting_ascii_chars[converting_ascii_chars_length]
            else:
                old_step = 0
                next_step = converting_ascii_chars_step
                for current_step in range(converting_ascii_chars_length):
                    if converting_image_pixel > old_step and converting_image_pixel <= next_step:
                        try:
                            r, g, b, a = colored_converting_image_pixels[x, y]
                        except:
                            r, g, b = colored_converting_image_pixels[x, y]
                        converted_ascii_pixels = converted_ascii_pixels + aal_span(converting_ascii_chars[current_step],aal_rgb_to_hex(r,g,b))
                        break
                    old_step = next_step
                    next_step = next_step + converting_ascii_chars_step
            perc_current = perc_current + 1
            perc = (perc_current / perc_max) * 100
            print("Converting is at {}%".format(int(perc)), end='\r', flush=True)
        converting_ascii_image = converting_ascii_image + converted_ascii_pixels + "\n"
        converted_ascii_pixels = ""
    
    converting_ascii_image = converting_ascii_image + eHTML
    
    return converting_ascii_image
