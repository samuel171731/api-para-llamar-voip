# api-para-llamar-voip
Flask Asterisk Call API

This repository contains a Flask application that interfaces with an Asterisk PBX system to initiate phone calls via a RESTful API. The application listens for POST requests containing the phone number to call and then uses Asterisk to place the call.
Table of Contents

    Installation
    Configuration
    Usage
    API Endpoint
    Logging
    Error Handling
    Contributing
    License

Installation

    Clone the repository:

    bash

git clone https://github.com/yourusername/flask-asterisk-call-api.git
cd flask-asterisk-call-api

Create a virtual environment and activate it:

bash

python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

Install the required packages:

bash

    pip install -r requirements.txt

    Ensure Asterisk is installed and configured on the server where this Flask application will run.

Configuration

The Flask application runs on port 5000 by default and listens on all available network interfaces (0.0.0.0). You can change these settings in the app.run() call at the bottom of the script if needed.
Usage

    Start the Flask application:

    bash

    python app.py

    Send a POST request to the /realizar_llamada endpoint with the phone number in the request body.

API Endpoint
/realizar_llamada (POST)

This endpoint initiates a call to the provided phone number using Asterisk.
Request

    Method: POST
    Headers: Content-Type: application/x-www-form-urlencoded
    Body: Include the phone number in a form field, e.g., numero=value

Response

    Success:
        Code: 200
        Content: {'message': 'Llamada realizada exitosamente', 'data': {<submitted data>}}
    Failure:
        Code: 400 if the phone number is not provided
        Content: {'error': 'Número de teléfono no proporcionado'}
        Code: 500 if there's an error executing the call
        Content: {'error': 'Error al realizar la llamada: <error_message>'}

Logging

The application logs detailed debugging information, including HTTP method, headers, and request data. Logs can help troubleshoot issues related to the request and the execution of the Asterisk command.
Error Handling

The application handles errors in two main scenarios:

    Missing phone number in the request: Returns a 400 status code with an appropriate error message.
    Asterisk command execution failure: Returns a 500 status code with the error details.

Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
License

This project is licensed under the MIT License.
