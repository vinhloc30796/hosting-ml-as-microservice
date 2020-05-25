# Import packages
import json
from pred import get_sentiment

# Define lambda_handler
def lambda_handler(event, context):
    """Input:
    - event (dict): {'body': str}
    Output:
    - sentiment (str):
    'pos' for positive
    and 'neg' for negative
    """
    # Log status
    print('Received event: ' + json.dumps(event, indent=2))
    # Run get_sentiment if 'body' found
    if 'body' in event:
        try:
            sentiment = get_sentiment(event['body'])
            print(f"Sentiment detected: {sentiment}")
        except:
            raise TypeError(
                "event['body'] is not compatible with get_sentiment()")
    else:
        raise ValueError("Can't find event['body']")

    return sentiment


# For testing
if __name__ == "__main__":
    test_event = {'body': 'Good and comprehensive guide to Hadoop architecture. Some of the first chapters are diving really deep into architecting own cluster. I would welcome similar deep dive into automating and provisioning of Hadoop clusters, because there is only brief introduction to this topics.'}
    lambda_handler(test_event, {})
