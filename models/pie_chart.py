import pandas as pd
import matplotlib.pyplot as plt

def pie_chart():
    df = pd.read_csv('./assets/game_data.csv')

    # Drop rows with missing values
    df = df.dropna()

    # Convert 'Year_of_Release' to integer
    df['Year'] = df['Year'].astype(int)

    # Count the occurrences of each unique value in the 'Genre' column and store it in 'genre_distribution'
    genre_distribution = df['Genre'].value_counts()
    # Create a pie chart using Matplotlib, where:
    # - x-values are the counts of each genre,
    # - labels are the unique genres,
    # - autopct='%1.1f%%' displays the percentage on each wedge with one decimal place,
    # - startangle=90 rotates the starting position of the pie chart to 90 degrees (top of the chart).
    plt.pie(genre_distribution, labels=genre_distribution.index, autopct='%1.1f%%', startangle=90)
    # Set the title of the plot
    plt.title('Genre Distribution')
    # Display the pie chart
    plt.show()