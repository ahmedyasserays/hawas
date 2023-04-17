# Hawas (e-commerce)

## installation for local dev

make sure you have python3 installed

- create new virtual env 
    `python -m venv venv`

- activate the virtual env
    - for linux: 
        `source venv/bin/activate`

    - for windows: 
        `venv\Scripts\activate`

- install the required packages 
    `pip install -r requirements.txt`

- create a new file in the root directory and name it `.env`
    - copy the content of `.env.example` and paste it in the new file

- migrate the database
    `python manage.py migrate`

- run the project 
    `python manage.py runserver`

- if you want to create a superuser for admin site
    `python manage.py createsuperuser`

- if you want to add fake data
    `python manage.py fake_data`

## API Documentation

- Add and remove items to wishlist 
    url: /api/wishlist/<int:prod_id>/
    methods: POST, DELETE
    headers: {'X-CSRFToken': csrftoken} // the csrf token is in the cookie with the name 'csrftoken'

```
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

```