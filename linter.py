from SublimeLinter.lint import (
    Linter,
    WARNING,
    util,
)


class Revive(Linter):
    # cmd = "revive -formatter ndjson ${args}"
    cmd = ("revive", "-formatter", "ndjson", "${args}", "${file}")
    # regex = r"^.+:(?P<line>\d+):(?P<col>\d+):\s+(?P<message>.+)"
    regex = (
        r".+\"Severity\":\"((?P<error>error)|(?P<warning>warning))\".+?\"Failure\":\"(?P<message>.*?)\".+?"
        '"Offset":(?P<col>\d+).+?"Line":(?P<line>\d+)'
    )
    # regex = r".+\"Severity\":\"((?P<error>error)|(?P<warning>warning))\".+?\"Failure\":\"(?P<message>.*?)\".+?\"Offset\":(?P<col>\d+).+?\"Line\":(?P<line>\d+)"
    multiline = False
    default_type = WARNING
    tempfile_suffix = "go"
    error_stream = util.STREAM_STDOUT
    defaults = {"selector": "source.go"}
