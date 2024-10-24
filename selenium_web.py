import requests
import wikipediaapi
import webbrowser  # Import webbrowser to open URLs
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup  # Import BeautifulSoup for web scraping
# Use this If you want to avoid manually managing the WebDriver binaries, you can use webdriver-manager
from webdriver_manager.microsoft import EdgeChromiumDriverManager  # Auto-manage the WebDriver version
            
class WikipediaSearcher:
    def __init__(self):
        self.wiki_wiki = wikipediaapi.Wikipedia(
            language='en',
            extract_format=wikipediaapi.ExtractFormat.WIKI,
            user_agent='MyVlexaVoiceAssistant/1.0 (https://www.wikipedia.org/; contact@example.com)'
        )

    def search_info(self, query):
        """Search for information on Wikipedia and open the page."""
        page = self.wiki_wiki.page(query)
        if page.exists():
            print(f"Wikipedia Summary: {page.summary[:500]}")  # Print the first 500 characters
            webbrowser.open(page.fullurl)
        else:
            print(f"Page not found for {query}")

class YouTubeSearcher:
    def __init__(self):
        edge_driver_path = r'C:\Drivers\Driver_Notes\msedgedriver.exe'  # Set your path
        edge_options = Options()
        edge_options.add_argument('log-level=3')  # Suppress all but fatal errors
        service = Service(edge_driver_path)
        self.driver = webdriver.Edge(service=service, options=edge_options)
        # self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)  # Modify this line (optional)

    def search_video(self, query):
        try:
            self.driver.get('https://www.youtube.com')
            wait = WebDriverWait(self.driver, 20)
            search_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#search')))
            search_box.click()
            search_box.send_keys(query)
            search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-icon-legacy"]')))
            search_button.click()
            print("Search complete. You can view the results.")
        except Exception as e:
            print(f"An error occurred while searching YouTube: {e}")
        finally:
            input("Press Enter to close the browser...")
            self.driver.quit()  # Ensure the browser is closed after the task

class NewsSearcher:
    def __init__(self, speak_func):
        self.api_key = "f06582ff1af7412898c9bd29e908de9b"  # Your API key
        self.base_url = "https://newsapi.org/v2/everything"  # News API base URL
        self.speak = speak_func  # Assign the speak function

    def get_news(self, query):
        """Fetch news articles based on a given query."""
        try:
            params = {
                'q': query,         # The search query
                'apiKey': self.api_key,  # Your API key
                'pageSize': 5,      # Number of articles to return
                'language': 'en'    # Language of the articles
            }
            response = requests.get(self.base_url, params=params)

            if response.status_code == 200:
                articles = response.json().get('articles', [])
                if articles:
                    print(f"Here are the latest news articles about '{query}':")
                    for index, article in enumerate(articles, start=1):
                        title = article.get('title')
                        url = article.get('url')
                        print(f"{index}. {title}\n   Read more: {url}\n")

                    # Ask the user if they want to read any article
                    read_choice = input("Would you like to read any of these articles? (Enter the article number or 'no' to skip): ")
                    if read_choice.isdigit() and 1 <= int(read_choice) <= len(articles):
                        selected_article = articles[int(read_choice) - 1]
                        print(f"Opening {selected_article.get('title')} in your browser...")
                        webbrowser.open(selected_article.get('url'))
                        
                        # Read the full article
                        self.read_full_article(selected_article.get('url'))
                    else:
                        print("No articles will be opened.")
                else:
                    print(f"No articles found for '{query}'.")
            else:
                print(f"Failed to fetch news articles. Status code: {response.status_code}")

        except Exception as e:
            print(f"An error occurred while fetching news: {e}")

    def read_full_article(self, url):
        """Read the full content of the article aloud using pyttsx3."""
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract the article content; this might need to be customized based on the news site's structure
            paragraphs = soup.find_all('p')
            article_text = ' '.join([para.get_text() for para in paragraphs])
            
            # Use the speak function passed during initialization
            self.speak(article_text)

        else:
            print(f"Failed to fetch the article content. Status code: {response.status_code}")

class JokeSearcher:
    def __init__(self):
        self.api_url = "https://official-joke-api.appspot.com/jokes/random"
        self.running = True  # Attribute to control the infinite loop

    def fetch_joke(self):
        """Fetches a random joke from the API."""
        try:
            response = requests.get(self.api_url)
            if response.status_code == 200:
                joke_data = response.json()
                joke = f"{joke_data['setup']} ... {joke_data['punchline']}"
                print(joke)
                return joke
            else:
                print("Failed to fetch a joke.")
                return None
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def stop(self):
        """Method to stop fetching jokes in a loop."""
        self.running = False
        print("Stopping the joke searcher...")

    def start_joke_loop(self):
        """Runs a loop to continuously fetch jokes until stopped."""
        while self.running:
            joke = self.fetch_joke()
            if joke:
                print(f"Joke: {joke}")
            else:
                print("No joke fetched.")