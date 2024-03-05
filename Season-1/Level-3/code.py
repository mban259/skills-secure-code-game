# Welcome to Secure Code Game Season-1/Level-3!

# You know how to play by now, good luck!

import os
from flask import Flask, request

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)
@app.route("/")
def source():
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore

class TaxPayer:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    # returns the path of an optional profile picture that users can set
    def get_prof_picture(self, path=None):
        # setting a profile picture is optional
        if not path:
            pass

        # defends against path traversal attacks
        if not safe_path(path):
            return None

        # builds path
        base_dir = os.path.dirname(os.path.abspath(__file__))
        prof_picture_path = os.path.normpath(os.path.join(base_dir, path))

        with open(prof_picture_path, 'rb') as pic:
            picture = bytearray(pic.read())

        # assume that image is returned on screen after this
        return prof_picture_path

    # returns the path of an attached tax form that every user should submit
    def get_tax_form_attachment(self, path=None):
        tax_data = None

        if not path:
            raise Exception("Error: Tax form is required for all users")
        if not safe_path(path):
            return None
        with open(path, 'rb') as form:
            tax_data = bytearray(form.read())

        # assume that tax data is returned on screen after this
        return path

def safe_path(path: str) -> bool:
    """相対パスpathが安全か判定する"""
    # 現在のパス
    base_dir: str = os.path.dirname(os.path.abspath(__file__))
    # 引数の絶対パスの正規化
    file_path: str = os.path.normpath(os.path.join(base_dir, path))
    # カレントディレクトリと引数のパスが一致する (引数のパスはbase_dir以下)ならok
    common: str = os.path.commonpath([base_dir, file_path])
    return common == base_dir
