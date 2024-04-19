from collections import OrderedDict

from django.db import transaction

from mung_manager.common.exception.exceptions import AlreadyExistsException
from mung_manager.common.services import update_model
from mung_manager.users.models import User
from mung_manager.users.selectors.users import UserSelector
from mung_manager.users.services.abstracts import AbstractUserService


class UserService(AbstractUserService):
    """이 클래스는 유저를 데이터베이스에서 PUSH하는 역할을 담당합니다."""

    def __init__(self, user_selector: UserSelector):
        self._user_selector = user_selector

    @transaction.atomic
    def create_social_user(
        self,
        email: str,
        name: str,
        social_id: str,
        phone_number: str,
        birth: object,
        gender: str,
        social_provider: int,
    ) -> User:
        """이 함수는 유저 데이터를 받아 소셜 유저를 생성합니다.

        Args:
            email (str): 이메일
            name (str): 이름
            social_id (str): 소셜 아이디
            phone_number (str): 전화번호
            birth (object): 생년월일
            gender (str): 성별
            social_provider (int): 소셜 제공자

        Returns:
            User: 유저 객체
        """
        user = self._user_selector.get_user_by_social_id(social_id)

        # 전화번호가 변경되었을 경우 업데이트
        if user is not None and user.phone_number != phone_number:
            user.phone_number = phone_number
            user.save(update_fields=["phone_number"])

        if user is None:
            user = User.objects.create_social_user(
                email=email,
                name=name,
                phone_number=phone_number,
                social_id=social_id,
                social_provider=social_provider,
                birth=birth,
                gender=gender,
            )
        return user

    @transaction.atomic
    def update_user(self, user, data: OrderedDict) -> User:
        """이 함수는 유저 데이터를 받아 이메일 중복 확인 후 유저 정보를 수정합니다.

        Args:
            user (User): 유저 객체
            data (dict): 수정할 데이터

        Returns:
            User: 유저 객체
        """
        if self._user_selector.check_is_exists_user_by_email_excluding_self(email=data.get("email"), user=user):
            raise AlreadyExistsException("Email already exists.")

        fields = ["name", "email"]
        user, has_updated = update_model(instance=user, fields=fields, data=data)
        return user
