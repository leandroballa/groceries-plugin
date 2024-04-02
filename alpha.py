from fastapi import FastAPI, HTTPException

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

@app.get("/products")
async def list_products():
    '''List all products'''
    return {"products": products}

@app.post("/products")
async def create_product():
    '''Create a new product'''
    # Implement creation logic here
    pass

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    '''Fetch a product given its identifier'''
    for product in products:
        if product['style_id'] == product_id:
            return {'product': product}
    raise HTTPException(status_code=404, detail="Product not found")

@app.put("/products/{product_id}")
async def update_product(product_id: int):
    '''Update a product given its identifier'''
    # Implement update logic here
    pass

@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    '''Delete a product given its identifier'''
    # Implement delete logic here
    pass

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
