# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
from flask import , request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
  if data["name"].lower() == "david":
    return "Hello baldie"


app.run(host='0.0.0.0', port=81)

```
<details> <summary> 👀 Answer </summary>

```python
from flask import Flask, request # Didn't import Flask

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
  get = request.args # Didn't request the args and assign to a variable
  if get["name"].lower() == "david": # Wrong variable name used
    return "Hello baldie"

  return "No data" # No return for if the page is empty

app.run(host='0.0.0.0', port=81)
```

</details>