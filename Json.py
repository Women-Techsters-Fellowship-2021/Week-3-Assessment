import json
from marshmallow import Schema, fields, post_load
from pprint import pprint

class UserSchema(Schema):
    issue = fields.String()
    item_number = fields.Integer()

   

complains_string = '''
{
    "complains": [
    "issue": "The item was in bad quality",
    "item_number": "123456",
    "quantity": "2kgs"
    

},
{
    "issue": "I received different size from what I ordered",
    "item_number": "234567",
    "quantity":  "1kg"

   }
 ]
}
''' 

schema = UserSchema()
user = schema.load(complains_string)

