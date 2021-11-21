import json
import boto3
def lambda_handler(event, context):
	# TODO implement
	dynamodb = boto3.resource('dynamodb')
	tableResources = dynamodb.Table('resources')
	response = tableResources.scan()
	return {
		'statusCode': 200,
		'body': response['Items']
	}