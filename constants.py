class Headers:
    
    def auth(auth_key): 
        return {'Authorization': f'JWT {auth_key}'}
