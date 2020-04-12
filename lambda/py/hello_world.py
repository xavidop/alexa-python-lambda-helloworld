# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_model import Response
from intents import LaunchRequestHandler as launch
from intents import HelloWorldIntentHandler as hello
from intents import HelpIntentHandler as help
from intents import CancelOrStopIntentHandler as cancel
from intents import SessionEndedRequestHandler as session
from intents import IntentReflectorHandler as reflector
from errors import CatchAllExceptionHandler as errors
from interceptors import LocalizationInterceptor as locale

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.
sb = SkillBuilder()

sb.add_request_handler(launch.LaunchRequestHandler())
sb.add_request_handler(hello.HelloWorldIntentHandler())
sb.add_request_handler(help.HelpIntentHandler())
sb.add_request_handler(cancel.CancelOrStopIntentHandler())
sb.add_request_handler(session.SessionEndedRequestHandler())
# make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers
sb.add_request_handler(reflector.IntentReflectorHandler())

sb.add_global_request_interceptor(locale.LocalizationInterceptor())

sb.add_exception_handler(errors.CatchAllExceptionHandler())

handler = sb.lambda_handler()
