import psycopg2
from datetime import datetime
class DatabaseManager:
    def __init__(self, config):
        self.config = config
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = psycopg2.connect(**self.config)
        self.cursor = self.connection.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def list_tables(self):
        self.connect()
        query = '''
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public';
        '''
        self.cursor.execute(query)
        tables = self.cursor.fetchall()
        self.close()
        return [table[0] for table in tables]

    def create_tables(self):
        self.connect()
        query = '''
    CREATE TABLE Users (
    username VARCHAR(250) PRIMARY KEY,
    user_type VARCHAR(100) NOT NULL,
    password_hash TEXT NOT NULL,
    user_photo BYTEA
);

CREATE TABLE Customers (
    email VARCHAR(250) PRIMARY KEY,
    full_name VARCHAR(250) NOT NULL,
    phone_number VARCHAR(15) NOT NULL
);

CREATE TABLE Menu (
    item_name VARCHAR(250) PRIMARY KEY,
    type VARCHAR(100) NOT NULL,
    image TEXT,
    description TEXT,
    price NUMERIC(10, 2) NOT NULL,
    recipe TEXT
);
CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    time TIME NOT NULL,
    username VARCHAR(250),
    email VARCHAR(250),
    price NUMERIC(10, 2) NOT NULL,
    tip NUMERIC(10, 2),
    offer NUMERIC(10, 2),
    total NUMERIC(10, 2) NOT NULL,
    notes TEXT,
    items JSONB NOT NULL, 
    CONSTRAINT fk_username FOREIGN KEY (username) REFERENCES Users(username),
    CONSTRAINT fk_email FOREIGN KEY (email) REFERENCES Customers(email)
);

CREATE TABLE Logs (
    date DATE NOT NULL,
    time TIME NOT NULL,
    username VARCHAR(250),
    action TEXT NOT NULL,
    CONSTRAINT fk_logs_username FOREIGN KEY (username) REFERENCES Users(username)
);


        '''
        self.cursor.execute(query)
        self.connection.commit()
        default_customer_query = '''
    INSERT INTO Customers (email, full_name, phone_number)
    VALUES ('anonymous@mawgood.com', 'Anonymous Customer', '0000000000')
    ON CONFLICT DO NOTHING;         
    '''
        self.cursor.execute(default_customer_query)
        self.connection.commit()
        self.close()

    def check_user(self,username):
    
        check_code=f"SELECT COUNT(*) FROM users WHERE username = %s;"
        check=self.cursor.execute(check_code,(username,))
        result = self.cursor.fetchone()
        
        return result[0] > 0


    def create_user(self,username,photo,user_type,pass_hash):
     try : 
        self.connect()
        check=self.check_user(username)
        if(check):
            
            return "Sorry the username u entered is already exist!"
        else:
            create_user_code=f'''
            INSERT INTO users (username, user_photo, user_type,password_hash)
            VALUES (%s, %s, %s,%s);   
             '''  
            self.cursor.execute(create_user_code,(username,photo,user_type,pass_hash))
            self.connection.commit()
           
            return "User created successfully!"
     finally:
          self.close()
             
        
    def check_userpass(self,username,user_pass):
        self.connect()
        check=self.check_user(username)
        if(check):
           check_pass=f"SELECT COUNT(*) FROM users WHERE password_hash  = '{user_pass}'"
           check=self.cursor.execute(check_pass)
           result = self.cursor.fetchone()
           self.close()
           return result[0] > 0
            
        else:
            self.close()
            return "Sorry the username u entered not available  !"             

    def insert_order(self, date, time, username, email, price, tip, offer, total, notes, items):
     try:
        self.connect()  # Ensure the connection is opened

        # Check if the customer already exists
        query_check_customer = "SELECT COUNT(*) FROM customers WHERE email = %s;"
        self.cursor.execute(query_check_customer, (email,))
        customer_exists = self.cursor.fetchone()[0]

        # If the customer doesn't exist, insert them into the Customers table
        if customer_exists == 0:
            query_insert_customer = '''
            INSERT INTO customers (email, full_name, phone_number)
            VALUES (%s, %s, %s);
            '''
            # Insert default details for the customer
            self.cursor.execute(query_insert_customer, (email, 'New Customer', '0000000000'))

        # Insert the order into the Orders table
        query_insert_order = '''
        INSERT INTO orders (date, time, username, email, price, tip, offer, total, notes, items)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        '''
        self.cursor.execute(query_insert_order, (date, time, username, email, price, tip, offer, total, notes, items))
        self.connection.commit()

        return "Order inserted successfully, and customer data added automatically (if not already present)."

     finally:
        self.close()  # Ensure the connection is closed

    
    def delete_item_from_menu(self, item_name):

        self.connect()
        
        query = '''
        DELETE FROM menu
        WHERE item_name = %s;
        ''' 
        self.cursor.execute(query, (item_name,))
        self.connection.commit()
        
        self.close()
        return f"Item '{item_name}' deleted successfully from the menu."    
    
    def add_item(self, item_name, item_type, image, description, price, recipe):
        self.connect()
        
        query = '''
        INSERT INTO menu (item_name, type, image, description, price, recipe)
       VALUES (%s, %s, %s, %s, %s, %s);
        '''
        
        self.cursor.execute(query,(item_name, item_type, image, description, price, recipe))
        self.connection.commit()
        self.close()
        return f"Item '{item_name}' added successfully to the menu."


    def add_log(self, date, time, username, action):
        self.connect()
        
        query = '''
        INSERT INTO logs (date, time, username, action)
        VALUES (%s, %s, %s, %s);
        '''
        
        self.cursor.execute(query,(date, time, username, action))
        self.connection.commit()
        return f"Log entry added successfully: {username} - {action}."


        
config = {
    'dbname': 'mawgood2',
    'user': 'postgres',
    'password': 'seif00',
    'host': 'localhost',
    'port': '5432',
}


db_manager = DatabaseManager(config)

