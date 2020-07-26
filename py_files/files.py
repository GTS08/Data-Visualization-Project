from bs4 import BeautifulSoup # Scrap urls from webpages
import urllib.request # Make url requests
import requests # Open and store files from urls
import calendar # Get the months
import sqlite3 # Manage a database
import xlrd # Read excel files
import os # Manage directories
import re # Regeular expressions


# Download and store excel files
def download():
    # The main url to get download links
    main_url = "https://www.statistics.gr/en/statistics/-/publication/STO04/201X-Q4"

    for year in range(1, 5):
        new_url = main_url.replace("X", str(year)) # Change the year

        file_name = new_url.split("/")[-1] + ".xls" # Get the file name
        print("Downloading " + file_name + "...")
        
        # Open the corresponding page
        html_page = urllib.request.urlopen(new_url)

        # Parse the page
        soup = BeautifulSoup(html_page, "html.parser")

        # Find the first "a" tag with the given text
        link = soup.find("a", text="Arrivals of non-residents from abroad, by country of residence and by means of transport ")

        # Get the download link from the page
        url = link.get("href")

        # Get the relative path filename in respect to cwd
        rel_path_filename = "../" + "excel_files" + "/" + file_name

        # Open the link, download the file and store it in the given folder
        r = requests.get(url, allow_redirects=True)
        open(rel_path_filename, "wb+").write(r.content)

    print("All files downloaded.")


# Export the necessary information from excel files to database
def export_to_db():
    print("Exporting to database...")

    # Create/connect to database
    conn = sqlite3.connect("../tourism.db")

    # All excel files
    excel_files = os.listdir("../excel_files/")

    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS statistics
                (Country TEXT, Air REAL, Railway REAL, Sea REAL, Road REAL, Month TEXT, Year INTEGER, unique(Country, Month, Year))''')

    # For every excel file
    for excel_file in excel_files:

        path = "../excel_files/" + excel_file

        # Open the file and get the sheets
        book = xlrd.open_workbook(path)

        # For every sheet within excel file
        for i, sheet in enumerate(book.sheets()):
            shown = 0
            # Get the first table of the sheet and add it to database
            for row_num in range(sheet.nrows):
                    row_value = sheet.row_values(row_num)
                    if row_value[0] == " - EUROPEAN UNION":
                        shown += 1
                    r = re.compile(r"\d.")
                    if shown == 1 and r.match(row_value[0]):
                        c.execute("INSERT INTO statistics VALUES (?, ?, ?, ?, ?, ?, ?)", 
                                 (row_value[1], row_value[2], row_value[3], row_value[4], row_value[5], calendar.month_name[i+1], excel_file.split("-")[0]))
                    if shown == 2:
                        break
    
    # Fix empty values
    means_of_transport = ["Air", "Railway", "Sea", "Road"]
    for mean in means_of_transport:
        c.execute("UPDATE statistics SET {} = 0 WHERE {} = ''".format(mean, mean))


    conn.commit() # Commit changes

    conn.close() # Close connection

    print("Done.")
