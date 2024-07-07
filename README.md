# YouTube Music Playlists Creator
This repo is mainly formed of a quick Python script, to create playlists on YouTube Music from .csv files. In my case, those files came from scraping my Deezer account. See the repo [Deezer Scraper](https://github.com/vam-engineering/ScrapingDeezer).

**How to use:** 
1. Create an authentification file following [ytmusicapi documentation](https://ytmusicapi.readthedocs.io/en/stable/setup/oauth.html) 
2. Launch the script, a folder location containing the .csv files will be requested; columns **Title** and **Artist** are expected.\
[An example file](example.csv) is available, which was created using the [Deezer Scraper](https://github.com/vam-engineering/ScrapingDeezer) previously mentionned.

**Disclaimer:**
This script has been written quickly - it is far from perfect and errors might (will?) happen.\
Since I'm using an API, errors are quite likely to happen, as of right now, none of those are handled; _my goal was to get most of the job done, and this script does that just fine._
