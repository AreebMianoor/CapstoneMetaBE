# Little Lemon Restaurant API

This project is a Django-based API for the Little Lemon restaurant, providing endpoints for menu items, bookings, and user authentication.

## Setup

1. Clone the repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your MySQL database and update the `DATABASES` configuration in `settings.py`
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```
   python manage.py runserver
   ```

## Available Endpoints

### Authentication

- `POST /auth/token/login/`: Obtain an authentication token
  - Request body: `{"username": "your_username", "password": "your_password"}`
  - Response: `{"auth_token": "your_token"}`

- `POST /auth/token/logout/`: Logout (invalidate token)
  - Requires Authentication

### Menu Items

- `GET /restaurant/menu/`: List all menu items
  - Requires Authentication

- `POST /restaurant/menu/`: Create a new menu item
  - Requires Authentication
  - Request body: `{"title": "Item Name", "price": "10.99", "inventory": 100}`

- `GET /restaurant/menu/<int:pk>`: Retrieve a specific menu item
  - Requires Authentication

- `PUT /restaurant/menu/<int:pk>`: Update a specific menu item
  - Requires Authentication
  - Request body: `{"title": "Updated Name", "price": "11.99", "inventory": 90}`

- `DELETE /restaurant/menu/<int:pk>`: Delete a specific menu item
  - Requires Authentication

### Bookings

- `GET /restaurant/booking/`: List all bookings
  - Requires Authentication

- `POST /restaurant/booking/`: Create a new booking
  - Requires Authentication
  - Request body: `{"name": "John Doe", "no_of_guests": 4, "booking_date": "2023-12-31T19:00:00Z"}`

### Other

- `GET /restaurant/message/`: Get a protected message
  - Requires Authentication

## How to Use

1. Obtain an authentication token by sending a POST request to `/auth/token/login/` with your username and password.

2. Include the token in the header of your requests:
   ```
   Authorization: Token your_token_here
   ```

3. You can now access the protected endpoints.

4. To logout and invalidate the token, send a POST request to `/auth/token/logout/`.

## Running Tests

To run the tests for this project, use the following command:

`python manage.py test restaurant.tests`
