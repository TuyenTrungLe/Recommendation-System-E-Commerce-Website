
# Product Recommendation and Categorization E-Commerce Platform

This project is an **E-Commerce Web Application** built using the Django framework. It incorporates Machine Learning techniques to provide intelligent **Product Categorization** and **Product Recommendation** systems, creating a personalized shopping experience for buyers and a streamlined workflow for sellers.

---

## Website Overview

### **Buyer's Experience**
- **Product Categorization**: The platform uses Naive Bayes Classification for automated and accurate categorization of products.
- **Registration**: Buyers must register to make purchases, ensuring a secure and personalized shopping journey.
- **Recommendation System**: A product recommendation system powered by **Cosine Similarity** enhances the user experience by suggesting relevant products based on browsing and purchase history.

### **Seller's Experience**
- **Vendor Registration**: Sellers can register and provide company details to start listing products.
- **Automated Categorization**: Products are automatically categorized using Naive Bayes Classification, saving time and effort.
- **Product Management**: Sellers can manage their product inventory, including adding, editing, and deleting listings.
- **Order Management**: Sellers can efficiently handle orders and update statuses for smooth transaction processes.

---

## Key Features
1. **Efficient Product Categorization**:
   - Simplifies the product listing process for sellers using machine learning techniques.
2. **Personalized Recommendations**:
   - Recommends products based on user preferences and history.
3. **Vendor Management**:
   - Allows sellers to manage their products, orders, and payments seamlessly.

---

## Installation on Local Machine

### **Environment**: Python 3 (3.9.5 recommended)

### **Steps**:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/TwoPointerr/ProductRecommendation.git
   cd ./ProductRecommendation
   ```

2. **Create a Virtual Environment (Optional but Recommended)**:
   ```bash
   # Install virtualenv if not installed
   pip install virtualenv

   # Create a virtual environment
   python -m venv venv

   # Activate the virtual environment
   # On Windows
   venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**:
   Adjust the database configuration in `ProductRecommendation/eshop/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'mssql',
           'NAME': config('name'),
           'USER': config('user'),
           'PASSWORD': config('pass'),
           'HOST': config('host'),
           'PORT': config('port'),
           'OPTIONS': {
               'driver': 'ODBC Driver 17 for SQL Server',
               'MARS_Connection': True,
               'Encrypt': 'yes',
               'TrustServerCertificate': 'no',
           },
       }
   }
   ```

5. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser (Optional)**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

---

## Technologies Used

- **Backend Framework**: Django
- **Database**: Microsoft SQL Server
- **Machine Learning Techniques**:
  - **Naive Bayes Classification** for Product Categorization
  - **Cosine Similarity** for Product Recommendations
- **Frontend**: HTML, CSS, JavaScript (via Django templates)
- **Deployment**: Configured with Docker and Nginx for production readiness.

---

## Folder Structure
```plaintext
ProductRecommendation/
├── apps/                  # Contains modular Django apps
├── eshop/                 # Main Django project folder
├── media/                 # Uploaded media files
├── nginx/                 # Configuration for Nginx server
├── static/                # Static files (CSS, JS, Images)
├── templates/             # HTML templates for the frontend
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── Dockerfile             # Docker configuration for deployment
```

---

## Key Objectives Achieved
1. **Automated Product Categorization** using Naive Bayes Classification.
2. **Product Recommendation System** leveraging Cosine Similarity for personalized suggestions.
3. **User-friendly Vendor and Buyer Management** functionalities.

---

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, open an issue first to discuss your suggestions.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contact
For any inquiries, please contact the developer:
- **Email**: trungtuyenlevn@gmail.com
