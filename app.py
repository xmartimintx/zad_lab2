import re
from datetime import datetime

def is_valid_phone_number(phone):
    """Sprawdza, czy numer telefonu jest poprawny (np. +48123456789)."""
    return bool(re.fullmatch(r'\+\d{11}', phone))

def calculate_triangle_area(base, height):
    """Zwraca pole trójkąta na podstawie podstawy i wysokości."""
    if base <= 0 or height <= 0:
        raise ValueError("Wymiary muszą być dodatnie.")
    return 0.5 * base * height

def filter_positive_numbers(numbers):
    """Zwraca listę tylko dodatnich liczb z wejściowej listy."""
    return [n for n in numbers if isinstance(n, (int, float)) and n > 0]

def convert_date_to_iso(date_str):
    """Konwertuje datę z formatu DD-MM-YYYY na ISO (YYYY-MM-DD)."""
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        return date_obj.date().isoformat()
    except ValueError:
        raise ValueError("Nieprawidłowy format daty.")

def count_vowels(text):
    """Zwraca liczbę samogłosek w podanym tekście."""
    return sum(1 for char in text.lower() if char in "aeiouyąę")