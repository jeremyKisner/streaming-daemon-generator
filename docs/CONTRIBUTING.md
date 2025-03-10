# Getting Started

1. Create Virtual Environment
``` bash
python -m venv .venv
```

2. Activate Virtual Environment (Windows)
``` bash
.\.venv\Scripts\Activate.ps1 
```

3. Install Dependencies
``` bash
pip install -r requirements.txt
```

4. Export Python Path 
Example Windows:
``` bash
$env:PYTHONPATH = $pwd
```

# Running Locally

## Running Script
1. Run
At minimum, you need to set the description, which is used by the LLM to produces an audio file.
``` bash
python .\sdg\main.py -d "<description of audio to generate>"
```

However, you may supply the following additional, optional parameters.

- **-n --name** - name of audio
- **-a --artist** - artist of audio
- **-l --album** - album of audio
- **-t --time** - length of time of audio. Warning, longer=more computing power needed
- **-d --description** - a prompt describing the specific audio requirements

For example, run:
``` bash
python .\sdg\main.py -n "<name>" -a "<artist>" -l "<album>" -t 10 -d "<description of audio to generate>"
```

## Running Server
1. Run
``` bash
uvicorn server:app --port 8081 --reload
```
2. Check health z-page
``` bash
curl http://127.0.0.1:8000
```

## Running Docker
1. Build
``` bash
docker compose up --build -d
```
2. Check health z-page
``` bash
curl http://127.0.0.1:8081
```
3. Tear down
``` bash
docker compose down
```
