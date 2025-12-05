import json

def lambda_handler(event, context):
    """
    Sadhu's Lambda Function
    This function will be automatically deployed from GitHub
    """
    
    # Parse input
    if 'body' in event and event['body']:
        try:
            body = json.loads(event['body'])
        except:
            body = {}
    else:
        body = {}
    
    # Get name from input or use default
    name = body.get('name', 'World')
    
    # Create response
    response_message = f"Hello {name}! This is Sanjay's Lambda function."
    
    # Return response
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'X-Created-By': 'Sadhana'
        },
        'body': json.dumps({
            'message': response_message,
            'input': event,
            'timestamp': context.aws_request_id,
            'function': 'sadhu-lambda-func'
        })
    }