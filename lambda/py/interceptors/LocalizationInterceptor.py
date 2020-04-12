from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractRequestInterceptor, AbstractExceptionHandler)
from ask_sdk_core.handler_input import HandlerInput
import i18n
import os
import os.path

class LocalizationInterceptor(AbstractRequestInterceptor):
    """
    Add function to request attributes, that can load locale specific data
    """
    def process(self, handler_input):
        i18n.load_path.append(os.path.join(os.path.dirname(__file__), "../locales"))
        i18n.set('locale', handler_input.request_envelope.request.locale.split(sep='-')[0])