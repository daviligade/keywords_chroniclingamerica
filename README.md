
# keywords_chroniclingamerica

This script allows you to search for specific keywords or strings on [Chronicling America](https://chroniclingamerica.loc.gov) and retrieve article metadata. The search leverages the Chronicling America API and retrieves results in JSON format.

## Description

The script fetches and processes results based on your chosen keywords. For each keyword, it performs the following tasks:
1. Sends a request to the Chronicling America API to fetch articles containing the keyword.
2. Extracts key metadata such as titles, URLs, publication details, OCR content, and more.
3. Processes and prints a detailed summary of each article.

## Requirements

- Python 3.x
- `requests` library (`pip install requests`)

## Usage

1. **Set your search keywords and results limit:**

   In the script, modify the `TARGET_STRINGS` list with the keywords or strings you wish to search. For example:

   ```python
   TARGET_STRINGS = ["example keyword", "another keyword"]
   ```

   You can also adjust the maximum number of results per keyword by modifying `MAX_RESULTS`:

   ```python
   MAX_RESULTS = 10
   ```

2. **Run the script:**

   ```bash
   python keywords_chroniclingamerica.py
   ```

   The script will search for each keyword in `TARGET_STRINGS`, fetch the articles, and display key details.

## Output Details

For each search result, the script provides the following information:

- **ID**: A unique identifier for the article.
- **URL**: The URL linking directly to the article's available data formats in JSON.
- **Title**: The title of the article.
- **OCR Content**: Text content extracted using OCR (Optical Character Recognition).
- **County**: The county in which the article was published.
- **Edition**: The edition information of the publication.
- **Frequency**: How frequently the publication is issued.
- **Subject**: A list of subjects associated with the article.
- **City**: The city of publication.
- **Date**: The date of publication.
- **Start Year**: The starting year of the publication.
- **End Year**: The year when the publication ceased.
- **Note**: Additional notes associated with the article.
- **State**: The state where the article was published.
- **Section Label**: The section label, if applicable.
- **Type**: The type of the publication (e.g. "page").
- **Place of Publication**: The place of publication.
- **Edition Label**: Additional edition labeling details.
- **Publisher**: The publisher of the article.
- **Language**: The language of the article.
- **Alternate Titles**: Alternate titles associated with the publication.
- **LCCN**: The Library of Congress Control Number.
- **Country**: The country of publication.
- **Image URL**: A link to the image of the article in `.jp2` format.

## Example URL Formats

- **Fetching all articles containing a keyword**:
  ```
  https://chroniclingamerica.loc.gov/search/pages/results/?proxtext=my%20string&rows=20&format=json
  ```
  Replace `my%20string` with your desired search keyword, where `%20` represents a space.

- **Accessing data types**:
  - All available types: `https://chroniclingamerica.loc.gov/lccn/sn90065065/1905-08-05/ed-1/seq-1.json`
  - OCR text: `https://chroniclingamerica.loc.gov/lccn/sn90065065/1905-08-05/ed-1/seq-1/ocr.txt`
  - Image: `https://chroniclingamerica.loc.gov/lccn/sn90065065/1905-08-05/ed-1/seq-1.jp2`

## Notes

- The script fetches results using a GET request to the Chronicling America API with parameters like keyword, number of results, and response format.
- It extracts metadata from the API response and formats it for easy reading.
- **Useful links**:
  - https://chroniclingamerica.loc.gov/about/api/
  - https://github.com/LibraryOfCongress/data-exploration/tree/master
  - https://guides.loc.gov/digital-scholarship/accessing-digital-materials#s-lib-ctab-26648178-2
