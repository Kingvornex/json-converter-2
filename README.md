# json-converter-2

[structure.md](structure.md)

---

## Rule for project

Every file inside converters/ should expose exactly one function:

def convert(data):
    ...
    return result

and should not open input files or write output files. That responsibility belongs exclusively to runner.py. This keeps every converter consistent and lets the pipeline automatically process any module listed in pipeline.json.

---

# JSON Converter Pipeline

A modular Python-based JSON conversion pipeline designed to transform game data into custom output formats.

Each converter is implemented as an independent module, while a single runner executes the entire pipeline based on a configuration file. This makes it easy to add new converters without modifying the main application.

## Features

* Modular converter architecture
* Configurable conversion pipeline
* Supports multiple conversion jobs in one run
* Automatically creates output directories
* UTF-8 support
* GitHub Actions compatible
* Easy to extend with additional converters

---

# Project Structure

```text
.
├── config/
│   └── pipeline.json
├── converters/
│   ├── dbm_table.py
│   ├── DamageAttrIdName.py
│   └── ...
├── input/
│   ├── DbmTable.json
│   ├── DamageAttrIdName.json
│   └── ...
├── output/
├── runner.py
└── README.md
```

---

# Requirements

* Python 3.10 or newer

No external dependencies are required.

---

# Usage

Run the entire pipeline:

```bash
python runner.py
```

Each configured job will:

1. Load its input JSON.
2. Execute the specified converter.
3. Write the converted data to the configured output file.

Example output:

```text
Finished dbm_table
Finished DamageAttrIdName
```

---

# Configuration

The conversion pipeline is defined in:

```text
config/pipeline.json
```

Example:

```json
{
  "jobs": [
    {
      "module": "dbm_table",
      "input": "input/DbmTable.json",
      "output": "output/DbmTable.json"
    },
    {
      "module": "DamageAttrIdName",
      "input": "input/DamageAttrIdName.json",
      "output": "output/DamageAttrIdName.json"
    }
  ]
}
```

Each job contains:

| Field    | Description                           |
| -------- | ------------------------------------- |
| `module` | Converter module inside `converters/` |
| `input`  | Input JSON file                       |
| `output` | Output JSON file                      |

Jobs are executed sequentially in the order they appear.

---

# Creating a Converter

Each converter must expose a single function named `convert`.

Example:

```python
def convert(data):
    output = {}

    for key, value in data.items():
        output[key] = value

    return output
```

The converter:

* receives the parsed JSON object
* performs any required transformation
* returns the converted object

Do **not** read or write files inside converter modules. File handling is managed entirely by `runner.py`.

---

# Example Converter

```python
def convert(data):
    return {
        str(key): value["Name"]
        for key, value in data.items()
    }
```

---

# Adding a New Converter

1. Create a new Python file inside `converters/`.

Example:

```text
converters/MyConverter.py
```

2. Implement:

```python
def convert(data):
    ...
    return result
```

3. Add a new job to `config/pipeline.json`.

```json
{
  "module": "MyConverter",
  "input": "input/MyData.json",
  "output": "output/MyData.json"
}
```

4. Run:

```bash
python runner.py
```

The new converter will automatically be executed.

---

# Output

Converted files are written to the configured output paths.

Output directories are automatically created if they do not already exist.

---

# Design Philosophy

The project separates responsibilities:

* **runner.py** handles loading files, executing converters, and writing output.
* **Converter modules** only transform data.
* **pipeline.json** controls which conversions are executed.

This separation keeps converters simple, reusable, and easy to maintain.

---

# License

This project is released under the MIT License.
