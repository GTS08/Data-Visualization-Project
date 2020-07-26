import matplotlib.pyplot as plt # Create diagrams
import pandas as pd # Analyze data
import textwrap as tw # Text wrapping

# Diagram for total arrivals
def export_total_arrivals(df, diagram_name):
    print("Exporting " + diagram_name + "...")
    rel_path_filename = "../diagrams/" + diagram_name
    df.plot(kind = "bar", x = "Year", y = "Total Arrivals", title = "Total Arrivals in 2011-2014", legend = False) # Plotting the dataframe
    plt.style.use("seaborn-dark") # Color style
    plt.ylabel("Total Arrivals") # Label for y axis
    plt.xlabel("Years") # Label for x axis
    plt.xticks(rotation = 0) # Rotation for x axis' labels
    plt.tight_layout() # Fit labels
    plt.savefig(rel_path_filename) # Save the diagram
    print("Done.")


# Diagram for total arrivals by country
def export_total_arrivals_by_country(df, diagram_name):
    print("Exporting " + diagram_name + "...")
    rel_path_filename = "../diagrams/" + diagram_name
    df.plot(kind = "bar", x = "Country", y = "Total Arrivals", title = "Total Arrivals by Country in 2011-2014", legend = False) # Plotting the dataframe
    plt.style.use("seaborn-dark") # Color style
    plt.ylabel("Total Arrivals") # Label for y axis
    plt.xlabel("Countries") # Label for x axis

    text = '''\
    Note: Other European Countries are European countries besides Austria, Belgium, Bulgaria, Denmark, Estonia, Ireland, 
    Spain, Italy, Croatia, Cyprus, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Hungary, Poland, Portugal, 
    Romania, Slovakia, Slovenia, Sweden, Czech Republic, Finland, Albania, Switzerland, Norway, Iceland, Russia, Servia.
    '''

    # Format the text
    fig_txt = tw.fill(tw.dedent(text.rstrip()), width=80)

    # Place the text
    plt.figtext(0.5, -0.12, fig_txt, horizontalalignment = "center",
                fontsize = 8, multialignment = "left",
                bbox=dict(boxstyle = "round", facecolor = "#D8D8D8",
                        ec = "0.5", pad = 0.5, alpha = 1), fontweight = "bold")

    plt.xticks(rotation = 45) # Rotation for x axis' labels
    plt.tight_layout() # Fit labels
    plt.savefig(rel_path_filename, bbox_inches = "tight") # Save the diagram
    print("Done.")



# Diagram for total arrivals by means of transport
def export_total_arrivals_by_means_of_transport(df, diagram_name):
    print("Exporting " + diagram_name + "...")
    rel_path_filename = "../diagrams/" + diagram_name
    df.plot(kind = "bar", x = "Means of Transport", y = "Total Arrivals", title = "Total Arrivals by Means of Transport in 2011-2014", legend = False) # Plotting the dataframe
    plt.style.use("seaborn-dark") # Color style
    plt.ylabel("Total Arrivals") # Label for y axis
    plt.xlabel("Means of Transport") # Label for x axis
    plt.xticks(rotation = 0) # Rotation for x axis' labels
    plt.tight_layout() # Fit labels
    plt.savefig(rel_path_filename) # Save the diagram
    print("Done.")


# Diagram for total arrivals by quarter
def export_total_arrivals_quarter(df, diagram_name):
    print("Exporting " + diagram_name + "...")
    rel_path_filename = "../diagrams/" + diagram_name
    df.pivot("Year", "Quarter", "Total Arrivals").plot(kind="bar", title = "Total Arrivals by Quarter in 2011-2014") # Plotting the dataframe
    plt.style.use("seaborn-dark") # Color style
    plt.ylabel("Total Arrivals") # Label for y axis
    plt.xlabel("Years") # Label for x axis
    plt.xticks(rotation = 0) # Rotation for x axis' labels
    plt.tight_layout() # Fit labels
    plt.savefig(rel_path_filename) # Save the diagram
    print("Done.")
