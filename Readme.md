# Commands to run locally
# Create virtual environment
python3 -m venv env

#Activate virtual environment
myenv/Scripts/activate

#Installing requirements in the virtual environment
pip install -r requirements.txt

#To run bdds
behave


# policies update in AWS
Created a inline policy for the codepipeline to access S3

#Resources used for creating AWS codepipeline
https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-create-pipeline.html#how-to-create-pipeline-console

#Purpose of the test
This is a sample integration test which downloads a file from S3 in AWS and executes the python script using the input


