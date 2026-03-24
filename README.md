Little Lemon Project - API Endpoints
-------------------------------------

This project is a Django web application for managing menu items, table bookings, and user authentication.

API Endpoints to Test:

1. User Registration:
   POST /api/registration/
   Example: 
   {
       "username": "user1",
       "password": "password123",
       "email": "user1@example.com"
   }

2. User Login:
   POST /api/token/
   Example:
   {
       "username": "user1",
       "password": "password123"
   }

3. Menu Items:
   GET /api/menu/
   GET /api/menu/<id>/  # Retrieve details of a specific menu item
   GET /api/menu/category/<category_id>/  # Filter menu items by category

4. Categories:
   GET /api/categories/

5. Table Bookings:
   GET /api/bookings/  # Get all bookings
   POST /api/bookings/  # Create a new booking
   GET /api/bookings?date=YYYY-MM-DD  # Filter bookings by date

6. Cart (for customers):
   GET /api/cart/
   POST /api/cart/  # Add item to cart

7. Orders:
   GET /api/orders/  # View your orders
   POST /api/orders/  # Place an order
   PATCH /api/orders/<id>/deliver/  # Mark order as delivered (delivery crew only)

Notes for Reviewers:
- Make sure to register first to get access tokens for protected endpoints.
- Use token authentication in the headers to test endpoints that require login.
- You can test APIs using tools like **Insomnia** or **Postman**.
