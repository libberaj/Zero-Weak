import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Function to test SQL Injection
def test_sql_injection(url):
    payload = "' OR '1'='1"
    response = requests.get(url + payload)
    if "error" in response.text:
        return ("SQL Injection", url, f"Payload: {payload}")
    return None

# Function to test XSS
def test_xss(url):
    payload = "<script>alert('XSS')</script>"
    response = requests.get(url + payload)
    if payload in response.text:
        return ("XSS", url, f"Payload: {payload}")
    return None

# Function to generate PDF report
def generate_pdf_report(results, filename='vulnerability_report.pdf'):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    
    data = [['Vulnerability Type', 'URL/IP', 'Details']]
    for result in results:
        data.append(result)
    
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    elements = [table]
    doc.build(elements)

# Example usage
def run_scanner(urls):
    results = []
    for url in urls:
        result = test_sql_injection(url)
        if result:
            results.append(result)
        result = test_xss(url)
        if result:
            results.append(result)
    generate_pdf_report(results)

# Define target URLs
urls = ["http://example.com/login", "http://example.com/search"]
run_scanner(urls)
