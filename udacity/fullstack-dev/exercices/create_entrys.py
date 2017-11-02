from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# With wich database we want to communicate
engine = create_engine('sqlite:///restaurantmenu.db')

# Bind to the engine
# Make the connections between our class defintions and their corresponding tables within our database
Base.metadata.bind = engine

# create a link of comminucation between our code executions and the engine we created
DBSession = sessionmaker(bind = engine)

# Communication interface for read, update, delete
session = DBSession()
myFirstRestaurant = Restaurant(name = "Pizza Palace")

# Add my first restaurant to the staging zone
session.add(myFirstRestaurant)

# Ecriture des modifications dans la BDD
session.commit()

print(session.query(Restaurant).all())

cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella", course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)

session.add(cheesepizza)
session.commit()
print(session.query(MenuItem).all())

firstResult = session.query(restaurant).first()
print(firstresult.name)

items = session.query(MenuItem).all()
for item in items:
    print item.name

veggieBurgers = session.query(MenuItem).filter_by(name= 'Veggie Burger')

for veggieBurger in veggieBurgers:
    if veggieBurger.price != '2.99':
        veggieBurger.price = '$2.99'
        session.add(veggieBurger)
        session.commit()
