from dataclasses import dataclass
import datetime
from typing import List

from bookmanagement.types.result import Result, Fail, Success


@dataclass
class UserRentalRecord(object):
    user_id: int
    when: datetime.datetime
    is_expired: bool


class RentalList(object):
    def __init__(self, rental_list_id: int, rental_record_list: List[UserRentalRecord]):
        self.rental_list_id = rental_list_id
        self.records = rental_record_list

    def rental_book(self, user_id: int) -> Result:
        if not self.now_avaliable():
            return Fail("이 책은 다른 사람이 이미 사용중입니다.")
        self.records.append(UserRentalRecord(user_id, datetime.datetime.now(), False))
        return Success("ok")

    def now_avaliable(self) -> bool:
        return not self.records[-1].is_expired
