---
id: "0006"
title: "Solve Backend Import Error"
stage: misc
date: 2025-12-08
surface: agent
model: gemini-2.0-flash-exp
feature: 001-fullstack-todo-app
branch: null
user: sheikhqirat100@gmail.com
command: solve this error inside the backend folder
labels:
  - backend
  - bugfix
  - import-error
  - python
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - d:\q_4\ai-hackathon\full-tack\backend\main.py
tests: []
---

# Prompt

solve this error inside the backend folder

PS D:\q_4\ai-hackathon\full-tack\backend> uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['D:\\q_4\\ai-hackathon\\full-tack\\backend']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12304] using WatchFiles
Process SpawnProcess-1:
Traceback (most recent call last):
  File "C:\Program Files\Python313\Lib\multiprocessing\process.py", line 313, in _bootstrap
    self.run()
    ~~~~~~~~^^
  File "C:\Program Files\Python313\Lib\multiprocessing\process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\pc\AppData\Roaming\Python\Python313\site-packages\uvicorn\_subprocess.py", line 76, in subprocess_started
    target(sockets=sockets)
    ~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\Users\pc\AppData\Roaming\Python\Python313\site-packages\uvicorn\server.py", line 61, in run
    return asyncio.run(self.serve(sockets=sockets))
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python313\Lib\asyncio\runners.py", line 195, in run
    return runner.run(main)
           ~~~~~~~~~~^^^^^^
  File "C:\Program Files\Python313\Lib\asyncio\runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "C:\Program Files\Python313\Lib\asyncio\base_events.py", line 719, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "C:\Users\pc\AppData\Roaming\Python\Python313\site-packages\uvicorn\server.py", line 68, in serve
    config.load()
    ~~~~~~~~~~~^^
  File "C:\Users\pc\AppData\Roaming\Python\Python313\site-packages\uvicorn\config.py", line 467, in load
    self.loaded_app = import_from_string(self.app)
                      ~~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "C:\Users\pc\AppData\Roaming\Python\Python313\site-packages\uvicorn\importer.py", line 21, in import_from_string
    module = importlib.import_module(module_str)
  File "C:\Program Files\Python313\Lib\importlib\__init__.py", line 88, in import_module    
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "D:\q_4\ai-hackathon\full-tack\backend\main.py", line 2, in <module>
    from .service import router as api_router
ImportError: attempted relative import with no known parent package

# Response

Fixed the ImportError in `backend/main.py` by changing relative imports to absolute imports.
Also fixed similar relative import issues in `backend/service.py`, `backend/crud.py`, and `backend/database.py`.
Additionally, installed missing dependency `psycopg2-binary`.

## Changes
- Modified `backend/main.py`, `backend/service.py`, `backend/crud.py`, `backend/database.py`:
  - Changed relative imports (e.g., `from . import`) to absolute imports.
- Installed `psycopg2-binary` via `pip`.

This allows `uvicorn main:app --reload` to run correctly when executed from the `backend` directory.
