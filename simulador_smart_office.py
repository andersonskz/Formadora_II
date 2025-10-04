
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_sensor_data(start_date, num_days):
    data = []
    current_datetime = start_date

    for _ in range(num_days * 24 * 4):  
        hour = current_datetime.hour
        temp_base = 22 + 2 * np.sin(2 * np.pi * (hour - 8) / 24) 
        temperature = round(temp_base + np.random.normal(0, 0.5), 2)

        if 6 <= hour < 19:  
            luminosity = int(np.random.normal(500, 100)) 
        else:  
            luminosity = int(np.random.normal(10, 5)) 
        luminosity = max(0, luminosity) 

        
        if 8 <= hour < 18 and current_datetime.weekday() < 5:  
            occupancy = 1 if np.random.rand() < 0.8 else 0 
        else:
            occupancy = 1 if np.random.rand() < 0.1 else 0 

        data.append({
            'timestamp': current_datetime,
            'sensor_id': 'temp_001',
            'value': temperature,
            'type': 'temperature'
        })
        data.append({
            'timestamp': current_datetime,
            'sensor_id': 'lux_001',
            'value': luminosity,
            'type': 'luminosity'
        })
        data.append({
            'timestamp': current_datetime,
            'sensor_id': 'occ_001',
            'value': occupancy,
            'type': 'occupancy'
        })

        current_datetime += timedelta(minutes=15)

    return pd.DataFrame(data)

if __name__ == "__main__":
    start_date = datetime(2025, 10, 1, 0, 0, 0) 
    num_days = 7
    df = generate_sensor_data(start_date, num_days)
    df.to_csv('smart_office_data.csv', index=False)
    print("Dados simulados gerados e salvos em smart_office_data.csv")

