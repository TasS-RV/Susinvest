import sys
import os

# Ensures that the esg_platform file is added to PYTHONPATH as a module for importing
sys.path.append(os.path.dirname(os.path.abspath(__file__)).rsplit('\\', 1)[0])

from esg_platform.sentiment_analysis.gdelt_query import gdelt_query

if __name__ == "__main__":
    urls = gdelt_query("apple")
    print(urls[:10])