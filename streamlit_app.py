import requests
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
  # Use streamlit to parse the HTML
  soup = st.html(html)

  # Find all the h3 elements with the class "LC
