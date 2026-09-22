from uuid import UUID

from sqlalchemy.orm import Session
from geoalchemy2.elements import WKTElement

from src.domain.user.model import User
from src.domain.user.schema import UserCreate, UserUpdate


class UserRepository:

    @staticmethod
    def get_by_id(db: Session, user_id: UUID) -> User | None:
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_by_phone(db: Session, phone: str) -> User | None:
        return db.query(User).filter(User.phone == phone).first()

    @staticmethod
    def get_by_email(db: Session, email: str) -> User | None:
        if not email:
            return None

        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def create(
        db: Session,
        user_in: UserCreate,
        hashed_password: str
    ) -> User:

        point = WKTElement(
            f"POINT({user_in.longitude} {user_in.latitude})",
            srid=4326
        )

        user = User(
            name=user_in.name,
            phone=user_in.phone,
            email=user_in.email,
            password_hash=hashed_password,
            profile_img=user_in.profile_img,
            address=user_in.address,
            latitude=user_in.latitude,
            longitude=user_in.longitude,
            geo_location=point,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def update(
        db: Session,
        user: User,
        update_data: UserUpdate
    ) -> User:

        update_dict = update_data.model_dump(
            exclude_unset=True
        )

        if "latitude" in update_dict or "longitude" in update_dict:

            lat = update_dict.get(
                "latitude",
                user.latitude
            )

            lng = update_dict.get(
                "longitude",
                user.longitude
            )

            user.geo_location = WKTElement(
                f"POINT({lng} {lat})",
                srid=4326
            )

        for field, value in update_dict.items():
            setattr(user, field, value)

        db.commit()
        db.refresh(user)

        return user
