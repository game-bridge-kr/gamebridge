
# Requirements
- python 3.10+


# How to start fastAPI server
1. go to ```apps/server```
2. ```server % python3 -m venv .venv```
3. ```server % source .venv/bin/activate```
4. ```server % pip install -r requirements.txt```
5. go to ```apps``` 
6. ```apps % uvicorn server.main:app --reload```
