# Xiaomi Georgia Online Shop Scraper

This Python project involves scraping product data from the Xiaomi Georgia online shop and saving it to an Excel file. The script extracts product information such as names, prices, descriptions, and URLs from multiple pages on the website.

## Overview

The script performs the following tasks:
1. **Scrapes Product URLs**: Collects product URLs from multiple pages of the online shop.
2. **Extracts Product Details**: Fetches details like name, price, description, and URL for each product.
3. **Writes Data to Excel**: Saves the extracted data into an Excel file for further analysis.

## Requirements

Ensure you have the following Python packages installed:
- `requests`
- `beautifulsoup4`
- `xlsxwriter`
- `lxml`
- `time` (for sleeping between requests)
