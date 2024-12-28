class Orders :
    def __init__ (self , order_id , date , time , username , email , price , tip , offer , total , notes , item_name ,amount ):
       self.__order_id =int(order_id)
       self.__date = date 
       self.__time = time
       self.__username =str(username)
       self.__email = str(email)
       self.__price =float(price)
       self.__tip = float(tip)
       self.__offer = offer 
       self.__total = float(total)
       self.__notes = str(notes)
       self.__dict={"itemname":item_name,"amount":amount}

    def set_item_name(self ,item_name):
        self.__item_name = str(item_name)
    def get_item_name(self):
        return self.__item_name

    def set_amount(self ,amount):
        self.__amount = float (amount)
    def get_amount(self):
        return self.__amount


    def set_order_id(self, order_id):
        self.__order_id = int (order_id)
    def get_order_id(self):
        return self.__order_id

    def set_date(self , date) :
        self.__date = date
    def get_date(self ) :
        return self.__date

    def set_time(self, time):
        self.__time= time
    def get_time(self):
        return self.__time

    def set_username(self, username):
        self.__username = str (username)
    def get_username(self):
        return self.__username

    def set_email(self, email):
        self.__email =  str (email)
    
    def get_email(self):
        return self.__email

    def set_price(self,price):
        self.__price = float (price)    
    def get_price(self):
        return self.__price

    def set_tip(self,tip):
        self.__tip = float (tip)   
    def get_tip(self):
        return self.__tip

    def set_offer(self,offer):
        self.__offer = float (offer)       
    def get_offer(self):
        return self.__offer

    def set_total(self,total):
        self.__total= float (total)           
    def get_total(self):
        return self.__total

    def set_notes(self,notes):
        self.__notes= str (notes)          
    def get_notes(self):
        return self.__notes

    def set_items(self,items):
        self.__items= str (items)                  
    def get_items(self):
        return self.__items  

class Log :
    def __init__ (self , date , time , username , action) :
       self.__date = date 
       self.__time = time 
       self.__username = str(username)
       self.__action = str (action) 
    
    def set_date(self ,date ):
        self.__date = date

    def get_date(self):
        return self.__date

    def set_time(self ,time):
        self.__time = time
    
    def get_time(self):
        return self.__time

    def set_username(self ,username):
        self.__username = str (username)
    
    def get_username(self):
        return self.__username

    def set_action(self , action ):
        self.__action = action
    
    def get_action(self):
        return self.__action

class Users :
    def __init__(self, username, profile_picture, user_type, password_hash):
        self.__username = str(username) 
        self.__profile_picture = profile_picture
        self.__user_type = str(user_type)
        self.__password_hash = str(password_hash)

    def set_username(self, username):
        self.__username = str(username)

    def set_profile_picture(self, profile_picture):
        self.__profile_picture = str(profile_picture)

    def set_user_type(self, user_type):
        self.__user_type = str(user_type)

    def set_password_hash(self, password_hash):
        self.__password_hash = str(password_hash)

    def get_username(self):
        return self.__username

    def get_profile_picture(self):
        return self.__profile_picture

    def get_user_type(self):
        return self.__user_type

    def get_password_hash(self):
        return self.__password_hash
    

class Customers:
    def __init__(self, email, full_name, phone_number):
        self.__email = str(email)
        self.__full_name = str(full_name)
        self.__phone_number = str(phone_number)

    def set_email(self, email):
        self.__email = str(email)

    def set_full_name(self, full_name):
        self.__full_name = str(full_name)

    def set_phone_number(self, phone_number):
        self.__phone_number = str(phone_number)

    def get_email(self):
        return self.__email

    def get_full_name(self):
        return self.__full_name

    def get_phone_number(self):
        return self.__phone_number

class Menu:
    def __init__(self, item_name, item_type, image, description, price, recipe):
        self.__item_name =str(item_name) 
        self.__item_type = str(item_type)
        self.__image = str(image)
        self.__description = str(description)
        self.__price = float(price)
        self.__recipe = str(recipe)

    def set_item_name(self, item_name):
        self.__item_name = str(item_name)

    def set_item_type(self, item_type):
        self.__item_type = str(item_type)

    def set_image(self, image):
        self.__image = str(image)

    def set_description(self, description):
        self.__description = str(description)

    def set_price(self, price):
        self.__price = float(price)

    def set_recipe(self, recipe):
        self.__recipe = str(recipe)

    def get_item_name(self):
        return self.__item_name

    def get_item_type(self):
        return self.__item_type

    def get_image(self):
        return self.__image

    def get_description(self):
        return self.__description

    def get_price(self):
        return self.__price

    def get_recipe(self):
        return self.__recipe
