from flask import Flask, render_template, request, jsonify
import boto3
import json

app = Flask(__name__)

# Create a Bedrock client using Boto3
def create_bedrock_client():
    """Create and return a Bedrock Runtime client."""
    return boto3.client(
        service_name='bedrock-runtime',
        region_name='us-west-2'  # Change this to your AWS region
    )

# Create chat request body
def create_chat_request(prompt):
    """Create the request body for the Bedrock API."""
    return {
        "modelId": "anthropic.claude-3-haiku-20240307-v1:0",  # Changed from DeepSeek to Claude 3 Haiku
        "contentType": "application/json",
        "accept": "application/json",
        "body": json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 512,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        })
    }

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle chat requests
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if user_input:
        try:
            client = create_bedrock_client()
            request_data = create_chat_request(user_input)
            response = client.invoke_model(**request_data)
            response_body = json.loads(response['body'].read())
            assistant_message = response_body['content'][0]['text']
            
            # Extract code block if present
            if '```' in assistant_message:
                # Find the code block
                start_idx = assistant_message.find('```')
                end_idx = assistant_message.rfind('```')
                if start_idx != end_idx:
                    # Extract everything between the first and last ``` markers
                    code_block = assistant_message[start_idx:end_idx + 3]
                    assistant_message = code_block
            
            # Format the response
            formatted_response = {
                'response': assistant_message,
                'isCode': '```' in assistant_message
            }
            return jsonify(formatted_response)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return jsonify({'error': 'No message provided'}), 400

if __name__ == "__main__":
    app.run(debug=True)
