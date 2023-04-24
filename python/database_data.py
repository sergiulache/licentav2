import uuid
import random
import psycopg2
import psycopg2.extras
from faker import Faker
import csv



fake = Faker()

# Connect to your Supabase instance
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Phatiacy272",
    host="db.yqyheutdblzkrxymbhpw.supabase.co",
    port="5432"
)
psycopg2.extras.register_uuid()
cur = conn.cursor()

# Read cities and countries from the CSV file
with open('cities.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    cities = [row['city'] for row in reader]
    csvfile.seek(0)  # Reset the CSV reader to the beginning
    countries = [row['country'] for row in reader]

# Generate and insert fake data for the users table
user_ids = []
for _ in range(30):  # Create 100 fake users
    user_id = uuid.uuid4()
    user_ids.append(user_id)
    first_name = fake.first_name()
    last_name = fake.last_name()
    country = random.choice(countries)
    city = random.choice(cities)
    address = fake.street_address()
    state = fake.state_abbr()
    zip_code = fake.zipcode()
    username = fake.user_name()
    email = fake.email()
    about = fake.text(max_nb_chars=200)
    created_at = fake.date_between(start_date='-2y', end_date='today')
    completed_jobs = fake.random_int(min=0, max=300)
    
    cur.execute(
        """
        INSERT INTO users (user_id, first_name, last_name, country, address, city, state, zip, username, email, about, created_at, completed_jobs)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (user_id, first_name, last_name, country, address, city, state, zip_code, username, email, about, created_at, completed_jobs)
    )
    

# Generate and insert fake data for the items table
item_ids = []
for _ in range(10):  # Create 5 fake items
    item_id = uuid.uuid4()
    item_ids.append(item_id)
    title = fake.sentence(nb_words=4)
    description = fake.text(max_nb_chars=200)
    preferred_price = fake.random_int(min=1000, max=10000)
    preferred_date = fake.date_between(start_date='-1y', end_date='today')
    starting_bid = preferred_price - fake.random_int(min=100, max=500)
    current_bid = starting_bid
    bid_holder = fake.random_element(user_ids)
    poster_id = fake.random_element(user_ids)
    expiration_date = fake.date_between(start_date='today', end_date='+1y')
    poster_first_name = fake.first_name()
    poster_last_name = fake.last_name()
    poster_country = random.choice(countries)
    poster_address = fake.street_address()
    poster_city = random.choice(cities)
    poster_state = fake.state_abbr()
    poster_zip = fake.zipcode()
    created_at = fake.date_between(start_date='-2y', end_date='today')
    
    cur.execute(
        """
        INSERT INTO items (item_id, title, description, preferred_price, preferred_date, starting_bid, current_bid, bid_holder, poster_id, expiration_date, poster_first_name, poster_last_name, poster_country, poster_address, poster_city, poster_state, poster_zip, created_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (item_id, title, description, preferred_price, preferred_date, starting_bid, current_bid, bid_holder, poster_id, expiration_date, poster_first_name, poster_last_name, poster_country, poster_address, poster_city, poster_state, poster_zip, created_at)
    )

# Generate and insert fake data for the bids table
for _ in range(200):  # Create 20 fake bids
    bid_id = uuid.uuid4()
    bidder_id = fake.random_element(user_ids)
    item_id = fake.random_element(item_ids)
    bid_amount = fake.random_int(min=1000, max=10000)
    created_at = fake.date_between(start_date='-1y', end_date='today')
    bid_completion_date = fake.date_between(start_date='today', end_date='+1y')
    bid_completion_time = fake.random_int(min=1, max=100)
    
    cur.execute(
        """
        INSERT INTO bids (bid_id, bidder_id, item_id, bid_amount, created_at, bid_completion_date, bid_completion_time)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (bid_id, bidder_id, item_id, bid_amount, created_at, bid_completion_date, bid_completion_time)
    )

# Generate and insert fake data for the reviews table
for _ in range(100):  # Create 30 fake reviews
    review_id = uuid.uuid4()
    reviewer_id = fake.random_element(user_ids)
    reviewed_id = fake.random_element(user_ids)
    text = fake.text(max_nb_chars=200)
    rating = fake.random_int(min=1, max=5)
    created_at = fake.date_between(start_date='-2y', end_date='today')
    
    cur.execute(
        """
        INSERT INTO reviews (review_id, reviewer_id, reviewed_id, text, rating, created_at)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (review_id, reviewer_id, reviewed_id, text, rating, created_at)
    )

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()
