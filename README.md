# Amazon Web Scraper

This Python project scrapes product information from Amazon, including product names, prices, and links. The data is collected using **Selenium** and saved into a CSV file for easy analysis.

## Features
- Scrapes product names, prices, and links from Amazon search results.
- Navigates through multiple pages of search results.
- Stores the data in a CSV file.

## Requirements

To run this project, you'll need the following:
- **Python 3.x**
- **Selenium**: A web automation tool to interact with browsers.
- **Geckodriver**: The driver needed to run **Firefox** with Selenium.

### Python Packages
You can install the required Python package by running:
```
pip install selenium
```

### Web Browser and Driver
- **Firefox**: This script uses the Firefox web browser.
- **Geckodriver**: Download the geckodriver for your operating system, and make sure it's in your system's PATH.

### How to Use
### 1. **Clone the repository**:
```
git clone https://github.com/prash0099/amazon-web-scraper.git
cd amazon-web-scraper
```

### 2. **Install dependencies**: 
Install the Selenium package using pip:
```
pip install selenium
```

### 3. **Set up Geckodriver**:
- Download [geckodriver](https://github.com/mozilla/geckodriver) and ensure it’s in your system’s PATH.
- Alternatively, place the `geckodriver` executable in the same directory as the script.

### 4. **Run the Script**: 
Run the script by using the following command:
```
python scraping_amazon.py
```
The script will scrape product data for a specified product (in this case, laptops) and save it to a CSV file (`scraped_product_data.csv`).

### 5. **Change Product**: 
You can change the product being scraped by modifying the product variable inside the script:
```
product = 'laptop'  # Change this to any product name you want to search
```

### 6. **CSV Output&**:
The output will be saved in a file named `scraped_product_data.csv` with the following columns:
- Product Name
- Price
- Product Link

## Error Handling
- The script uses `try-except` blocks to handle cases where some product details (name, price, or link) may be missing.

## Disclaimer
- Amazon's Terms of Service: Web scraping may violate Amazon’s terms of service, and it's important to respect the site's rules. This project is for educational purposes only.
- Legal Note: Make sure you understand the legal and ethical implications of web scraping before using this project for anything other than learning.

## License
- This project is licensed under the MIT License - see the [LICENSE](https://github.com/prash0099/amazon-web-scraper/blob/main/MIT%20License) file for details.
