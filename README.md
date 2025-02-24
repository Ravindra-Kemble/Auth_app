# django-rest-api
A REST api written in Django

## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```sh
        pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```sh
        git clone https://github.com/Ravindra-Kemble/Auth_app.git
    ```

* #### Dependencies
    1. Create and fire up your virtual environment:
        ```sh
             virtualenv  venv -p python3
             venv/scripts/activate
        ```
    3. Install the dependencies needed to run the app:
        ```sh
             cd Auth_app
             pip install -r requirements.txt
        ```
    4. Make those migrations work
        ```sh
            python manage.py makemigrations
            python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```sh
        python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/api/
    ```
    
    #### API Endpoints

1. **User Registration**:
   - POST /api/register
     - Request: { "email": "user@example.com" }
     - Response: { "message": "Registration successful. Please verify your email." }

2. **Request OTP**:
   - POST /api/request-otp
     - Request: { "email": "user@example.com" }
     - Response: { "message": "OTP sent to your email." }

3. **Verify OTP**:
   - POST /api/verify-otp
     - Request: { "email": "user@example.com", "otp": "123456" }
     - Response: { "message": "Login successful.", "token": "jwt_token" }
