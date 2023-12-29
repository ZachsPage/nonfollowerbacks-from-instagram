# Get Non-Followbacks From Instagram JSON
This is a very simple script that provides a list of people who do not followback on Instagram.  
It **does not** require any Instagram APIs / permissions - which is preferred for security / privacy.  
There is a little leg work before, but some (including myself) prefer this trade off.

## How it works
For the input data, Instagram provides a way to download your data to JSON format - the 
`download request` takes about 5 minutes to process - here's how:
* Sign in to the [Account Center](https://accountscenter.instagram.com/):
    * This is provided by Meta [About blog for authenticity](https://www.facebook.com/help/instagram/1731078377046291)
* On the left, go to `Your information and permissions` -> [Download your information](https://accountscenter.instagram.com/info_and_permissions/dyi/)
* `Request a download` -> `Select types of information` -> `Followers & Following (under Connections)`
* `Date Range` -> `All time`
* `Format` -> `JSON`
* `Submit request`

Extract the downloaded data to a folder and use that as the argument to this script:
* Can use the folder `./downloads` here with a subfolder like `./downloads/<date>_data/`, if desired
* `python3 get_nonfollowers_from_json.py -i <directory with followers_1.json & following.json>`
