def connect_db(case):
    try:
        if case == 1:
            raise Exception('Error connecting to the database')
        else:
            return 'Connected to the database'
    except Exception as e:
        return str(e)
    
s = connect_db(1)
print(s)
    