import os
import random
import string
import time

from flask import Flask, request
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)

# Mock data for demonstration purposes
orders = []

@api.route('/orders')
class OrderList(Resource):
    @api.doc('list_orders')
    def get(self):
        '''List all orders'''
        return [{'order': order} for order in orders]

    @api.doc('create_order')
    def post(self):
        '''Create a new order'''
        data = request.get_json()

        # Generate an order ID
        order_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

        # Create a new order
        order = {
            'id': order_id,
            'external_id': data['external_id'],
            'created_at': int(time.time()),
            'updated_at': int(time.time()),
            'external_source': data['external_source'],
            'addresses': {
                'billing': data['billing_address'],
                'shipping': data['shipping_address']
            },
            'order_details': data['order_details'],
            'payments': {
                'amount': data['amount']
            }
        }

        # Add the order to the list
        orders.append(order)

        # Return the new order
        return {'order': order}, 201

@api.route('/orders/<string:order_id>')
@api.param('order_id', 'The order identifier')
class Order(Resource):
    @api.doc('get_order')
    def get(self, order_id):
        '''Fetch an order given its identifier'''
        for order in orders:
            if order['id'] == order_id:
                return {'order': order}
        return {'message': 'Order not found'}

    @api.doc('update_order')
    def put(self, order_id):
        '''Update an order given its identifier'''
        pass

    @api.doc('delete_order')
    def delete(self, order_id):
        '''Delete an order given its identifier'''
        pass
