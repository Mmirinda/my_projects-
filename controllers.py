import views
import models


class ContactsController:
    def get_contact_by_phone_number(self, phone_number: str):
        contact = models.Contact().get_contact_by_phone_number(phone_number)
        views.print_contact(contact)
