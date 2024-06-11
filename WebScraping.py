import requests
from bs4 import BeautifulSoup

#Function to create a custom search engine with Google API key.

def Google_search(query, api_key, cx):

    #Accessing the customised search engine using the Args query, api_key, cx.
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        search_results = [item['link'] for item in data.get('items', [])]      
        if search_results:
            print("Search results:\n")
            for link in search_results:
                print(link)
            web_page(search_results)
        else:
            print("No search results found.")
    else:
        print(f"Failed to fetch search results. Status code: {response.status_code}")

#Function to scrape individual links obtained from the search engine.

def web_page(links):

    for i, link in enumerate(links):
        try:
            response = requests.get(link)           
            if response.status_code == 200:
                print(f"\nThe Link: '{link}' is accessible.")
                scraped_data = BeautifulSoup(response.text, "html.parser")
                # Writing the scraped data to a file
                with open(f"scraped_content_{i}.html", "w", encoding="utf-8") as file:
                    file.write(str(scraped_data))
                print(f"Scraped data is saved to 'scraped_content_{i}.html'")
            else:
                print(f"\nFailed to fetch '{link}'. Status code: {response.status_code}")
        except Exception as e:
            print(f"\nAn error occurred while fetching '{link}': {e}")

if __name__ == "__main__":
    #API key to access search engine.
    api_key = "-_-"

    #id of custom google search engine.
    cx = "-_-"

    query = input("Enter the Google search query: ")
    Google_search(query, api_key, cx)


"""Thus we successfully scrape the web page urls on google.com and open individual urls and scrape the data,
   store everything in document format as results. """
