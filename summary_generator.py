def generate_mock_company_summary(company_data, twitter_data, financial_data):
    summary = f"Company Overview: {company_data['overview']}\n"
    summary += f"Products/Services: {', '.join(company_data['products'])}\n"
    summary += f"Recent News: {', '.join(company_data['news'])}\n"
    summary += f"Contact Info: {company_data['contact']}\n"
    summary += f"Twitter Data: {', '.join(twitter_data)}\n"
    summary += f"Financial Data: Company Size - {financial_data['company_size']}, Funding - {financial_data['funding']}, Revenue - {financial_data['revenue']}"
    return summary