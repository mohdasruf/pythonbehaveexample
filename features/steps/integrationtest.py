from behave import *
import boto3
from configparser import ConfigParser

from printprog import printfile

use_step_matcher("re")


@step("trigger the python script")
def step_impl(context):
    context.successread = printfile(context.save_as)
    print('Successfully trigger the python script')


@then("the python output is as expected")
def step_impl(context):
    assert (context.successread == ['Test File'])

@given("I download the file and place it in the test files folder")
def step_impl(context):
    config_object = ConfigParser()
    config_object.read("config.ini")
    context.s3 = boto3.client('s3')
    filedetails = config_object["FILEDETAILS"]
    context.bucket_name = filedetails["bucketname"]
    context.s3_file_path = filedetails["s3_file_path"]
    context.save_as = filedetails["save_as"]
    context.s3.download_file(context.bucket_name, context.s3_file_path, context.save_as)
    print('Successfully placed it in the folder')
