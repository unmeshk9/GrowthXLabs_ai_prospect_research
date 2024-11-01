import requests
from bs4 import BeautifulSoup

def scrape_company_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    overview = soup.find('meta', {'name': 'description'})
    overview_text = overview['content'] if overview else 'No overview available'
    
    products = [item.get_text() for item in soup.find_all('div', class_='product')]
    news = [article.get_text() for article in soup.find_all('article')]
    contact = soup.find('a', href=True, text=lambda t: 'contact' in t.lower())
    contact_info = contact['href'] if contact else 'No contact information available'
    
    return {
        'overview': overview_text,
        'products': products,
        'news': news,
        'contact': contact_info
    }
