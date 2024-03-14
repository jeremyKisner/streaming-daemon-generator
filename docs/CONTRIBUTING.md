# Getting Started

1. Create Virtual Environment
```
python -m venv .venv
```

2. Activate Virtual Environment (Windows)
```
.\.venv\Scripts\Activate.ps1 
```

3. Install Dependencies
```
pip install -r requirements.txt
```

4. Export Python Path 
Example Windows:
```
$env:PYTHONPATH = $pwd
```

# Running Locally
## Running as Script
1. Run script
At minimum, you need to set the description, which is used by the LLM to produces an audio file.
```
python sdg/main.py -d "<description of audio to generate>"
```

However, you may supply the following additional, optional fields.
**-n --name** - name of audio
**-a --artist** - artist of audio
**-l --album** - album of audio
**-t --time** - length of time of audio. Warning, longer=more computing power needed
**-d --description** - a prompt describing the specific audio requirements
```
python sdg/main.py -n "<name>" -a "<artist>" -l "<album>" -t 10 -d "<description of audio to generate>"
```

Once complete, this should have uploaded a new audio record to streaming-daemon. If not, a local copy should be stored in a local `assets` directory for resending.

## Running as Server
1. Start the server
```
uvicorn server:app --reload
``

2. Check health z-page
```
curl http://127.0.0.1:8000/healthz
```

3. Send Generation Request
```
curl -X POST -d {"description":"<insert audio description for LLM>"} http://127.0.0.1:8000/audio/generate
```
