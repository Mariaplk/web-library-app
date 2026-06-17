from app import app
from models import db
from models import Role
from models import ReviewStatus


with app.app_context():

    db.create_all()

    if not Role.query.first():

        admin = Role(
            name="Администратор",
            description="Полный доступ"
        )

        moderator = Role(
            name="Модератор",
            description="Модерация рецензий"
        )

        user = Role(
            name="Пользователь",
            description="Создание рецензий"
        )

        db.session.add(admin)
        db.session.add(moderator)
        db.session.add(user)

    if not ReviewStatus.query.first():

        pending = ReviewStatus(
            name="На рассмотрении"
        )

        approved = ReviewStatus(
            name="Одобрена"
        )

        rejected = ReviewStatus(
            name="Отклонена"
        )

        db.session.add(pending)
        db.session.add(approved)
        db.session.add(rejected)

    db.session.commit()

    print("База данных инициализирована")
