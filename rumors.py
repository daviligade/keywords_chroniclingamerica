import requests

# SETTINGS - list of strings to search and max number of results you want
TARGET_STRINGS = ["my string", "other string"]
MAX_RESULTS = 2

def fetch_results(the_string, max_results=2):
    """
    Fetches results from the Chronicling America API for a given the_string.
    
    Parameters:
        the_string (str): The the_string to search for.
        max_results (int): Max number of results to fetch per request. Defaults to 2.
    
    Returns:
        list: A list of results for the given the_string.
    """
    base_url = "https://chroniclingamerica.loc.gov/search/pages/results/"
    params = {
        "proxtext": the_string,
        "rows": max_results,
        "format": "json"
    }
    
    response = requests.get(base_url, params=params) # resulting in "https://chroniclingamerica.loc.gov/search/pages/results/?proxtext=my%20string&rows=20&format=json"
    
    if response.status_code == 200:
        data = response.json()
        return data.get('items', [])  # Extracting the list of items from the response
    else:
        print(f"Failed to fetch results for keyword: {the_string}")
        return []

def process_results(results):
    """
    Processes a list of results and prints key details.
    
    Parameters:
        results (list): List of result items to process.
    """
    if results:
        for i, item in enumerate(results, start=1):

            base_url = "https://chroniclingamerica.loc.gov"
            id= item.get('id', 'N/A')
            url= item.get('url', 'N/A')
            title= item.get('title', 'N/A')
            the_content = item.get('ocr_eng', '') # all the text
            edition= item.get('edition', 'N/A')
            county = item.get('county', [None])
            frequency= item.get('frequency', 'N/A')
            subject = item.get('subject', [])
            city = item.get('city', [None])
            date= item.get('date', 'N/A')
            start_year= item.get('start_year', 'N/A')
            end_year= item.get('end_year', 'N/A')
            note = item.get('note', [])
            state = item.get('state', [None])
            section_label= item.get('section_label', 'N/A')
            the_type= item.get('type', 'N/A')
            place_of_publication= item.get('place_of_publication', 'N/A')
            edition_label= item.get('edition_label', 'N/A')
            publisher= item.get('publisher', 'N/A')
            language = item.get('language', [])
            alternate_titles = item.get('alt_title', [])
            lccn= item.get('lccn', 'N/A')
            country= item.get('country', 'N/A')
            image_url = base_url+id.rstrip("/")+".jp2"
            print(f"Result {i}:")
            print(f"  ID: {id}")
            print(f"  URL: {url}")
            print(f"  Title: {title}")
            print(f"  OCR Content: {the_content}")
            print(f"  County: {county}")
            print(f"  Edition: {edition}")
            print(f"  Frequency: {frequency}")
            print(f"  Subject: {subject}")
            print(f"  City: {city}")
            print(f"  Date: {date}")
            print(f"  Start Year: {start_year}")
            print(f"  End Year: {end_year}")
            print(f"  Note: {note}")
            print(f"  State: {state}")
            print(f"  Section Label: {section_label}")
            print(f"  Type: {the_type}")
            print(f"  Place of Publication: {place_of_publication}")
            print(f"  Edition Label: {edition_label}")
            print(f"  Publisher: {publisher}")
            print(f"  Language: {language}")
            print(f"  Alternate Titles: {alternate_titles}")
            print(f"  LCCN: {lccn}")
            print(f"  Country: {country}")
            print(f"  Image URL: {image_url}")
            print("-" * 40)

    else:
        print("No results found")

def main():
    # Loop over each keyword
    for the_string in TARGET_STRINGS:
        print(f"Searching for the_string: '{the_string}'")
        results = fetch_results(TARGET_STRINGS, MAX_RESULTS)
        
        if results:
            print(f"Found {len(results)} results for '{the_string}'")
            process_results(results)
        else:
            print(f"No results found for '{the_string}'")
        print("="*40)

if __name__ == "__main__":
    main()
