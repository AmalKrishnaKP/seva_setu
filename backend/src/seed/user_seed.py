import uuid
import random
import string
import math
from domain.user.model import User

def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_phone():
    return ''.join(random.choices(string.digits, k=10))

def random_location_within_30km(center_lat, center_lon):
    radius_km = 30.0
    lat_degree = 111.0
    # Calculate km per longitude degree at the given latitude
    lon_degree = 111.0 * math.cos(math.radians(center_lat))
    
    # Random distance and angle for a uniform distribution within the circle
    r = radius_km * math.sqrt(random.random())
    theta = random.random() * 2 * math.pi
    
    delta_lat = (r * math.sin(theta)) / lat_degree
    delta_lon = (r * math.cos(theta)) / lon_degree
    
    return center_lat + delta_lat, center_lon + delta_lon

def generate_user_seed_data():
    users = []
    
    # First 10 users: values up to geolocation + any nullable=False columns
    # nullable=False columns: name, phone, password_hash, is_verified, latitude, longitude, address
    # "up to geolocation" includes: email, geo_location
    for i in range(1, 11):
        # Base location: Kochi, Kerala (10.0246, 76.3075) as an example center point
        lat, lon = random_location_within_30km(10.0246, 76.3075)
        user = User(
            id=uuid.uuid4(),
            name=f"User {i}",
            phone=random_phone(),
            email=f"user{i}@example.com",
            password_hash=random_string(32),
            is_verified=random.choice([True, False]),
            latitude=lat,
            longitude=lon,
            geo_location=f"SRID=4326;POINT({lon} {lat})",
            address=f"{random.randint(100, 999)} Main St, City {i}"
        )
        users.append(user)

    # Next 10 users: values for all columns
    for i in range(11, 21):
        lat, lon = random_location_within_30km(10.0246, 76.3075)
        user = User(
            id=uuid.uuid4(),
            name=f"User {i}",
            phone=random_phone(),
            email=f"user{i}@example.com",
            password_hash=random_string(32),
            is_verified=random.choice([True, False]),
            latitude=lat,
            longitude=lon,
            geo_location=f"SRID=4326;POINT({lon} {lat})",
            address=f"{random.randint(100, 999)} Broad St, City {i}",
            profile_img=f"https://example.com/img{i}.png",
            verification_proof=f"https://example.com/proof{i}.pdf",
            exp_yrs=round(random.uniform(1.0, 15.0), 1),
            salary=round(random.uniform(20000, 120000), 2),
            service_radius=random.randint(5, 50),
            average_rating=round(random.uniform(1.0, 5.0), 1),
            total_rating=random.randint(0, 1000),
            status=random.choice([True, False])
        )
        users.append(user)
    
    return users

def seed_users(session):
    users = generate_user_seed_data()
    session.add_all(users)
    session.commit()
    print(f"Successfully seeded {len(users)} users.")

if __name__ == "__main__":
    from core.session import engine
    from sqlalchemy.orm import sessionmaker
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        seed_users(db)
    finally:
        db.close()
