import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def box_plot():
    df = pd.read_csv('./assets/game_data.csv')

    # Drop rows with missing values
    df = df.dropna()

    # Convert 'Year_of_Release' to integer
    df['Year'] = df['Year'].astype(int)

    # Set up the figure size for the box plot
    plt.figure(figsize=(12, 8))

    # Create a box plot using Seaborn, where x-values are 'Platform', y-values are 'Global_Sales',
    # data is taken from the DataFrame 'df', and 'pastel' is used for the color palette
    sns.boxplot(x='Platform', y='Global_Sales', data=df, palette='pastel', hue='Platform', legend=False)

    # Set the title, x-axis label, and y-axis label for the plot
    plt.title('Sales Distribution by Platform')
    plt.xlabel('Platform')
    plt.ylabel('Global Sales (in millions)')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Display the box plot
    plt.show()