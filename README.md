# Tokenizer

With running spaCy in the back this API provides tokenization for English, French, German, Spanish and Portuguese. 

The [endpoint](https://tokenizer-citibeats.herokuapp.com/tokenizer) accepts POST request with JSON; the user can either provide the language of the text in the form:

{ 
"lang": "en",
"text": "whatever text you want to get tokenized
}


or have the endpoint detect the language itself. Then the request body can be simply:

{
"text": "I guess the endpoint will have to figure out what language this is"
}


Klick [here](https://tokenizer-citibeats.herokuapp.com/docs) to get to the interactive FastApi docs to try out the endpoint without Postmen et al. 

## To run the API locally follow these steps

Step 1: Clone the master branch repo into your local machine

Step 2: Create a pipenv using the requirements.txt file

> pipenv install -r requirements.txt

Step 3: Open the env

> pipenv shell

Step 4: Start the server

go to the app folder, then: 

> uvicorn main:app --reload

step 5: visit localhost 

> under http://127.0.0.1:8000/docs#/

## Dockerization 

To create an image:

> docker build -t tokenizer .

To run the container:

> docker run tokenizer











