pip install requests beautifulsoup4 streamlit
import requests
from bs4 import BeautifulSoup
import streamlit as st

def find_prospects(industry, area):
  # Set the search URL
  search_url = f"https://www.google.com/search?q={industry}+companies+in+{area}"

  # Send the request and get the response
  response = requests.get(search_url)

  # Check the status code of the response
  if response.status_code == 200:
    # Extract the companies from the search results
    companies = extract_companies_from_search_results(response.text)

    # Generate an HTML table containing the search results
    html = generate_html_table(companies)

    # Return the HTML code
    return html
  else:
    # Return an error message if the request failed
    return f"An error occurred: {response.status_code}"

def extract_companies_from_search_results(html):
  # Use BeautifulSoup to parse the HTML
  soup = BeautifulSoup(html, "html.parser")

  # Find all the h3 elements with the class "LC20lb"
  h3_elements = soup.find_all("h3", class_="LC20lb")

  # Extract the company names from the h3 elements
  companies = [element.text for element in h3_elements]

  return companies

def generate_html_table(companies):
  # Create the HTML table header
  html = "<table>"
  html += "<tr><th>Company</th></tr>"

  # Add a row for each company
  for company in companies:
    html += f"<tr><td>{company}</td></tr>"

  # Close the HTML table
