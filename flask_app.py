from flask import Flask, request, render_template_string
from scraping import scrape_company_website
from mock_data import get_mock_twitter_data, get_mock_financial_data
from generate_summary import generate_mock_company_summary

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    if request.method == 'POST':
        url = request.form['url']
        company_data = scrape_company_website(url)
        twitter_data = get_mock_twitter_data()
        financial_data = get_mock_financial_data()
        summary = generate_mock_company_summary(company_data, twitter_data, financial_data)
    return render_template_string('''
        <form method="post">
            Company URL: <input type="text" name="url">
            <input type="submit" value="Generate Summary">
        </form>
        <pre>{{ summary }}</pre>
    ''', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
