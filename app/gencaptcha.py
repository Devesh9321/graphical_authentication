import random
import string
from captcha.image import ImageCaptcha

def generate_random_string(length=4):
    """Generate a random alphanumeric string of given length."""
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    # image = ImageCaptcha(width=170,height=70,fonts=['./Graphical_User_Authentication/static/font/Olicana.ttf'],font_sizes=tuple([32]))
    image = ImageCaptcha(width=170,height=70,fonts=['./app/static/font/Roboto.ttf'],font_sizes=tuple([32]))
    image_data = image.generate(password)
    image.write(password, './app/static/imgcaptcha/image.png')
    print("Generated CAPTCHA:", password)
    return password

