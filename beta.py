from fastapi import FastAPI, HTTPException
from typing import List, Optional
import random
import string
import time

app = FastAPI()

# Mock data for demonstration purposes
orders = []

@app.get('/orders', response_model=List[dict])
async def list_orders():
    '''List all orders'''
    return [{'order': order} for order in orders]

@app.post('/orders', response_model=dict, status_code=201)
async def create_order(external_id: str, external_source: str, billing_address: dict, shipping_address: dict, order_details: dict, amount: float):
    '''Create a new order'''
    # Generate an order ID
    order_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    # Create a new order
    order = {
        'id': order_id,
        'external_id': external_id,
        'created_at': int(time.time()),
        'updated_at': int(time.time()),
        'external_source': external_source,
        'addresses': {
            'billing': billing_address,
            'shipping': shipping_address
        },
        'order_details': order_details,
        'payments': {
            'amount': amount
        }
    }

    # Add the order to the list
    orders.append(order)

    # Return the new order
    return {'order': order}

@app.get('/orders/{order_id}', response_model=dict)
async def get_order(order_id: str):
    '''Fetch an order given its identifier'''
    for order in orders:
        if order['id'] == order_id:
            return {'order': order}
    raise HTTPException(status_code=404, detail='Order not found')

@app.put('/orders/{order_id}', response_model=dict)
async def update_order(order_id: str):
    '''Update an order given its identifier'''
    pass

@app.delete('/orders/{order_id}', response_model=dict)
async def delete_order(order_id: str):
    '''Delete an order given its identifier'''
    pass

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)