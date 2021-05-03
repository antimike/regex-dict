import re


class RegexDict(dict):
    """RegexDict.
    Extension of Python dict which supports regex filtering.

    Methods:
    ========

    match: Returns a RegexDict whose keys match the passed regex
    match_or: Returns a RegexDict whose keys match any of the passed regexes
    match_and: Returns a RegexDict whose keys match all of the passed regexes
    """

    def __init__(self, *args, **kwargs):
        """__init__.
        RegexDict constructor.  Inherits from normal `dict` constructor.

        :param args: Any args which could be passed to `dict` constructor
        :param kwargs: Any kwargs which could be passed to `dict` constructor
        """
        super().__init__(*args, **kwargs)

    def match(self, regex):
        """match.
        Returns an instance of RegexDict whose keys match a single passed regex.

        :param regex: Regular expression to match
        """
        return RegexDict(
            filter(
                lambda item: re.compile(regex).match(item[0]) is not None,
                super().items(),
            )
        )

    def match_or(self, *regexes):
        """match_or.
        Returns an instance of RegexDict whose keys match any of a list of passed regexes.

        :param regexes: Regexes to match "inclusively" (i.e., at least one must match)
        """
        return RegexDict(
            filter(
                lambda item: any(
                    re.compile(regex).match(item[0]) is not None for regex in regexes
                ),
                super().items(),
            )
        )

    def match_and(self, *regexes):
        """match_and.
        Returns an instance of RegexDict whose keys match all of a list of passed regexes.

        :param regexes: Regexes to match "exclusively" (i.e., all must match)
        """
        return RegexDict(
            filter(
                lambda item: all(
                    re.compile(regex).match(item[0]) is not None for regex in regexes
                ),
                super().items(),
            )
        )
