# AWS-ETL-Pipeline-in-python-on-YouTube-Data

# AWS ETL Pipeline for YouTube Data Analysis

Welcome to the **AWS ETL Pipeline for YouTube Data Analysis** project! This pipeline extracts YouTube video data from a specified channel using the YouTube Data API, processes and transforms the data, and uploads it to an AWS S3 bucket. The project is divided into the following stages:

1. **Extracting** video data from a YouTube channel.
2. **Transforming** the data into CSV, JSON, and Excel formats.
3. **Uploading** the transformed data to an AWS S3 bucket.

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed and configured:

- **Python 3.x** (Recommended version: 3.8+)
- **AWS CLI** for AWS credentials configuration (required for uploading data to S3)
- **Google API Python Client** for accessing the YouTube Data API

---

## 📦 Setup Instructions

### Step 1: Install Python and Dependencies

1. **Install Python 3.x** if you haven't already from the [official Python website](https://www.python.org/downloads/).
   
2. **Install required Python libraries**:
   
   Use the following command to install all necessary dependencies:

   ```bash
   pip install google-api-python-client
   pip install pandas
   pip install openpyxl
   pip install boto3
   pip install isodate
