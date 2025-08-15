# Digital-Marketing-Project
About digital marketing data analysis

GA4APIDataPull.pynb file contains code to do foloowing -
    -Automatically fetch user behaviour analytics data of any live hosted web site (Business, Merchandise or others) to pyhton IDE using GA4 API. 
    
User has to do following steps to use this file:
    -create a account on google cloud
    -create account on google analytics
    -create a property id and update serive email in to its property(Can be found in the Google_cloud_serice_credential_json file) and provide at leastr viewer acces       to it.
    - add website url in data stream for which user wants user behaviour data. 
    - add GA4 tagging code snippet in every web page html of the website with the measurement id (provided in data stream). This will let GA4 API to collect user          -behaviour data  
    - initialize 'Property_Id' environment variable
    - intialize 'GA4_Service_Account_Credentials' environment variable with the Google cloud service credentials json file. 

Run the code
