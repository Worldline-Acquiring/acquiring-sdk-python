import codecs
import re

from typing import AnyStr, Dict, Mapping, Optional, Pattern, Sequence, Union

from .obfuscation_rule import ObfuscationRule, obfuscate_all, obfuscate_all_but_first, obfuscate_all_but_last


class BodyObfuscator(object):
    """
    A class that can be used to obfuscate properties in JSON bodies.
    """

    __obfuscation_rules: Dict[str, ObfuscationRule] = None
    __property_pattern: Pattern[AnyStr] = None

    def __init__(self, additional_rules: Optional[Mapping[str, ObfuscationRule]] = None):
        """
        Creates a new  body obfuscator.
        This will contain some pre-defined obfuscation rules, as well as any provided custom rules

        :param additional_rules: An optional mapping from property names to obfuscation rules,
         where an obfuscation rule is a function that obfuscates a single string,
        """
        self.__obfuscation_rules = {
            "address": obfuscate_all(),
            "authenticationValue": obfuscate_all_but_first(4),
            "bin": obfuscate_all_but_first(6),
            "cardholderAddress": obfuscate_all(),
            "cardholderPostalCode": obfuscate_all(),
            "cardNumber": obfuscate_all_but_last(4),
            "cardSecurityCode": obfuscate_all(),
            "city": obfuscate_all(),
            "cryptogram": obfuscate_all_but_first(4),
            "expiryDate": obfuscate_all_but_last(4),
            "name": obfuscate_all(),
            "paymentAccountReference": obfuscate_all_but_first(6),
            "postalCode": obfuscate_all(),
            "stateCode": obfuscate_all(),

        }
        if additional_rules:
            for name, rule in additional_rules.items():
                self.__obfuscation_rules[name] = rule

        property_names = tuple(self.__obfuscation_rules.keys())
        self.__property_pattern = self.__build_property_pattern(property_names)

    @staticmethod
    def __build_property_pattern(property_names: Sequence[str]) -> Pattern[AnyStr]:
        if not property_names:
            return re.compile("$^")
        s = "([\"'])("
        for p in property_names:
            s += '|' + re.escape(p)
        s += ")\\1\\s*:\\s*(?:([\"'])(.*?)(?<!\\\\)\\3|([^\"'\\s\\[\\{]((?!,)\\S)*))"
        return re.compile(s, re.DOTALL)

    def __obfuscate_value(self, property_name: str, value: str) -> str:
        obfuscation_rule = self.__obfuscation_rules.get(property_name)
        if obfuscation_rule:
            return obfuscation_rule(value)
        return value

    def obfuscate_body(self, body: Union[str, bytes, None], charset: Optional[str] = None) -> Optional[str]:
        """
        Obfuscates the body from the given stream as necessary.
        :param body: The body to obfuscate, as string or bytes.
        :param charset: The charset to use to read the body bytes.
        """
        if charset:
            body = codecs.decode(body, charset)

        if body is None:
            return None
        if not body:
            return ""
        index = 0
        s_obfuscate = ""
        matcher = self.__property_pattern.finditer(body)
        for x in matcher:
            property_name = x.group(2)
            value = x.group(4)
            value_start = x.start(4)
            value_end = x.end(4)
            if not value:
                value = x.group(5)
                value_start = x.start(5)
                value_end = x.end(5)
            obfuscated_value = self.__obfuscate_value(property_name, value)
            s_obfuscate += body[index:value_start] + obfuscated_value
            index = value_end
        return s_obfuscate + body[index:]

    @staticmethod
    def default_body_obfuscator() -> 'BodyObfuscator':
        return _DEFAULT_BODY_OBFUSCATOR


_DEFAULT_BODY_OBFUSCATOR = BodyObfuscator()
