# Amazon Bedrock Integration App

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- AWS Account with Bedrock access
- AWS CLI installed and configured

## AWS Setup
1. Configure AWS credentials:
   ```bash
   aws configure
   ```
   Enter your AWS Access Key ID, Secret Access Key, and preferred region.

2. Ensure you have access to Amazon Bedrock in your AWS account and the necessary IAM permissions.

## Installation Steps

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd amazon-bedrock-integration-app
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   .\venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with the following variables:
   ```
   AWS_REGION=your-aws-region
   FLASK_APP=app.py
   FLASK_ENV=development
   # Add any other required environment variables
   ```

## Running the Application

1. Start the Flask development server:
   ```bash
   flask run
   ```
   or
   ```bash
   python app.py
   ```

2. Access the application:
   Open your browser and navigate to `http://localhost:5000`

## Troubleshooting

- Ensure your AWS credentials are properly configured
- Check that you have the necessary AWS Bedrock permissions
- Verify all environment variables are correctly set
- Make sure all Python dependencies are installed correctly

## Additional Resources

- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python AWS SDK (Boto3) Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

