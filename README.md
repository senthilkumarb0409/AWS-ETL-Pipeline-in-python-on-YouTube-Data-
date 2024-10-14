# AWS-ETL-Pipeline-in-python-on-YouTube-Data

Welcome to the **AWS-ETL-Pipeline-in-python-on-YouTube-Data** project! This pipeline extracts YouTube video data from a specified channel using the YouTube Data API, processes and transforms the data, and uploads it to an AWS S3 bucket. The project is divided into the following stages:

1. **Extracting** video data from a YouTube channel.
2. **Transforming** the data into CSV, JSON, and Excel formats.
3. **Uploading** the transformed data to an AWS S3 bucket.

->to watch the video walkthrough :[CLICK HERE!!](https://youtu.be/uoCJSXlmyIY)

---


Step 1 : Extraction of youtube data :

    1.  -> create a project in google cloud console for API integration to extract  youtube data
    
      ->click the API & services 
      
                      -> click credentials and click create credentials

                      -> API key will be generated (copy the key)
                      
                      ->Inorder to extract the youtube data through this api key
                      
                                    -> goto API library : search youtube data api v3 
                                    
                                    ->click ENABLE
    
     2. ->write the python code for extracting the needed data using youtube api and save it in the json format (extract.py)
     
                      -> In the api key section of code : paste the copied api key.
                      
                      -> In the channel id section of code: paste the channel id from which ur going to collect the data
                      
                      -> Run the extract.py code . 

Step 2 : Transforming the youtube data :

     ->write the python code for transforming the collected data from extraxtion process according to ur use cases / requirements, clean the data,in different format you need(transform.py)
     
                      ->Run the transform.py code.

Step 3 : Loading of youtube data  :

      -> write the python code for storing the data in the aws s3 or rds or dynamo db for later use for aanalying the data using analytics tools for business or other purposes.(load.py)
      
           ->in order for the code to run and correctly load the data into the aws 
           
                   ->configure the file that helps the boto3 package to establish connection between ur code and aws s3
                   
                            ->the file should be in the format: .aws/credentials
                            
                                      -> in side the credentials file:
                                      
                                               ->Format:
                                                              [default]
                                                              aws_access_key_id = "your aws access key from iam security credentials section"
                                                              aws_secret_access_key = "your aws secret key from iam security credentials section"
                                                              region = eu-north-1
                                                              
                                                ->the file should be located in :users/ur usr name/.aws/credentials
                                                
             -> create a empty bucket in the s3 and copy the name.
             
                      ->paste the name of the bucket in the code section where the bucket name is needed
                      
             ->Run the Load.py code.

the xlsx file will be successfully uploaded in the bucket in the name u mentioned in  the code.


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



