class Headers:
    
    def auth_header(auth_key): 
        return {'Authorization': f'JWT {auth_key}'}
