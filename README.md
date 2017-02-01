# Codeforces-Contest-Scraper
Downloads Contest problems and tutorials

The scraper does the following:
  1. Makes a Problem Set folder
  2. Requests for the range of contest IDs the user wants to download
  3. Maintains a text file which tracks whether the requested contest has already been downloaded
  4. Creates separate folders for each valid contest and downloads all the problems and tutorials as PDFs. Note that all Codeforces contests don't have tutorials
  
Run by executing runner.py
It is a Python3 file

Requirements: Python3;
              Python libraries: bs4, requests, os, pdfkit; 
              Application: wkhtmltopdf

Created by Ritwik Saha
