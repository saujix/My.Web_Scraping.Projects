<detail>
<summary>Spotify Album Downloader</summary>
#Spotify Album Downloader
A Python script for downloading Spotify albums efficiently, ensuring progress is saved to prevent data loss.

## Features

- Downloads multiple albums with progress saved in `save_file.json`.
- Utilizes Selenium for web automation and BeautifulSoup for parsing.
- Supports retries if download issues occur.

## Requirements

- Python 3.x
- Selenium
- BeautifulSoup
- ChromeDriver
- Requests

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/saujix/My.Web_Scraping.Projects/spotify-album-downloader.git
   ```
2. Install dependencies:
   ```bash
   pip install selenium beautifulsoup4 requests
   ```

3. Ensure ChromeDriver is installed and added to PATH.

## Usage

1. Run the script:
   ```bash
   python spotify_album_downloader.py
   ```

2. Follow the prompts to enter Spotify album links and specify the storage folder.

## Notes

- If the script fails during download, rerun it. The progress is saved in `save_file.json`.
- For single album downloads, enter the link directly when prompted.

## Disclaimer

This script is for educational purposes only. Use responsibly and ensure you have the rights to download the content.

</detail>
