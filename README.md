# APK-Alekseevski backend

## API Endpoints

### Auth 

### News
- /api/v1/news/ (News create and list endpoint)
- /api/v1/news/{slug}/ (News retrieve, update and destroy endpoint)
### Products
- /api/v1/products/ (Products create and list endpoint)
- /api/v1/products/{slug}/ (Products retrieve, update and destroy endpoint)
### Category
- /api/v1/category/ (Products create and list endpoint)
- /api/v1/category/{slug}/ (Products retrieve, update and destroy endpoint)
### Catalog
- /api/v1/catalog/ (List all categories)
- /api/v1/catalog/{slug_category}/ (List all products in a category)
- /api/v1/catalog/{slug_category}/{slug_product}/ (View selected product)
### Bidding
- /api/v1/bidding/ (Bidding create and list endpoint)
- /api/v1/bidding/{id}/ (Bidding retrieve, update and destroy endpoint)
### Application bidding
- /api/v1/application-bidding/ (Application bidding create and list endpoint)
- /api/v1/application-bidding/{id}/ (Application bidding retrieve, update and destroy endpoint)
### Purchase
- /api/v1/purchase/ (Purchase create and list endpoint)
- /api/v1/purchase/{id}/ (Purchase retrieve, update and destroy endpoint)
### Application purchase
- /api/v1/application-purchase/ (Application purchase create and list endpoint)
- /api/v1/application-purchase/{id}/ (Application purchase retrieve, update and destroy endpoint)




## Install
#### 1.  Clone repo https://github.com/INDEX-GG/APK-Alekseevski-backend
#### 2.  Create a virtual environment and activate
 - `pip install virtualenv`
 - `python3 -m venv env`
 - `source env/bin/activate` 
#### 3.```pip install -r requirements.txt```




