from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status

from mung_manager.common.base.api_managers import BaseAPIManager
from mung_manager.pet_kindergardens.apis.reservations.apis import (
    ReservationCalendarListAPI,
    ReservationCancelAPI,
    ReservationCustomerPetListAPI,
    ReservationCustomerTicketListAPI,
    ReservationDayOffCreateAPI,
    ReservationDayOffDeleteAPI,
    ReservationListAPI,
    ReservationRegisterAPI,
    ReservationToggleAttendanceAPI,
)
from mung_manager.schemas.errors.authentications import (
    ErrorAuthenticationPasswordChangedSchema,
    ErrorAuthenticationUserDeletedSchema,
    ErrorAuthenticationUserInactiveSchema,
    ErrorAuthenticationUserNotFoundSchema,
    ErrorAuthorizationHeaderSchema,
    ErrorTokenIdentificationSchema,
)
from mung_manager.schemas.errors.commons import (
    ErrorAuthenticationFailedSchema,
    ErrorInvalidParameterFormatSchema,
    ErrorInvalidTokenSchema,
    ErrorNotAuthenticatedSchema,
    ErrorPermissionDeniedSchema,
    ErrorUnknownServerSchema,
)
from mung_manager.schemas.errors.customers import (
    ErrorCustomerNotFoundSchema,
    ErrorCustomerPetOverDailyLimitSchema,
    ErrorCustomerTicketConflictSchema,
    ErrorCustomerTicketExpiredSchema,
    ErrorCustomerTicketInvalidExpiredAtSchema,
    ErrorCustomerTicketNoCountSchema,
    ErrorCustomerTicketNotFoundSchema,
)
from mung_manager.schemas.errors.pet_kindergardens import (
    ErrorPetKindergardenClosedSchema,
    ErrorPetKindergardenInvalidBusinessHourSchema,
    ErrorPetKindergardenNotFoundSchema,
)
from mung_manager.schemas.errors.reservations import (
    ErrorDayOffNotFoundSchema,
    ErrorReservationAlreadyExistsCustomerPetSchema,
    ErrorReservationNotFoundSchema,
    ErrorReservationTimeTicketTypeAllDaySchema,
    ErrorReservationTimeTicketTypeHotelSchema,
    ErrorReservationTimeTicketTypeTimeSchema,
)


class ReservationCalendarListAPIManager(BaseAPIManager):
    VIEWS_BY_METHOD = {
        "GET": ReservationCalendarListAPI.as_view,
    }

    @extend_schema(
        tags=["반려동물 유치원-예약"],
        summary="반려동물 유치원 월간 예약 목록 조회",
        description="""
        Rogic
            - 유저가 반려동물 유치원 월간 예약 목록을 조회합니다.
        """,
        parameters=[VIEWS_BY_METHOD["GET"]().cls.FilterSerializer],
        responses={
            status.HTTP_200_OK: VIEWS_BY_METHOD["GET"]().cls.OutputSerializer,
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorInvalidParameterFormatSchema,
                ],
            ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorAuthenticationFailedSchema,
                    ErrorNotAuthenticatedSchema,
                    ErrorInvalidTokenSchema,
                    ErrorAuthorizationHeaderSchema,
                    ErrorAuthenticationPasswordChangedSchema,
                    ErrorAuthenticationUserDeletedSchema,
                    ErrorAuthenticationUserInactiveSchema,
                    ErrorAuthenticationUserNotFoundSchema,
                    ErrorTokenIdentificationSchema,
                ],
            ),
            status.HTTP_403_FORBIDDEN: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorPermissionDeniedSchema,
                ],
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorPetKindergardenNotFoundSchema,
                ],
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorUnknownServerSchema,
                ],
            ),
        },
    )
    def get(self, request, *args, **kwargs):
        return self.VIEWS_BY_METHOD["GET"]()(request, *args, **kwargs)


class ReservationDayOffListAPIManager(BaseAPIManager):
    VIEWS_BY_METHOD = {
        "POST": ReservationDayOffCreateAPI.as_view,
    }

    @extend_schema(
        tags=["반려동물 유치원-예약"],
        summary="반려동물 유치원 휴무일 생성",
        description="""
        Rogic
            - 유저가 반려동물 유치원 휴무일을 생성합니다.
        """,
        request=VIEWS_BY_METHOD["POST"]().cls.InputSerializer,
        responses={
            status.HTTP_201_CREATED: VIEWS_BY_METHOD["POST"]().cls.OutputSerializer,
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorInvalidParameterFormatSchema,
                ],
            ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorAuthenticationFailedSchema,
                    ErrorNotAuthenticatedSchema,
                    ErrorInvalidTokenSchema,
                    ErrorAuthorizationHeaderSchema,
                    ErrorAuthenticationPasswordChangedSchema,
                    ErrorAuthenticationUserDeletedSchema,
                    ErrorAuthenticationUserInactiveSchema,
                    ErrorAuthenticationUserNotFoundSchema,
                    ErrorTokenIdentificationSchema,
                ],
            ),
            status.HTTP_403_FORBIDDEN: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorPermissionDeniedSchema,
                ],
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorPetKindergardenNotFoundSchema,
                ],
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorUnknownServerSchema,
                ],
            ),
        },
    )
    def post(self, request, *args, **kwargs):
        return self.VIEWS_BY_METHOD["POST"]()(request, *args, **kwargs)


class ReservationDayOffDetailAPIManager(BaseAPIManager):
    VIEWS_BY_METHOD = {
        "DELETE": ReservationDayOffDeleteAPI.as_view,
    }

    @extend_schema(
        tags=["반려동물 유치원-예약"],
        summary="반려동물 유치원 휴무일 삭제",
        description="""
        Rogic
            - 유저가 반려동물 유치원 휴무일을 삭제합니다.
        """,
        responses={
            status.HTTP_204_NO_CONTENT: OpenApiTypes.NONE,
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorInvalidParameterFormatSchema,
                    ErrorDayOffNotFoundSchema,
                ],
            ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorAuthenticationFailedSchema,
                    ErrorNotAuthenticatedSchema,
                    ErrorInvalidTokenSchema,
                    ErrorAuthorizationHeaderSchema,
                    ErrorAuthenticationPasswordChangedSchema,
                    ErrorAuthenticationUserDeletedSchema,
                    ErrorAuthenticationUserInactiveSchema,
                    ErrorAuthenticationUserNotFoundSchema,
                    ErrorTokenIdentificationSchema,
                ],
            ),
            status.HTTP_403_FORBIDDEN: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorPermissionDeniedSchema,
                ],
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorPetKindergardenNotFoundSchema,
                ],
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorUnknownServerSchema,
                ],
            ),
        },
    )
    def delete(self, request, *args, **kwargs):
        return self.VIEWS_BY_METHOD["DELETE"]()(request, *args, **kwargs)


class ReservationListAPIManager(BaseAPIManager):
    VIEWS_BY_METHOD = {
        "GET": ReservationListAPI.as_view,
        "POST": ReservationRegisterAPI.as_view,
    }

    @extend_schema(
        tags=["반려동물 유치원-예약"],
        summary="반려동물 유치원 예약 목록 조회",
        description="""
        Rogic
            - 유저가 반려동물 유치원 예약 목록을 조회합니다.
        """,
        parameters=[VIEWS_BY_METHOD["GET"]().cls.FilterSerializer],
        responses={
            status.HTTP_200_OK: VIEWS_BY_METHOD["GET"]().cls.OutputSerializer,
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorInvalidParameterFormatSchema,
                ],
            ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorAuthenticationFailedSchema,
                    ErrorNotAuthenticatedSchema,
                    ErrorInvalidTokenSchema,
                    ErrorAuthorizationHeaderSchema,
                    ErrorAuthenticationPasswordChangedSchema,
                    ErrorAuthenticationUserDeletedSchema,
                    ErrorAuthenticationUserInactiveSchema,
                    ErrorAuthenticationUserNotFoundSchema,
                    ErrorTokenIdentificationSchema,
                ],
            ),
            status.HTTP_403_FORBIDDEN: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorPermissionDeniedSchema,
                ],
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorPetKindergardenNotFoundSchema,
                ],
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorUnknownServerSchema,
                ],
            ),
        },
    )
    def get(self, request, *args, **kwargs):
        return self.VIEWS_BY_METHOD["GET"]()(request, *args, **kwargs)

    @extend_schema(
        tags=["반려동물 유치원-예약"],
        summary="반려동물 유치원 예약 생성",
        description="""
        Rogic
            - 유저가 반려동물 유치원 예약을 생성합니다.
        """,
        request=VIEWS_BY_METHOD["POST"]().cls.InputSerializer,
        responses={
            status.HTTP_201_CREATED: VIEWS_BY_METHOD["POST"]().cls.OutputSerializer,
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorInvalidParameterFormatSchema,
                    ErrorCustomerPetOverDailyLimitSchema,
                    ErrorPetKindergardenClosedSchema,
                    ErrorReservationAlreadyExistsCustomerPetSchema,
                    ErrorCustomerTicketExpiredSchema,
                    ErrorCustomerTicketInvalidExpiredAtSchema,
                    ErrorReservationTimeTicketTypeAllDaySchema,
                    ErrorReservationTimeTicketTypeHotelSchema,
                    ErrorReservationTimeTicketTypeTimeSchema,
                    ErrorPetKindergardenInvalidBusinessHourSchema,
                    ErrorCustomerTicketNoCountSchema,
                    ErrorCustomerTicketConflictSchema,
                ],
            ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorAuthenticationFailedSchema,
                    ErrorNotAuthenticatedSchema,
                    ErrorInvalidTokenSchema,
                    ErrorAuthorizationHeaderSchema,
                    ErrorAuthenticationPasswordChangedSchema,
                    ErrorAuthenticationUserDeletedSchema,
                    ErrorAuthenticationUserInactiveSchema,
                    ErrorAuthenticationUserNotFoundSchema,
                    ErrorTokenIdentificationSchema,
                ],
            ),
            status.HTTP_403_FORBIDDEN: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorPermissionDeniedSchema,
                ],
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorPetKindergardenNotFoundSchema,
                    ErrorCustomerNotFoundSchema,
                    ErrorCustomerTicketNotFoundSchema,
                ],
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorUnknownServerSchema,
                ],
            ),
        },
    )
    def post(self, request, *args, **kwargs):
        return self.VIEWS_BY_METHOD["POST"]()(request, *args, **kwargs)


class ReservationToggleAttendanceAPIManager(BaseAPIManager):
    VIEWS_BY_METHOD = {
        "PATCH": ReservationToggleAttendanceAPI.as_view,
    }

    @extend_schema(
        tags=["반려동물 유치원-예약"],
        summary="반려동물 유치원 예약 출석 상태 변경",
        description="""
        Rogic
            - 유저가 반려동물 유치원 예약 출석 상태를 변경합니다.
        """,
        responses={
            status.HTTP_200_OK: VIEWS_BY_METHOD["PATCH"]().cls.OutputSerializer,
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorAuthenticationFailedSchema,
                    ErrorNotAuthenticatedSchema,
                    ErrorInvalidTokenSchema,
                    ErrorAuthorizationHeaderSchema,
                    ErrorAuthenticationPasswordChangedSchema,
                    ErrorAuthenticationUserDeletedSchema,
                    ErrorAuthenticationUserInactiveSchema,
                    ErrorAuthenticationUserNotFoundSchema,
                    ErrorTokenIdentificationSchema,
                ],
            ),
            status.HTTP_403_FORBIDDEN: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorPermissionDeniedSchema,
                ],
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorReservationNotFoundSchema,
                ],
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorUnknownServerSchema,
                ],
            ),
        },
    )
    def patch(self, request, *args, **kwargs):
        return self.VIEWS_BY_METHOD["PATCH"]()(request, *args, **kwargs)


class ReservationCustomerPetListAPIManager(BaseAPIManager):
    VIEWS_BY_METHOD = {
        "GET": ReservationCustomerPetListAPI.as_view,
    }

    @extend_schema(
        tags=["반려동물 유치원-예약"],
        summary="반려동물 유치원 예약 고객 반려동물 목록 조회",
        description="""
        Rogic
            - 유저가 반려동물 유치원 예약 고객 반려동물 목록을 조회합니다.
        """,
        parameters=[VIEWS_BY_METHOD["GET"]().cls.FilterSerializer],
        responses={
            status.HTTP_200_OK: VIEWS_BY_METHOD["GET"]().cls.OutputSerializer,
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorInvalidParameterFormatSchema,
                ],
            ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorAuthenticationFailedSchema,
                    ErrorNotAuthenticatedSchema,
                    ErrorInvalidTokenSchema,
                    ErrorAuthorizationHeaderSchema,
                    ErrorAuthenticationPasswordChangedSchema,
                    ErrorAuthenticationUserDeletedSchema,
                    ErrorAuthenticationUserInactiveSchema,
                    ErrorAuthenticationUserNotFoundSchema,
                    ErrorTokenIdentificationSchema,
                ],
            ),
            status.HTTP_403_FORBIDDEN: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorPermissionDeniedSchema,
                ],
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorPetKindergardenNotFoundSchema,
                ],
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorUnknownServerSchema,
                ],
            ),
        },
    )
    def get(self, request, *args, **kwargs):
        return self.VIEWS_BY_METHOD["GET"]()(request, *args, **kwargs)


class ReservationCustomerTicketListAPIManager(BaseAPIManager):
    VIEWS_BY_METHOD = {
        "GET": ReservationCustomerTicketListAPI.as_view,
    }

    @extend_schema(
        tags=["반려동물 유치원-예약"],
        summary="반려동물 유치원 예약 고객 티켓 목록 조회",
        description="""
        Rogic
            - 유저가 반려동물 유치원 예약 고객 티켓 목록을 조회합니다.
        """,
        responses={
            status.HTTP_200_OK: VIEWS_BY_METHOD["GET"]().cls.OutputSerializer,
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorAuthenticationFailedSchema,
                    ErrorNotAuthenticatedSchema,
                    ErrorInvalidTokenSchema,
                    ErrorAuthorizationHeaderSchema,
                    ErrorAuthenticationPasswordChangedSchema,
                    ErrorAuthenticationUserDeletedSchema,
                    ErrorAuthenticationUserInactiveSchema,
                    ErrorAuthenticationUserNotFoundSchema,
                    ErrorTokenIdentificationSchema,
                ],
            ),
            status.HTTP_403_FORBIDDEN: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorPermissionDeniedSchema,
                ],
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorPetKindergardenNotFoundSchema,
                ],
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorUnknownServerSchema,
                ],
            ),
        },
    )
    def get(self, request, *args, **kwargs):
        return self.VIEWS_BY_METHOD["GET"]()(request, *args, **kwargs)


class ReservationDetailAPIManager(BaseAPIManager):
    VIEWS_BY_METHOD = {
        "DELETE": ReservationCancelAPI.as_view,
    }

    @extend_schema(
        tags=["반려동물 유치원-예약"],
        summary="반려동물 유치원 예약 삭제",
        description="""
        Rogic
            - 유저가 반려동물 유치원 예약을 삭제합니다.
        """,
        responses={
            status.HTTP_204_NO_CONTENT: OpenApiTypes.NONE,
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorInvalidParameterFormatSchema,
                    ErrorCustomerTicketConflictSchema,
                ],
            ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorAuthenticationFailedSchema,
                    ErrorNotAuthenticatedSchema,
                    ErrorInvalidTokenSchema,
                    ErrorAuthorizationHeaderSchema,
                    ErrorAuthenticationPasswordChangedSchema,
                    ErrorAuthenticationUserDeletedSchema,
                    ErrorAuthenticationUserInactiveSchema,
                    ErrorAuthenticationUserNotFoundSchema,
                    ErrorTokenIdentificationSchema,
                ],
            ),
            status.HTTP_403_FORBIDDEN: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorPermissionDeniedSchema,
                ],
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorReservationNotFoundSchema,
                    ErrorPetKindergardenNotFoundSchema,
                ],
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                examples=[
                    ErrorUnknownServerSchema,
                ],
            ),
        },
    )
    def delete(self, request, *args, **kwargs):
        return self.VIEWS_BY_METHOD["DELETE"]()(request, *args, **kwargs)
