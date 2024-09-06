# E-Commerce Project

Welcome to the E-Commerce Project! This is a Django-based eCommerce platform designed to provide a robust solution for online shopping. 

## Features

- **User Authentication**: Sign up, log in, and manage user accounts.
- **Product Management**: Add, update, and view products.
- **Shopping Cart**: Add products to the cart, view cart, and proceed to checkout.
- **Order Management**: View order history and track orders.
- **Admin Dashboard**: Manage users, products, and orders through an admin interface.

## Installation

### Prerequisites

- Python 3.8 or higher
- Django 5.1 or higher

### Clone the Repository

```bash
git clone https://github.com/mrizwanakram786/Greatkart_E-Commerce_Django_Project.git
cd Greatkart_E-Commerce_Django_Project
```

### Set Up the Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Configure the Environment

Create a `.env` file in the project root and add the following environment variables:

```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3  # or your database configuration
ALLOWED_HOSTS=localhost, 127.0.0.1
```

### Apply Migrations

Run the database migrations:

```bash
python manage.py migrate
```

### Create a Superuser

Create an admin user to access the Django admin interface:

```bash
python manage.py createsuperuser
```

### Run the Development Server

Start the development server:

```bash
python manage.py runserver
```

You can now access the application at `http://127.0.0.1:8000/`.

## Usage

- **Home Page**: Browse products and access various features.
- **Admin Interface**: Navigate to `http://127.0.0.1:8000/admin/` to manage the application.
- **User Dashboard**: View and manage your orders and profile.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Commit your changes: `git commit -am 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Create a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [mrizwanakram786](mailto:mrizwanakramrizwan@gmail.com).

---

Feel free to modify the sections to better fit your project's specifics. If you have additional features or setup instructions, be sure to include those as well!
