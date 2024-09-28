import requests
from bs4 import BeautifulSoup

# List of companies with their terms and privacy policy URLs
COMPANIES = {
    "Google Terms": "https://policies.google.com/terms/archive/19990920?hl=en",
    "Apple Terms":  "https://www.apple.com/legal/privacy/en-ww/",
    # "Google Privacy Policy": "https://policies.google.com/privacy",
    # "Facebook Terms": "https://www.facebook.com/terms.php",
    # "Facebook Privacy Policy": "https://www.facebook.com/policy.php",
    # Add more companies and URLs as needed
}

def scrape_terms(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Parsing the page content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting all paragraphs and relevant text
        paragraphs = soup.find_all('p')
        terms_text = "\n".join([para.get_text() for para in paragraphs])

        return terms_text if terms_text else "No terms or conditions found on this page."
    except requests.RequestException as e:
        return f"Error fetching data: {str(e)}"

def main():
    for company, url in COMPANIES.items():
        print(f"Fetching {company} from {url}...\n")
        terms = scrape_terms(url)
        print(f"{company} terms:\n{'-'*80}\n{terms}\n{'-'*80}\n")

if __name__ == "__main__":
    main()
# python3 tools/scrapper.py > terms_output.txt
