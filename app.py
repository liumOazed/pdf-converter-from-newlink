from src.helper import scrape_article, create_pdf
# Main function to run the scraper
def main():
    news_url = 'https://www.bloomberg.com/opinion/articles/2024-08-20/markets-rebound-like-they-re-on-a-mission-from-nevermind'
    pdf_filename = 'news_article_bloomberg_market_rebound.pdf'
    
    text_content, image_urls = scrape_article(news_url)
    create_pdf(text_content, image_urls, pdf_filename)
    print(f"PDF created: {pdf_filename}")