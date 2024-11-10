# URL Shortener REST API

A simple URL shortening service built using Django REST Framework and PostgreSQL, deployed on [Railway](https://railway.app/). This service allows users to shorten long URLs using an MD5 hash-based algorithm.

## API Endpoint:

**URL:** `https://sit.up.railway.app/api/shorten`  
**Method:** `POST`  

**Request Body:**
```json
{
    "original_url": "https://www.example.com/your/long/url"
}
