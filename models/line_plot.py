import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def line_plot():
    df = pd.read_csv('./assets/game_data.csv')

    # Drop rows with missing values
    df = df.dropna()

    # Convert 'Year_of_Release' to integer
    df['Year'] = df['Year'].astype(int)

    # Group the DataFrame 'df' by 'Year' and calculate the sum of 'Global_Sales' for each year
    yearly_sales = df.groupby('Year')['Global_Sales'].sum()
    # Create a line plot using Matplotlib, where x-values are years, y-values are global sales,
    # and 'o' is used as a marker for each data point
    plt.plot(yearly_sales.index, yearly_sales.values, marker='o')
    # Set the title, x-axis label, and y-axis label for the plot
    plt.title('Global Sales Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Global Sales (in millions)')
    # Display the line plot
    plt.show()