### Instagram Media Downloader

A Python script for downloading media (images, videos, audio) from a specified Instagram user's profile using Selenium and BeautifulSoup.
Note: Insta account needed
## Features

- Automates login to Instagram.
- Collects up to 100 media posts from a target Instagram user.
- Downloads media using [saveinsta.app](https://saveinsta.app).

## Requirements

- Python 3.x
- Selenium
- BeautifulSoup
- Requests
- ChromeDriver

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/saujix/My.Web_Scraping.Projects.git
   ```

2. Install dependencies:
   ```bash
   pip install selenium beautifulsoup4 requests
   ```

3. Ensure ChromeDriver is installed and added to PATH.

## Usage

1. Run the script:
   ```bash
   python instagram_media_downloader.py
   ```

2. Follow the prompts:
   - Enter your Instagram username and password.
   - Specify the location to save the media files.
   - Enter the target Instagram username (without '@').

## Notes

- The script automates interactions with Instagram and saveinsta.app, so use responsibly to avoid IP blocking.
- Minimize the browser window as instructed and be patient while the script runs.

## Disclaimer

This script is for educational purposes only. Use responsibly and ensure you have the rights to download or utilize any content. Refrain from running the script excessively to avoid getting blocked by Instagram.
