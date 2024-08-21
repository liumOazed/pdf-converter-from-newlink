import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

# Function to scrape the news article from the provided URL
def scrape_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting the article content
    article_content = soup.find('div', class_='body-copy')  # Adjust class name based on actual HTML structure
    paragraphs = article_content.find_all('p') if article_content else []
    
    # Collecting text and images
    text_content = []
    images = []
    
    for paragraph in paragraphs:
        text_content.append(paragraph.get_text())
    
    # Extracting images if available
    img_tags = article_content.find_all('img')
    for img in img_tags:
        if 'src' in img.attrs:
            images.append(img['src'])

    return ' '.join(text_content), images

# Function to create a PDF from the scraped article
def create_pdf(text, images, pdf_filename):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Splitting text into chunks of approximately 300 words
    words = text.split()
    chunk_size = 300
    for i in range(0, len(words), chunk_size):
        chunk = words[i:i + chunk_size]
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, ' '.join(chunk))
        
        # Add images if available
        if i // chunk_size < len(images):
            pdf.add_page()
            pdf.image(images[i // chunk_size], x=10, y=10, w=180)  # Adjust position and size as needed
            pdf.add_page()  # Add a new page after the image

    pdf.output(pdf_filename)