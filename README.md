# Vlexa Voice Assistant Project
Vlexa is a personal voice assistant built using Python. It can perform various tasks such as searching for information on Wikipedia, fetching YouTube videos, retrieving news articles, telling jokes, and sharing random facts. Vlexa is designed to make interacting with the web and retrieving information easier using voice commands.

# Features
Wikipedia Search: Ask Vlexa to search for any information on Wikipedia. It will open the relevant Wikipedia page and read out a summary.

- **YouTube Video Search**: Search for videos on YouTube based on your voice commands, and Vlexa will display the search results in your browser.
  
- **News Search**: Fetch the latest news articles related to a specific query using the NewsAPI. Vlexa reads out summaries and opens articles in your browser.

- **Jokes**: Ask Vlexa for a joke, and it will fetch a random joke from an API to brighten your day.

- **Random Facts**: Vlexa can provide you with interesting random facts.

- **Voice Commands**: Vlexa understands voice commands using the `speech_recognition` library, making interaction seamless.


# Project Structure
- **main.py**: This file contains the core logic for interacting with Vlexa. It handles user input (via voice commands) and performs actions such as YouTube search, Wikipedia search, fetching news, telling jokes, and more.

- **selenium_web.py**: This file contains the helper classes and functions for interacting with external services such as YouTube, Wikipedia, and NewsAPI. It includes web scraping and automation features using Selenium and BeautifulSoup for fetching news articles and web content.

# Libraries Used
- **requests**: For making HTTP requests to APIs like NewsAPI.
- **wikipediaapi**: For interacting with Wikipedia and fetching summaries.
- **webbrowser**: To open URLs in the default browser.
- **selenium**: For automating web browser actions (e.g., searching YouTube).
- **BeautifulSoup**: For web scraping and parsing HTML content.
- **pyttsx3**: For text-to-speech functionality.
- **speech_recognition**: For recognizing user voice commands.
- **randfacts**: To fetch random facts.
- **NewsAPI**: For fetching news articles using the NewsAPI service.
# Setup Instructions
## Clone the Repository

```bash
git clone https://github.com/Anshu-Gondi/Vlexa-Voice-Assistant-project.git
```

## Install the Required Python Libraries:

```bash
pip install -r requirement.txt
```

# Setup Edge WebDriver
Download and install the Edge WebDriver.
Set the correct path to msedgedriver.exe in the selenium_web.py file.
Get NewsAPI Key
Get an API key from NewsAPI.
Replace the placeholder in the NewsSearcher class in selenium_web.py with your API key.
# Run the Application
To start interacting with Vlexa, run:

```bash
python main.py
```
# Author
This project is developed and maintained by **Anshu Gondi**.
