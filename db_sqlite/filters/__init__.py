from loader import dp
from .Is_admin import IsAdmin
from .is_user import IsUser

if __name__ == "__filters__":
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsUser)