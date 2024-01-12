import pandas as pd

def data_frame_info():
    # Load the dataset
    df = pd.read_csv('assets/game_data.csv')

    # Display basic information about the dataset
    print(df.info())
    # Display 1 line space in between
    print('\n')
    # Display the first few rows of the dataset
    print(df.head())
    # Display 1 line space in between
    print('\n')
    # Display the first few rows of the dataset
    print(df.tail())

    # Drop rows with missing values
    df = df.dropna()

    # Convert 'Year_of_Release' to integer
    df['Year'] = df['Year'].astype(int)

    #show the whole dataframe
    df  