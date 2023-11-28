DATABASE = [
    {
        "phone_number": "+79...",
        "name": "Юрий",
        "second_name": "Шаманов",
        "balance": 100,
    },
    {
        "phone_number": ...,
        "name": ...,
        "second_name": ...,
        "balance": ...,
    },
    {
        "phone_number": ...,
        "name": ...,
        "second_name": ...,
        "balance": ...,
    },
]


class Contact:
    def get_contact_by_phone_number(self, phone_number: str) -> dict | None:
        for item in DATABASE:
            if item.get("phone_number") == phone_number:
                return item

