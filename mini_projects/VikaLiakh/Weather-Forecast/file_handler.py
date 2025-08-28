import os
import pandas as pd

FILE_NAME = "forecast_results.txt"

def save_to_file(rows):
    """Append rows to the log file."""
    header = ["City", "Date", "Hour", "MaxTemp", "MinTemp", "Humidity", "WindSpeed", "WindDir"]
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a") as f:
        if not file_exists:
            f.write("\t".join(header) + "\n")
        for row in rows:
            f.write("\t".join(map(str, row)) + "\n")


def load_history():
    """Load history from file as a DataFrame."""
    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME, sep="\t")
        return df
    else:
        return None

