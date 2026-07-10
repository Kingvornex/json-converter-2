import json
import importlib
from pathlib import Path

config = json.load(open("config/pipeline.json", encoding="utf8"))

for job in config["jobs"]:

    module = importlib.import_module(f"converters.{job['module']}")

    with open(job["input"], encoding="utf8") as f:
        data = json.load(f)

    result = module.convert(data)

    Path(job["output"]).parent.mkdir(parents=True, exist_ok=True)

    with open(job["output"], "w", encoding="utf8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Finished {job['module']}")
