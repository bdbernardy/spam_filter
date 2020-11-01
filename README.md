# spam_filter

## TRICKS
- activate virtual env: source .venv/bin/activate
- run export PYTHONPATH=$PWD to add current path to PYTHONPATH
- use raise HTTPException(status_code=404, detail="Item not found") to raise http exceptions

## TODO
- Add training_set integration tests
- Add training_set openApi documentation
- Create the spam_filter service using the examples from Medium (with unit tests)
- Create a script to load the csv training set into the database
- Add a FastApi endpoint that tests if a new text is a spam or not (with integration tests)
- Create a gRPC service that tests if a new text is a spam or not (with integration tests)
- Add proper error handling
- Add logging with Elastic Search
