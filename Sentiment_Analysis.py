# Importing the Libraries
from newspaper import Article
from textblob import TextBlob

# Creating the function for text input
def Input_text():
    txt = input("Enter the text to analyze:")
    blob = TextBlob(txt)
    sentiment = blob.sentiment.polarity
    return sentiment

# Creating the function for link input
def Article_url():
    url = input("Paste the URL here:")

    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    text = article.summary
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment


# Source Code
Running = True
while Running:
    print("\n\n")
    print("Hello, This is a Sentiment Detection Program.")
    print("1. Input text to analyse.")
    print("2. Paste a link to analyze.")
    print("3. Quit.")

    ch = int(input("Enter your choice(1 -3): "))

    if ch == 1:
        print(Input_text())
    elif ch == 2:
        print(Article_url())
    elif ch == 3:
        Running = False
    else:
        print("Invalid choice.")
