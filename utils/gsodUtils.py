import requests
import os

def download_gsod_data(station_code: str, year: int, save_path: str) -> None:
    """
    Downloads GSOD data for a given station and year, and saves it to the specified path.

    https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/2024/69015093121.csv

    :param station_code: The GSOD station code (e.g., '69015093121').
    :param year: The year for which to download the data (e.g., 2024).
    :param save_path: The file path where the downloaded data will be saved.
    """
    base_url = "https://www.ncei.noaa.gov/data/global-summary-of-the-day/access"
    url = f"{base_url}/{year}/{station_code}.csv"

    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Data for station {station_code} in year {year} downloaded successfully.")
    else:
        print(f"Failed to download data: {response.status_code} - {response.reason}")