from fastapi import FastAPI, HTTPException
from typing import List, Optional

app = FastAPI()

# Mock data for demonstration purposes
products = [
    {
        "style_id": 1,
        "style_code": "SC1",
        "name": "Product 1",
        "colours": [
            {
                "colour_id": 1,
                "colour_code": "CC1",
                "name": "Red",
                "sizes": [
                    {
                        "size_id": 1,
                        "size_code": "S",
                        "price": 10.0,
                        "barcode": "123456789012"
                    }
                ]
            }
        ]
    }
]

@app.get("/products", response_model=List[dict])
async def list_products():
    '''List all products'''
    return products

@app.post("/products", response_model=dict)
async def create_product(
    style_id: int,
    style_code: str,
    name: str,
    colours: List[dict],  # List of dictionaries for colors
    sizes: List[dict]     # List of dictionaries for sizes
):
    '''Create a new product'''
    new_product = {
        "style_id": style_id,
        "style_code": style_code,
        "name": name,
        "colours": colours,
    }
    for color in new_product['colours']:
        color['sizes'] = sizes  # Add sizes to each color
    products.append(new_product)
    return new_product

@app.get("/products/{product_id}", response_model=dict)
async def get_product(product_id: int):
    '''Fetch a product given its identifier'''
    for product in products:
        if product['style_id'] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.put("/products/{product_id}", response_model=dict)
async def update_product(product_id: int, product: dict):
    '''Update a product given its identifier'''
    for idx, existing_product in enumerate(products):
        if existing_product['style_id'] == product_id:
            products[idx] = product
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}", response_model=dict)
async def delete_product(product_id: int):
    '''Delete a product given its identifier'''
    for idx, existing_product in enumerate(products):
        if existing_product['style_id'] == product_id:
            deleted_product = products.pop(idx)
            return deleted_product
    raise HTTPException(status_code=404, detail="Product not found")

@app.get("/", response_model=dict)
async def root():
    return {"message": "Welcome to the Groceries Plugin API!"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
