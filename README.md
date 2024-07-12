<h1>Webscraping Project</h1>

Overview
The Webscraping project is designed for scraping and analyzing web content programmatically. It leverages Python's requests and BeautifulSoup libraries to fetch and parse HTML content from websites, enabling users to extract specific data for various applications such as data analysis, research, or automation tasks.

Features
- Perform Google searches and retrieve links.
- Fetch HTML content from retrieved links.
- Save scraped data as HTML files locally.
- Handle HTTP errors and exceptions gracefully.

Installation
To use the Webscraping project, follow these steps:

1. Clone the repository:
   git clone https://github.com/your_username/webscraping.git
   cd webscraping

2. Install dependencies:
   pip install -r requirements.txt

Usage
1. Set up your Google Custom Search API credentials:
   - Obtain an API key and a Custom Search Engine ID from Google.

2. Update the api_key and cx variables in the main.py script with your credentials.

3. Run the script:
   python main.py

4. Enter a search query when prompted and observe the output.

Configuration
Ensure you have set up your Google Custom Search API credentials correctly in main.py before running the script.

Credits
- Requests: HTTP library for Python.
- BeautifulSoup: Library for parsing HTML and XML documents.

