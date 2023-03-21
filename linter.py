from SublimeLinter.lint import (
    Linter,
    WARNING,
    util,
    STREAM_STDOUT,
)
import json


class Revive(Linter):
    cmd = ("revive", "-formatter", "ndjson", "${args}")
    regex = r".*"
    multiline = False
    default_type = WARNING
    tempfile_suffix = "go"
    defaults = {"selector": "source.go"}

    def split_match(self, match):
        result = super().split_match(match)
        js = json.loads(match.group(0))
        result["line"] = js.get("Position").get("Start").get("Line") - 1
        result["col"] = js.get("Position").get("Start").get("Offset")
        result["end_col"] = js.get("Position").get("End").get("Offset")
        result["end_line"] = js.get("Position").get("End").get("Line") - 1
        result["message"] = js.get("Failure")
        sev = js.get("Severity")
        result["error_type"] = "warning" if sev == "warning" else "error"
        return result
