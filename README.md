# imgur-dynamic-wallpaper
Python script to set a random wallpaper from imgur gallery, after every specified time interval

[Current imgur gallery used](https://imgur.com/gallery/rBarn)

## Usage
### Install Requirements
Gnome 3 is required to update background

The script is built in python3

Only extra package apart from python standard package being used is python-crontab. Install the requirement usinig 
```bash
$ pip3 install -r requirements.txt
```
### Add cronjob
Run the script using
```bash
$ python3 cron.py
```
Default timer is set to 30 minutes.

To customize the update time interval, optional flags can be provided as
```
-min [1-59]  Set minutes after which the wallpaper updates
-hr [0-23]   Set hours after which the wallpaper updates
-dom [1-31]  Set the days for wallpaper update
```

## Working
Working of the script is described here. You can try this out and put any other imgur gallery page for your wallpapers

Imgur images are loaded dynamically with an additional XMLHttpRequest.
1. ```extract_json.py``` extracts the JSON containing url, extension of the images by running an ```XHR``` that is used in given imgur link
2. Extracted JSON is stored in ```img_info.json```
3. ```update_background.py``` picks a random image url from the ```img_info.json```, downloads the image, and updates the background image of desktop using ```gsettings```
4. ```cron.py``` adds a cronjob to run ```update_background.py``` after every given time interval


To change the imgur gallery
1. Open developers tools for your imgur page
2. Go to the ```Network``` panel select only ```XHR``` requests. Reload the page to display the requests made
3. Click any request to open a new details window 
4. Select ```Response``` tab in the details window
5. Find the request whose response tab contains the field ```is_album``` field with value ```1```
6. Right click the request, copy the URL 
7. Place this URL in the ```extract(URL=)``` function call in ```bin/extract_json.py```
8. Run ```bin/extract_json.py```
9. Run ```cron.py```, provide optional timer arguments if you wish

