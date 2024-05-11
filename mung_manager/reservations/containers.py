from dependency_injector import containers, providers

from mung_manager.pet_kindergardens.selectors.day_offs import DayOffSelector
from mung_manager.pet_kindergardens.selectors.korea_special_days import (
    KoreaSpecialDaySelector,
)
from mung_manager.pet_kindergardens.selectors.pet_kindergardens import (
    PetKindergardenSelector,
)
from mung_manager.reservations.selectors.daily_reservations import (
    DailyReservationSelector,
)


class ReservationContainer(containers.DeclarativeContainer):
    """이 클래스는 DI(Dependency Injection) 예약 컨테이너 입니다.

    Attributes:
        pet_kindergarden_selector: 반려동물 유치원 셀렉터
        daily_reservation_selector: 일일 예약 셀렉터
        day_off_selector: 휴무일 셀렉터
        korea_special_day_selector: 한국 특별일 셀렉터
    """

    pet_kindergarden_selector = providers.Factory(PetKindergardenSelector)
    daily_reservation_selector = providers.Factory(DailyReservationSelector)
    day_off_selector = providers.Factory(DayOffSelector)
    korea_special_day_selector = providers.Factory(KoreaSpecialDaySelector)