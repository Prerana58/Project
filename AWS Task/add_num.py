import json

def lambda_handler(event, context):
    # Extract numbers from the event object
    num1 = event.get('num1')
    num2 = event.get('num2')
    
    # Check if both numbers are provided
    if num1 is None or num2 is None:
        return {
            'statusCode': 400,
            'body': json.dumps('Please provide both num1 and num2')
        }
    
    # Calculate the sum of the two numbers
    result = num1 + num2
    
    # Return the result
    return {
        'statusCode': 200,
        'body': json.dumps({
            'result': result
        })
    }
