import json
import boto3


def lambda_handler(event, context):
	# Instanciating connection objects with DynamoDB using boto3 dependency
	dynamodb = boto3.resource('dynamodb')

	# Getting the table Resources object
	tableResources = dynamodb.Table('resources')

	resourceID = event['resourceID']
	title = event['title']
	task = event['task']


	# Putting a try/catch to log to user when some error occurs
	try:

		tableResources.put_item(
		   Item={
				'resourceID': int(resourceID),
				'title': title,
				'task': task
			}
		)

		return {
			'statusCode': 200,
			'body': json.dumps('Succesfully inserted task!')
		}
	except:
		print('Closing lambda function')
		return {
				'statusCode': 400,
				'body': json.dumps('Error saving the task')
		}