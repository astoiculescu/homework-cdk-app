import json
import pytest

from aws_cdk import core
from homework-cdk-app.homework_cdk_app_stack import HomeworkCdkAppStack


def get_template():
    app = core.App()
    HomeworkCdkAppStack(app, "homework-cdk-app")
    return json.dumps(app.synth().get_stack("homework-cdk-app").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
