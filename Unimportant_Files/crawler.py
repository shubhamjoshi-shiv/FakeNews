import requests
import argparse
import time
import json
import io
import gzip
import csv
import codecs

from bs4 import BeautifulSoup

import sys

domain = "https://timesofindia.indiatimes.com/us"

# list of available indices
index_list = ["2020-45"] #october 2020

#
# Searches the Common Crawl Index for a domain.
#
def search_domain(domain):

    record_list = []

    print ("[*] Trying target domain: %s" % domain)
    for index in index_list:
        print ("[*] Trying index %s" % index)

        cc_url  = "http://index.commoncrawl.org/CC-MAIN-%s-index?" % index
        cc_url += "url=%s&output=json" % domain

        response = requests.get(cc_url)

        if response.status_code == 200: # if the api call returns data successfully

            records = response.content.splitlines()

            for record in records:
                record = json.loads(record)
                if record["status"] == "200": # if the record contains the link to the required archive
                    record_list.append(record)

            print ("[*] Added %d results." % len(records))


    print ("[*] Found a total of %d hits." % len(record_list))

    return record_list

#
# Downloads a page from Common Crawl
#
def download_page(record):

    offset, length = int(record['offset']), int(record['length'])
    offset_end = offset + length - 1

    # We'll get the file via HTTPS so we don't need to worry about S3 credentials
    # Getting the file on S3 is equivalent however - you can request a Range
    prefix = 'https://commoncrawl.s3.amazonaws.com/'

    # We can then use the Range header to ask for just this set of bytes
    resp = requests.get(prefix + record['filename'], headers={'Range': 'bytes={}-{}'.format(offset, offset_end)})

    # The page is stored compressed (gzip) to save space
    # We can extract it using the GZIP library
    f = gzip.GzipFile(fileobj = io.BytesIO(resp.content))
##
##    # What we have now is just the WARC response, formatted:
    data = f.read().decode("utf-8")

    response = ""

    if len(data):
        try:
            warc, header, response = data.strip().split('\r\n\r\n', 2)
        except:
            pass
##
    return response

record_list = search_domain(domain)

for record in record_list:

    html_content = download_page(record)

    print ("[*] Retrieved %d bytes for %s" % (len(html_content),record['url']))
##    print ("content retrieved is ")
##    print(html_content)
