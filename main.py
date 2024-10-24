import pyttsx3 as p
import speech_recognition as sr
from selenium_web import WikipediaSearcher, YouTubeSearcher, NewsSearcher, JokeSearcher
from randfacts import get_fact  # Import get_fact directly to use it easily

# Initialize the speech engine
engine = p.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set female voice

def speak(text, emotional_tone='neutral'):
    """Make Vlexa speak with a specified tone."""
    if emotional_tone == 'excited':
        engine.setProperty('rate', 210)  # Faster rate for excitement
    elif emotional_tone == 'calm':
        engine.setProperty('rate', 160)  # Slower rate for calmness
    else:
        engine.setProperty('rate', 190)  # Default rate

    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """Listen and recognize user speech."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.", 'calm')
            return None
        except sr.RequestError:
            speak("Sorry, I'm unable to reach the speech recognition service.", 'calm')
            return None

# Start Vlexa interaction
speak("Hello, my name is Vlexa, and I am your Assistant. How can I help you today?")

# Initialize searcher instances
joke_searcher = JokeSearcher()
google_searcher = GoogleSearcher()

while True:
    action = recognize_speech()
    if action:
        action = action.lower()  # Normalize input

        if "youtube" in action:
            speak("What YouTube video would you like to search for?", 'excited')
            query = recognize_speech()
            if query:
                speak(f"Searching YouTube for {query}", 'excited')
                yt_searcher = YouTubeSearcher()
                yt_searcher.search_video(query)
            else:
                speak("I didn't catch that. Please try again.", 'calm')

        elif "wikipedia" in action:
            speak("What information would you like to search for on Wikipedia?", 'neutral')
            query = recognize_speech()
            if query:
                speak(f"Searching Wikipedia for {query}", 'neutral')
                wiki_searcher = WikipediaSearcher()
                wiki_searcher.search_info(query)
            else:
                speak("I didn't catch that. Please try again.", 'calm')

        elif "news" in action:
            speak("What topic would you like to get news about?", 'neutral')
            query = recognize_speech()
            if query:
                speak(f"Fetching the latest news about {query}", 'neutral')
                news_searcher = NewsSearcher(speak)  # Pass the speak function to read articles
                news_searcher.get_news(query)
            else:
                speak("I didn't catch that. Please try again.", 'calm')

        elif "fact" in action:
            speak("Sure, here's an interesting fact!")
            fact = get_fact()
            print(fact)
            speak(f"Did you know that {fact}")

        elif "joke" in action:
            speak("Let me tell you a joke.", 'excited')
            joke = joke_searcher.fetch_joke()
            if joke:
                speak(joke, 'neutral')
            else:
                speak("I couldn't fetch a joke at the moment.", 'calm')

        elif "stop jokes" in action:
            joke_searcher.stop()
            speak("I have stopped fetching jokes.", 'calm')

        elif "how are you" in action or "how r u" in action:
            speak("I'm just a program, but I'm here to help you!", 'neutral')

        elif "thank you" in action or "thanks" in action or "thank u" in action:
            speak("You're welcome! If you need anything else, just ask!", 'neutral')

        else:
            speak("I'm sorry, I didn't understand that. Could you please rephrase?", 'calm')
    else:
        speak("I didn't catch that. Please try again.", 'calm')
