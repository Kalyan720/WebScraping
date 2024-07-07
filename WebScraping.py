import os
import requests
from bs4 import BeautifulSoup

def Google_search(query, api_key, cx):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        
        data = response.json()
        search_results = [item['link'] for item in data.get('items', [])]
        
        if search_results:
            print("Search results:\n")
            for link in search_results:
                print(link)
            web_page(search_results)
        else:
            print("No search results found.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching search results: {e}")
    
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error fetching search results: {e}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def web_page(links):
    for i, link in enumerate(links):
        try:
            response = requests.get(link)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
            
            if response.status_code == 200:
                print(f"\nThe Link: '{link}' is accessible.")
                scraped_data = BeautifulSoup(response.text, "html.parser")
                
                filename = f"scraped_content_{i}.html"
                if not os.path.exists(filename):
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(str(scraped_data))
                    print(f"Scraped data is saved to '{filename}'")
                else:
                    print(f"File '{filename}' already exists, skipping.")
            
            else:
                print(f"\nFailed to fetch '{link}'. Status code: {response.status_code}")
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching '{link}': {e}")
        
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error fetching '{link}': {e}")
        
        except Exception as e:
            print(f"An error occurred while fetching '{link}': {e}")

if __name__ == "__main__":
    api_key = "-_-"
    cx = "-_-"
    query = input("Enter the Google search query: ")
    Google_search(query, api_key, cx)
