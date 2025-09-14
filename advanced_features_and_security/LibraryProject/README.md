# Library Project

## Overview

The Library Project is a Django-based web application designed to manage library resources, including books, authors, and users. It features a custom user model with enhanced attributes and integrates permission management to control access based on user roles.

## Features

- Custom User Model with:
  - Date of Birth
  - Profile Photo
- Permission Management:
  - Custom permissions for viewing, creating, editing, and deleting resources.
  - Group-based access control (e.g., Admins, Editors, Viewers).
  
## Requirements

- Python 3.x
- Django 3.x or later
- Pillow (for image handling)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/LibraryProject.git
   cd LibraryProject