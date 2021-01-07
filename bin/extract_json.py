import requests
import json

def extract(URL = "https://api.imgur.com/post/v1/posts/rBarn?client_id=546c25a59c58ad7&include=media%2Ctags%2Caccount%2Cadconfig%2Cpromoted"):

    # Get response from URL
    page = requests.get(URL)

    # Dump response JSON
    with open("img_info.json", "w") as f:

        # Extract only requrired fields
        cleaned = list(map(lambda x: {'url':x['url'], 'ext':x['ext']}, page.json()['media']))
        
        json.dump(cleaned, f)

if __name__ == "__main__":
    # For a different imgur gallery, pass the XHR URL for the imgur gallery page
    extract()
