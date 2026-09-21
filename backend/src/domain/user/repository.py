from sqlalchemy import select, func
from geoalchemy2 import Geography

from domain.user.model import User

class userRepo():
    def __init__(self,db):
        self.db=db
    def user_in_10km(self,lati,long):
        target_point = func.ST_SetSRID(
            func.ST_MakePoint(
                long,
                lati
            ),
            4326
        ).cast(Geography)

        stmt = (
            select(User)
            .where(
                func.ST_DWithin(
                    User.geo_location,
                    target_point,
                    10_000
                )
            )
        )

        result = self.db.execute(stmt).scalars().all()
        print(result)
        return result