def userEntity(item) -> dict:
        return {
            'id': str(item['_id']),
            'first_name': item['first_name'],
            'last_name': item['last_name'],
            'date_birth': item['date_birth'],
            'address': item['address'],
            'password': item['password'],
            'email': item['email'],
            'mobil_phone': item['mobil_phone'],
            
            
        }

def usersEntity (entity) ->  list:
     return[userEntity(item)for item in entity]
