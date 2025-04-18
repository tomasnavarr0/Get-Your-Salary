from enum import Enum


class CompanySize(str, Enum):
    SIZE_1 = "1 (solamente yo)"
    SIZE_2_10 = "De 2 a 10 personas"
    SIZE_11_50 = "De 11 a 50 personas"
    SIZE_51_100 = "De 51 a 100 personas"
    SIZE_101_200 = "De 101 a 200 personas"
    SIZE_201_500 = "De 201 a 500 personas"
    SIZE_501_1000 = "De 501 a 1000 personas"
    SIZE_1001_2000 = "De 1001 a 2000 personas"
    SIZE_2001_5000 = "De 2001a 5000 personas"
    SIZE_5001_10000 = "De 5001 a 10000 personas"
    SIZE_OVER_10000 = "Más de 10000 personas"
