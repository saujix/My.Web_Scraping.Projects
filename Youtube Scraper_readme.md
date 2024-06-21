### YouTube Recommended Video Downloader

A Python script for downloading every recommended video from YouTube using Selenium, BeautifulSoup, and PyTube. Requires Google account login.

## Features

- Automates login to Google account.
- Fetches recommended YouTube video URLs.
- Downloads videos using PyTube, saving them to the specified directory.

## Requirements

- Python 3.x
- Selenium
- BeautifulSoup
- PyTube
- ChromeDriver

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/saujix/My.Web_Scraping.Projects.git
   ```

2. Install dependencies:
   ```bash
   pip install selenium beautifulsoup4 pytube
   ```

3. Ensure ChromeDriver is installed and added to PATH.

## Usage

1. Run the script:
   ```bash
   python youtube_recommended_downloader.py
   ```

2. Follow the prompts:
   - Enter your Google account email and password.
   - Specify the location to save the downloaded videos.

## Notes

- The script automates interactions with Google and YouTube, so use responsibly to avoid account issues.
- Ensure proper handling of login credentials and avoid sharing them.

## Disclaimer

This script is for educational purposes only. Use responsibly and ensure you have the rights to download or utilize any content. Avoid running the script excessively to prevent account or IP blocking.
