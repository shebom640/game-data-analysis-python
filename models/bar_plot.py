import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def bar_plot():
    df = pd.read_csv('./assets/game_data.csv')

    # Drop rows with missing values
    df = df.dropna()

    # Convert 'Year_of_Release' to integer
    df['Year'] = df['Year'].astype(int)

    # Group the DataFrame 'df' by 'Publisher' and sum the 'Global_Sales' for each publisher
    top_publishers = df.groupby('Publisher')['Global_Sales'].sum().nlargest(10)
    # Set up the figure size for the plot
    plt.figure(figsize=(10, 6))
    # Create a bar plot using Seaborn, where x-values are the global sales values, y-values are the publisher names,
    # and use the 'viridis' color palette for the bars
    sns.barplot(x=top_publishers.values, y=top_publishers.index, palette='viridis', hue=top_publishers.index, legend=False)
    # Set the title of the plot
    plt.title('Top 10 Publishers by Global Sales')
    # Set labels for the x and y axes
    plt.xlabel('Global Sales (in millions)')
    plt.ylabel('Publisher')
    # Display the plot
    plt.show()