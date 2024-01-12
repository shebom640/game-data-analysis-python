#3D scatter plot using Plotly Express [opens in webpage]
import plotly.express as px
import pandas as pd

def three_dimensional_plot():
    df = pd.read_csv('./assets/game_data.csv')

    # Drop rows with missing values
    df = df.dropna()

    # Convert 'Year_of_Release' to integer
    df['Year'] = df['Year'].astype(int)
    fig = px.scatter_3d(df, x='NA_Sales', y='EU_Sales', z='Global_Sales', color='Genre',
                        size='Global_Sales', hover_name='Name',
                        title='Global_Sales vs. NA_Sales vs. EU_Sales')
    fig.show()