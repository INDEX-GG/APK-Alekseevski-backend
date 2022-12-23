from django.core.exceptions import ValidationError


def validate_size_file(file_obj):
    """
    File size check
    """

    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Размер файла не должен превышать { megabyte_limit }MB")
