# AWS-ETL-Pipeline-in-python-on-YouTube-Data

Welcome to the **AWS-ETL-Pipeline-in-python-on-YouTube-Data** project! This pipeline extracts YouTube video data from a specified channel using the YouTube Data API, processes and transforms the data, and uploads it to an AWS S3 bucket. The project is divided into the following stages:

1. **Extracting** video data from a YouTube channel.
2. **Transforming** the data into CSV, JSON, and Excel formats.
3. **Uploading** the transformed data to an AWS S3 bucket.

->to watch the video walkthrough :[CLICK HERE!!](https://youtu.be/uoCJSXlmyIY)

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

### Step 2: Obtain YouTube API Key

To interact with the **YouTube Data API**, you'll need to generate an **API Key**. Follow these steps to obtain your key:

1. **Visit the Google Cloud Console**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/).

2. **Create a New Project** (or use an existing one):
   - In the top navigation bar, click on the **project dropdown** and select **"New Project"**.
   - Give your project a name and click **"Create"**.
   - If you already have a project, you can skip this step and use the existing project.

3. **Enable the YouTube Data API v3**:
   - In the **Google Cloud Console**, navigate to the **API & Services** section.
   - Click on **"Library"** in the sidebar.
   - In the **API Library**, search for **"YouTube Data API v3"**.
   - Click on **"YouTube Data API v3"** and then click **Enable**.

4. **Generate an API Key**:
   - After enabling the API, navigate to the **Credentials** section.
   - Click **Create Credentials** and select **API Key** from the dropdown.
   - Your **API key** will be generated. **Copy** this key and keep it safe.
   
   > **Note:** Ensure that you **do not expose** your API key publicly. It is best practice to store the key in environment variables or configuration files that are not shared.

5. **Restrict Your API Key (Optional but Recommended)**:
   - To improve security, you can restrict your API key to specific HTTP referrers (websites) or IP addresses.
   - In the **Credentials** section, click on your newly created API Key and configure the restrictions as needed.

---

Now that you have your **YouTube API Key**, you can proceed with configuring it in the project as mentioned in the next steps.

# Step 3: Set Up AWS Credentials

To upload data to AWS S3, you need to configure your AWS credentials. 

---

Finally run all your .py files to see the output



