"""
pandasHW.py
====================================
This is an example file with correct docstring examples

| Author: Tobias Allerstorfer
| Date: 2026 April 17
"""
import requests
import re
import pandas as pd
import matplotlib.pyplot as plt
def main():
    
    url = "https://forecast.weather.gov/obslocal.php?warnzone=IAZ031&local_place=Sioux%20City%20IA&zoneid=CDT&offset=18000"
  

   
    response = requests.get(url)
    response.raise_for_status()
    html = response.text

    print(f"Downloaded {len(html)} characters")

    
    # 2. Extract table rows
   
    rows = re.findall(r'<tr class="(?:odd|even)">(.*?)</tr>', html, re.DOTALL)

    print(f"Found {len(rows)} data rows")

    
    # 3. Parse data from rows
  
    data = []

    for row in rows:
        cols = re.findall(r'<td.*?>(.*?)</td>', row, re.DOTALL)
        cols = [c.strip() for c in cols]

        if len(cols) >= 8:
            try:
                temp = int(cols[3])
                humidity = int(cols[5])
                pressure = float(cols[7])

                data.append([temp, humidity, pressure])
            except:
                # skip bad rows
                continue

    
    # 4. Create DataFrame
  
    df = pd.DataFrame(data, columns=['Temperature', 'Humidity', 'Pressure'])

    print("\nDataFrame Preview:")
    print(df.head())

   
    # 5. Analysis
    
    print("\n====== Weather Analysis ======")
    print(f"Records analyzed: {len(df)}")

    print("\nTemperature:")
    print(f"  Average: {df['Temperature'].mean():.2f}")
    print(f"  Min: {df['Temperature'].min()}")
    print(f"  Max: {df['Temperature'].max()}")
    print(f"  Median: {df['Temperature'].median()}")
    print(f"  Std Dev: {df['Temperature'].std():.2f}")

    print("\nHumidity:")
    print(f"  Average: {df['Humidity'].mean():.2f}")
    print(f"  Min: {df['Humidity'].min()}")
    print(f"  Max: {df['Humidity'].max()}")

    print("\nPressure:")
    print(f"  Average: {df['Pressure'].mean():.2f}")
    print(f"  Min: {df['Pressure'].min()}")
    print(f"  Max: {df['Pressure'].max()}")

    print("\nMost common temperatures:")
    print(df['Temperature'].value_counts())

    
    # 6. Plot (Extra Credit)
   
    plt.figure()
    df['Temperature'].plot(kind='bar', title='Temperature Observations')
    plt.xlabel("Observation Index")
    plt.ylabel("Temperature (F)")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()