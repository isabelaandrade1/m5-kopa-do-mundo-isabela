from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
import datetime

def data_processing(data):
    # Verificar se o número de títulos é negativo
    if data.get("titles", 0) < 0:
        raise NegativeTitlesError()
    
    # Verificar se o ano da primeira participação é válido
    first_cup = data.get("first_cup", "")
    try:
        year = int(first_cup.split("-")[0])
    except (ValueError, IndexError):
        raise InvalidYearCupError()
    
    if year < 1930 or (year - 1930) % 4 != 0:
        raise InvalidYearCupError()
    
    # Verificar se o número de títulos é possível
    current_year = datetime.datetime.now().year
    cups_disputed = (current_year - year) // 4 + 1

    if data.get("titles", 0) > cups_disputed:
        raise ImpossibleTitlesError()

    return "Data processed successfully"
