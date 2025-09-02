import requests
import pandas as pd

url = "https://restcountries.com/v3.1/all?fields=name,population"

try :
    
    print("Fetching data...")
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print("Data fetched successfully!")
    
    df = pd.DataFrame(data)
    df_simple = df[['name','population']].copy()
    df_simple['name'] = df_simple['name'].apply(lambda x : x['common'])
    df_sorted = df_simple.sort_values(by='population',ascending=False)
    
    print("\n--- Top 10 Most Populated Countries ---")
    print(df_sorted.head(10))

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from the API : {e}")
except Exception as e:
    print(f"An error occurred during data processing: {e}")