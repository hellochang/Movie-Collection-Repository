DEBUG = True
PORT = 8080
SECRET_KEY = "secret"
WTF_CSRF_ENABLED = True

PASSWORDS = {
    "admin": "$pbkdf2-sha256$29000$9z5HiJESIoTwvjfG2Nu79w$i253ffTI2iYAcdXpgLymtqcDSL3Ocl8ttB.4N3CtEY4",
    "normaluser": "$pbkdf2-sha256$29000$4TwH4PzfO4dwLgUAwJiT0g$hQwIIht8hLRz2z5M8tQlsJUfcnEGq2VS5YqQ4dyyYiY",
}

ADMIN_USERS = ["admin"]
