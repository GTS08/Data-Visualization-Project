import dataframe
import diagram
import files
import os

# Get this file directory and set it as cwd
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

files.download()

files.export_to_db()

# Total arrivals for each year
total_arrivals = dataframe.total_arrivals()
dataframe.export_to_csv(total_arrivals, "total_arrivals.csv")
diagram.export_total_arrivals(total_arrivals, "total_arrivals.png")

# Total arrivals by country
total_arrivals_by_country = dataframe.total_arrivals_by_country()
dataframe.export_to_csv(total_arrivals_by_country, "total_arrivals_by_country.csv")
diagram.export_total_arrivals_by_country(total_arrivals_by_country, "total_arrivals_by_country.png")

# Total arrivals by means of transport
total_arrivals_by_means_of_transport = dataframe.total_arrivals_by_means_of_transport()
dataframe.export_to_csv(total_arrivals_by_means_of_transport, "total_arrivals_by_means_of_transport.csv")
diagram.export_total_arrivals_by_means_of_transport(total_arrivals_by_means_of_transport, "total_arrivals_by_means_of_transport.png")

# Total arrivals by each year's quarter
total_arrivals_by_quarter = dataframe.total_arrivals_by_quarter()
dataframe.export_to_csv(total_arrivals_by_quarter, "total_arrivals_by_quarter.csv")
diagram.export_total_arrivals_quarter(total_arrivals_by_quarter, "total_arrivals_by_quarter.png")
