# HugChat Web Scraping and Chatbot Interaction

This repository contains Python code that utilizes the HugChat library to perform web scraping and interact with a chatbot. The code allows you to scrape data from a website and have a conversation with a chatbot using a typewriter effect for a fun and interactive experience.

## Prerequisites

Before running the code, make sure you have the following libraries installed:

- `hugchat`: This library is used for interacting with the HugChat API.
- `requests`: Used for making HTTP requests to the specified website.
- `bs4` (Beautiful Soup 4): Used for parsing HTML content.
- `flask`: Required for setting up a local web server for interaction.

You can install these dependencies using pip:

```bash
pip install hugchat requests beautifulsoup4 flask
```

Getting Started

```bash
python app.py
```
## Usage

Upon running the script, you will be able to interact with the web scraper and chatbot. Here's how it works:

1. The program starts with a greeting message from the chatbot.

2. You can type your queries or commands, and the chatbot will respond.

3. To perform web scraping, use the dedicated command "PWS" (stands for Perform Web Scraping). Enter the URL of the website you want to scrape, and the bot will scrape data from it.

4. The bot will then provide a sensible and meaningful interpretation of the scraped data.

5. You can continue the conversation with the bot by asking more questions or typing other commands.

6. To exit the program, you can type commands like "close," "no," "bye," or "off."

## Note

- Some websites may block web scraping, so the results may not be as expected.

- If the program encounters an error during scraping, it will prompt you to enter the URL again.

- The typewriter effect is used for a more engaging user experience.

## Contributing

Feel free to contribute to this project by submitting pull requests or reporting issues.

