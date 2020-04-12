import ask_sdk_core.utils as ask_utils
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractRequestInterceptor, AbstractExceptionHandler)
from ask_sdk_core.handler_input import HandlerInput
import i18n

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = i18n.t("strings.WELCOME_MESSAGE")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )