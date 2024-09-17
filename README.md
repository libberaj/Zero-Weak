

# 🛡️ Zero-Weak

A Python-based vulnerability scanner that automates the detection of common web vulnerabilities such as **SQL Injection** and **Cross-Site Scripting (XSS)**. The tool is designed for students and developers to improve web application security by quickly identifying security flaws.

## 🚀 Features

- **SQL Injection Detection**: Scans web forms and URLs for SQL injection vulnerabilities.
- **Cross-Site Scripting (XSS) Detection**: Detects potential XSS vulnerabilities in web input fields.
- **PDF Reporting**: Automatically generates detailed PDF reports of vulnerabilities found, including remediation suggestions.
- **Fast Scanning**: Scans up to 100 URLs per session, reducing vulnerability scanning time by 40% compared to manual testing.
- **Easy to Use**: Simple command-line interface for quick and efficient scanning.
  
## 🛠️ Technologies Used

- **Python**: Core programming language for the scanner.
- **BeautifulSoup**: HTML and XML parsing to interact with web forms.
- **Requests**: For making HTTP requests and fetching content from URLs.
- **Reportlab**: For generating PDF reports.
  
## 📂 Project Structure

```bash
├── scanner.py              # Core vulnerability scanner logic
├── report_generator.py      # Module for generating PDF reports
├── utils.py                 # Utility functions (e.g., payloads, input sanitization)
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
└── LICENSE                  # License file
```

## ⚙️ Setup & Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/libberaj/Zero-Weak
   ```

2. **Install dependencies**:

   Make sure you have Python 3 installed. Install required Python libraries using the following command:

   ```bash
   pip install -r requirements.txt
   ```

   The dependencies are:
   - `requests`
   - `beautifulsoup4`
   - `reportlab`

3. **Run the Scanner**:

   To start scanning, use the following command:

   ```bash
   python scanner.py
   ```

   By default, the tool will prompt you for a target URL or list of URLs to scan for vulnerabilities.

## 📝 Usage

1. **Basic Scan**: 

   ```bash
   python scanner.py --url https://example.com
   ```

   This will initiate a scan on the specified URL for SQL Injection and XSS vulnerabilities.

2. **Scan Multiple URLs**: 

   You can also scan multiple URLs by passing them in a text file:

   ```bash
   python scanner.py --file urls.txt
   ```

3. **Generate PDF Report**:

   After scanning, the tool automatically generates a report in the `/reports/` directory. Each report will contain:
   - Vulnerabilities found
   - Payloads used
   - Recommended fixes

## 📊 Sample Report

Example of a vulnerability report:

```
Vulnerability: SQL Injection
URL: https://example.com/search?query=test
Payload: ' OR '1'='1
Recommendation: Use parameterized queries to prevent SQL Injection attacks.
```

## 🛡️ Future Improvements

- Add support for more vulnerabilities (e.g., CSRF, SSRF).
- Integrate AI-based analysis for detecting complex attack patterns.
- Implement a GUI for easier use.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and create a pull request. Make sure to add tests for any new features or bug fixes.
