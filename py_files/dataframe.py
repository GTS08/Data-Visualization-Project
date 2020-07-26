import pandas as pd # Analyze data
import calendar # Get the months
import sqlite3 # Manage the datatbase


def total_arrivals():
    print("Calculating Total Arrivals...")

    # Connect to database
    conn = sqlite3.connect("../tourism.db")

    # Get the dataframe from the database
    df = pd.read_sql_query("SELECT * FROM statistics", conn)
    
    # Get the total arrivals for each year
    total_df = pd.DataFrame({"Total Arrivals" : df.groupby(by = "Year")[["Air", "Railway", "Sea", "Road"]].sum().sum(axis=1)}).reset_index()

    # Close the connection
    conn.close()

    print("Done.")

    return total_df


def total_arrivals_by_country():
    print("Calculating Total Arrivals by Country...")

    # Connect to database
    conn = sqlite3.connect("../tourism.db")

    # Get the dataframe from the database
    df = pd.read_sql_query("SELECT * FROM statistics", conn)
    
    # Get the total arrivals for each year
    total_df = pd.DataFrame({"Total Arrivals" : df.groupby(by = "Country")[["Air", "Railway", "Sea", "Road"]].sum().sum(axis=1)}).reset_index()
    
    # Sort values by total arrivals
    total_df = total_df.sort_values(by = ["Total Arrivals"], ascending = False).head(4)

    # Close the connection
    conn.close()

    print("Done.")

    return total_df


def total_arrivals_by_means_of_transport():
    print("Calculating Total Arrivals by Means of Transport...")

    # Connect to database
    conn = sqlite3.connect("../tourism.db")

    # Get the dataframe from the database
    df = pd.read_sql_query("SELECT * FROM statistics", conn)
    
    # Get the total arrivals for each year
    total_df = pd.DataFrame({"Total Arrivals" : df[["Air", "Railway", "Sea", "Road"]].sum()}).reset_index()

    # Rename the column
    total_df = total_df.rename(columns = {"index":"Means of Transport"})
    
    # Sort values by total arrivals
    total_df = total_df.sort_values(by = ["Total Arrivals"], ascending = False)

    # Close the connection
    conn.close()

    print("Done.")

    return total_df


def total_arrivals_by_quarter():
    print("Calculating Total Arrivals by Quarter...")

    # Connect to database
    conn = sqlite3.connect("../tourism.db")

    # Get the dataframe from the database
    df = pd.read_sql_query("SELECT * FROM statistics", conn)

    # Add quarter column
    df["Quarter"] = ""

    # Make the dataframe
    total_df = pd.DataFrame(df)

    # Update the quarter column
    for month in calendar.month_name:
        if month in calendar.month_name[1:4]:
            total_df.loc[total_df["Month"] == month, "Quarter" ] = "Q1"
        elif month in calendar.month_name[4:7]:
            total_df.loc[total_df["Month"] == month, "Quarter" ] = "Q2"
        elif month in calendar.month_name[7:10]:
            total_df.loc[total_df["Month"] == month, "Quarter" ] = "Q3"
        elif month in calendar.month_name[10:13]:
            total_df.loc[total_df["Month"] == month, "Quarter" ] = "Q4"

    # Get the total arrivals for each year's quarter
    total_df = pd.DataFrame({"Total Arrivals" : df.groupby(by = ["Year", "Quarter"])[["Air", "Railway", "Sea", "Road"]].sum().sum(axis=1)}).reset_index()

    print("Done.")

    return total_df


# Export csv file from pandas' dataframe
def export_to_csv(df, csv_name):
    print("Exporting " + csv_name + "...")
    csv_path = "../csv_files/" + csv_name # Path to store the csv file
    df.to_csv(csv_path, index = False) # Save the csv file
    print("Done.")
