from PIL import Image

def validate_image(file_path):

    try:
        img = Image.open(file_path)

        if img.format not in ["JPEG","PNG","JPG"]:
            return False

        return True

    except:
        return False