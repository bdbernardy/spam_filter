# spam_filter

## TRICKS
- activate virtual env: source .venv/bin/activate
- use raise HTTPException(status_code=404, detail="Item not found") to raise http exceptions
- use pydantic for partial updates (https://fastapi.tiangolo.com/tutorial/body-updates/)

## TODO
- Create the FastApi service to get, add, edit, and delete items in the training set (with integration tests and proper open id documentation)
- Create the training_set database service to get, add, edit, and delete items in the training set database
- Create the spam_filter service using the examples from Medium (with unit tests)
- Create a script to load the csv training set into the database
- Add a FastApi endpoint that tests if a new text is a spam or not (with integration tests)
- Create a gRPC service that tests if a new text is a spam or not (with integration tests)
- Add proper error handling
- Add logging with Elastic Search
