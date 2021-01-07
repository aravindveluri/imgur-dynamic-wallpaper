import random
import subprocess
import json
import pathlib
import requests

# Get current path
def get_current_path():
    return str(pathlib.Path(__file__).parent.absolute())

# Access JSON file; get image url and extension
def get_url_ext(current_path):

    with open(current_path + "/img_info.json", "r") as f:
        # Randomly choose an image link
        info = random.choice(json.load(f))

        return(info['url'], info['ext'])

# Update wallpaper file
def update_wallpaper(current_path, url, ext):

    with open(current_path + '/wallpaper.' + ext, 'wb') as handle:
        
        imgpath = handle.name
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)

# Get image path
def get_img_path(current_path, ext):

    return current_path + '/wallpaper.' + ext


if __name__ == "__main__":
    
    current_path = get_current_path()
    url, ext = get_url_ext(current_path)
    
    update_wallpaper(current_path, url, ext)
    
    # File path to update background
    img_filepath = "file:///" + get_img_path(current_path, ext)
    
    # Update backgroung using shell command
    stream = subprocess.Popen(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', 
        '"{}"'.format(img_filepath)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

