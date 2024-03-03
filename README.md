# streaming-daemon-generator
This service uses the AudioCraft (by Meta) for AI music generation used by the [streaming-daemon](https://github.com/jeremyKisner/streaming-daemon).

# Running Locally

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

4. Export Python Path (Windows)
```
$env:PYTHONPATH = $pwd
```

5. Run Music Generation Service
```
python sdg/main.py -n "<name>" -a "<artist>" -l "<album>" -d "<description of audio to generate>"
```

Once complete, this should have uploaded a new audio record to streaming-daemon. If not, a local copy should be stored in a local `assets` directory for resending.
