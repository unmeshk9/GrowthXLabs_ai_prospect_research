from scraping import scrape_company_website
from mock_data import get_mock_twitter_data, get_mock_financial_data
from generate_summary import generate_mock_company_summary

if __name__ == "__main__":
    url = 'https://example.com'
    company_data = scrape_company_website(url)
    twitter_data = get_mock_twitter_data()
    financial_data = get_mock_financial_data()
    
    summary = generate_mock_company_summary(company_data, twitter_data, financial_data)
    print(summary)