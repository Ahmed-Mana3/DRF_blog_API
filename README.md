# Django Blog API v1.0.0

A comprehensive REST API for a blog platform built with Django and Django REST Framework. This API provides user authentication, blog management, and user profile features with JWT authentication.

## 🚀 Features

- **User Authentication**: JWT-based authentication with token refresh
- **User Registration**: Create new user accounts with profile information
- **Blog Management**: Create, read, update, and delete blog posts
- **User Profiles**: Update user profile information and social media links
- **Image Support**: Upload profile pictures and blog images
- **Draft System**: Save blog posts as drafts before publishing
- **Category System**: Organize blogs by categories (Technology, Economy, Business, Sports)
- **Slug Generation**: Automatic URL-friendly slug generation for blogs

## 🛠️ Technology Stack

- **Django 5.2.6**: Web framework
- **Django REST Framework 3.16.1**: API framework
- **JWT Authentication**: Secure token-based authentication
- **SQLite**: Database (development)
- **Pillow**: Image processing
- **Custom User Model**: Extended user model with additional fields

## 📋 Prerequisites

- Python 3.8+
- pip (Python package installer)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Django_blog_API
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## 📚 API Endpoints

### Authentication Endpoints

#### 1. User Registration
- **Endpoint**: `POST /register_user/`
- **Description**: Register a new user account
- **Authentication**: Not required
- **Request Body**:
  ```json
  {
    "username": "johndoe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "password": "securepassword123"
  }
  ```
- **Response**: `201 Created`
  ```json
  {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe"
  }
  ```

#### 2. Obtain JWT Token
- **Endpoint**: `POST /token/`
- **Description**: Get access and refresh tokens for authentication
- **Authentication**: Not required
- **Request Body**:
  ```json
  {
    "username": "johndoe",
    "password": "securepassword123"
  }
  ```
- **Response**: `200 OK`
  ```json
  {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
  ```

#### 3. Refresh JWT Token
- **Endpoint**: `POST /token_refresh/`
- **Description**: Get a new access token using refresh token
- **Authentication**: Not required
- **Request Body**:
  ```json
  {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
  ```
- **Response**: `200 OK`
  ```json
  {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
  ```

### Blog Endpoints

#### 4. Create Blog Post
- **Endpoint**: `POST /create_blog/`
- **Description**: Create a new blog post
- **Authentication**: Required (JWT Token)
- **Headers**: `Authorization: Bearer <access_token>`
- **Request Body**:
  ```json
  {
    "title": "My First Blog Post",
    "content": "This is the content of my blog post...",
    "category": "Technology",
    "blog_image": "<file_upload>",
    "is_draft": false
  }
  ```
- **Response**: `201 Created`
  ```json
  {
    "id": 1,
    "title": "My First Blog Post",
    "slug": "my-first-blog-post",
    "content": "This is the content of my blog post...",
    "category": "Technology",
    "blog_image": "http://127.0.0.1:8000/img/blog_images/image.jpg",
    "author": {
      "id": 1,
      "username": "johndoe",
      "first_name": "John",
      "last_name": "Doe"
    },
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T10:30:00Z",
    "publish_date": "2024-01-15T10:30:00Z",
    "is_draft": false
  }
  ```

#### 5. List Blog Posts
- **Endpoint**: `GET /list_blogs/`
- **Description**: Get all published blog posts (non-draft)
- **Authentication**: Not required
- **Response**: `200 OK`
  ```json
  [
    {
      "id": 1,
      "title": "My First Blog Post",
      "slug": "my-first-blog-post",
      "content": "This is the content of my blog post...",
      "category": "Technology",
      "blog_image": "http://127.0.0.1:8000/img/blog_images/image.jpg",
      "author": {
        "id": 1,
        "username": "johndoe",
        "first_name": "John",
        "last_name": "Doe"
      },
      "created_at": "2024-01-15T10:30:00Z",
      "updated_at": "2024-01-15T10:30:00Z",
      "publish_date": "2024-01-15T10:30:00Z",
      "is_draft": false
    }
  ]
  ```

#### 6. Update Blog Post
- **Endpoint**: `PUT /update_blog/<int:pk>/`
- **Description**: Update an existing blog post
- **Authentication**: Required (JWT Token)
- **Headers**: `Authorization: Bearer <access_token>`
- **URL Parameters**: `pk` - Blog post ID
- **Request Body**:
  ```json
  {
    "title": "Updated Blog Post Title",
    "content": "Updated content...",
    "category": "Business",
    "is_draft": false
  }
  ```
- **Response**: `202 Accepted` (Success) or `403 Forbidden` (Not authorized)
  ```json
  {
    "id": 1,
    "title": "Updated Blog Post Title",
    "slug": "updated-blog-post-title",
    "content": "Updated content...",
    "category": "Business",
    "author": {
      "id": 1,
      "username": "johndoe",
      "first_name": "John",
      "last_name": "Doe"
    },
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T11:00:00Z",
    "publish_date": "2024-01-15T10:30:00Z",
    "is_draft": false
  }
  ```

#### 7. Delete Blog Post
- **Endpoint**: `DELETE /delete_blog/<int:pk>/`
- **Description**: Delete a blog post
- **Authentication**: Required (JWT Token)
- **Headers**: `Authorization: Bearer <access_token>`
- **URL Parameters**: `pk` - Blog post ID
- **Response**: `202 Accepted` (Success) or `403 Forbidden` (Not authorized)
  ```json
  {
    "message": "Blog deleted successfuly"
  }
  ```

### User Profile Endpoints

#### 8. Update User Profile
- **Endpoint**: `PUT /update_user_profile/`
- **Description**: Update user profile information
- **Authentication**: Required (JWT Token)
- **Headers**: `Authorization: Bearer <access_token>`
- **Request Body**:
  ```json
  {
    "username": "johndoe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "bio": "I am a passionate blogger...",
    "profile_picture": "<file_upload>",
    "facebook": "https://facebook.com/johndoe",
    "instagram": "https://instagram.com/johndoe",
    "youtube": "https://youtube.com/johndoe",
    "twitter": "https://twitter.com/johndoe"
  }
  ```
- **Response**: `202 Accepted`
  ```json
  {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "bio": "I am a passionate blogger...",
    "profile_picture": "http://127.0.0.1:8000/img/profile_pics/profile.jpg",
    "facebook": "https://facebook.com/johndoe",
    "instagram": "https://instagram.com/johndoe",
    "youtube": "https://youtube.com/johndoe",
    "twitter": "https://twitter.com/johndoe"
  }
  ```

## 🔐 Authentication

This API uses JWT (JSON Web Token) authentication. To access protected endpoints:

1. **Register a user** using `/register_user/`
2. **Get tokens** using `/token/` with your credentials
3. **Include the access token** in the Authorization header:
   ```
   Authorization: Bearer <your_access_token>
   ```

### Token Expiration
- **Access Token**: 30 minutes
- **Refresh Token**: Use `/token_refresh/` to get a new access token

## 📊 Data Models

### CustomUser Model
Extended Django user model with additional fields:
- `bio`: Text field for user biography
- `profile_picture`: Image field for profile photo
- `facebook`, `instagram`, `youtube`, `twitter`: URL fields for social media links

### Blog Model
- `title`: Blog post title
- `slug`: URL-friendly identifier (auto-generated)
- `content`: Blog post content
- `category`: Choice field (Technology, Economy, Business, Sports)
- `blog_image`: Image field for blog post image
- `author`: Foreign key to CustomUser
- `created_at`, `updated_at`: Timestamps
- `publish_date`: Publication date
- `is_draft`: Boolean field for draft status

## 🎯 Category Options

Blog posts can be categorized as:
- **Technology**
- **Economy**
- **Business**
- **Sports**

## 📁 File Uploads

The API supports file uploads for:
- **Profile Pictures**: Uploaded to `media/profile_pics/`
- **Blog Images**: Uploaded to `media/blog_images/`

Access uploaded files via: `http://127.0.0.1:8000/img/<file_path>`

## 🚨 Error Handling

The API returns appropriate HTTP status codes:
- `200 OK`: Successful GET requests
- `201 Created`: Successful POST requests
- `202 Accepted`: Successful PUT/DELETE requests
- `400 Bad Request`: Invalid request data
- `403 Forbidden`: Unauthorized access
- `404 Not Found`: Resource not found

## 🔧 Development

### Running Tests
```bash
python manage.py test
```

### Database Admin
Access the Django admin interface at `http://127.0.0.1:8000/admin/`

### API Documentation
The API follows RESTful conventions and returns JSON responses.

## 📝 Notes

- Only published blogs (non-draft) are returned in the blog list endpoint
- Users can only update/delete their own blog posts
- Automatic slug generation ensures unique URLs for blog posts
- JWT tokens expire after 30 minutes for security
- All file uploads are stored in the `media/` directory

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

---

**API Base URL**: `http://127.0.0.1:8000/`

For any questions or support, please refer to the Django REST Framework documentation or create an issue in the repository.