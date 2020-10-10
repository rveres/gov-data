import urllib.request
import json
import sys


def federal_register_document_api_json(request):
    if request is None or request == "":
        raise ValueError("Invalid request argument provided to parser.")

    # Base API URL for requesting data from the United States Federal Register
    base_api_url = "https://www.federalregister.gov/api/v1/documents.json?conditions%5Bterm%5D="
    custom_query_url = base_api_url + request

    # Try to download JSON data from Federal Register API
    with urllib.request.urlopen(custom_query_url) as response:
        try:
            raw_downloaded_json = response.read()
        except:
            print("Error when downloading JSON from Federal Register API: ", sys.exec_info()[0])
            raise

    print(raw_downloaded_json)


if __name__ == '__main__':
    federal_register_document_api_json("boeing")
