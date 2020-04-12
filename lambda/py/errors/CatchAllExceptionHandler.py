import ask_sdk_core.utils as ask_utils
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractRequestInterceptor, AbstractExceptionHandler)
from ask_sdk_core.handler_input import HandlerInput
import i18n
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """

    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)
        speak_output = i18n.t("strings.ERROR")

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )