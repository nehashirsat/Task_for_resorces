## Assignment || DevOps Engineer

As per my assignment I have created 3 services in AWS namely API Gateway, Lambda Function and DynamoDB Table

- API Gateway — This service is responsible for deploying and serving HTTP RESTful endpoints. Thus you can trigger actions, when HTTP calls arrives to the generated endpoints.
- Lambda — This let you run code without provisioning or managing servers.
- DynamoDB — The NoSQL amazon database, where you can insert the information of your application on tables (Collections).

I have written code in Python language

### Why Python ?
- Because Python is very user friendly, and it’s really fast to test and to create a function

## Creating the DynamoDB Table
This table will have save the task of resorces in some organization according to their Title, so I have created three fields(Columns) to this table:
- ResourceID
- Title
- Task

Where I have used Partition Key as ResourceID and Sort Key as Title

## Creating Lambda Function
I have Created Two Lambda functions
- Create-Todo - A lambda that accepts JSON data for todo ({ title: string, task: string }) via direct invocation and store it in DynamoDB with a unique ID
- Read-Todo - Another lambda which accepts all or id for the todos - direct invocation

I have used Runtime as Python 3.7 and used boto3 dependency for doing the database persistance, also
I have created IAM role and Policy which has dynamoDB read, Write Access

## API Gateway Endpoint
I have create API gateway and two methods in API gateway POST and GET and used root resource only

## Cloudformation
- I have Used Cloudformation template in yaml to create and deploy my application and resorces in AWS cloud


# Self Evaluation

## What I could be done better if given more time?
- May be I will use better infrastructure like VPN subnet and apply more security to my application
- In IAM role I will give more granular access
- Will follow best practices while writting cloudformation template
- instead of storing my code in machine I'll prefer S3 for that
- In API Gateway I will add more security like API key

## Rate yourself on the technologies used in the assignment out of 10!
- Lambda Function - 4/10 
- DynamoDB - 4/10
- API Gateway - 4/10
- Cloudformation - 5/10
- IAM - 4/10



