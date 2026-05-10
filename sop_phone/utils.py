import phonenumbers

__all__ = (
    'country_code_to_flag',
    'format_number_flag',
    'format_number_error',
    'number_quicksearch',
)

def country_code_to_flag(country:str) -> str:
    '''
    returns the right flag depending on the country code
    https://www.johndcook.com/blog/2022/10/02/flags-unicode/
    '''
    box = lambda ch: chr( ord(ch) + 0x1f1a5 )
    return box(country[0]) + box(country[1])


def format_number_error(number:int) -> str:
    prepare_number:str = f'+{str(number)}'
    parsed_number = phonenumbers.parse(prepare_number)
    return f'{phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}'


def format_number_flag(number:int) -> str:
    '''
    formats E164 numbers
    and displays a beautiful flag
    depending on their country code
    '''
    prepare_number:str = f'+{str(number)}'
    parsed_number = phonenumbers.parse(prepare_number)
    country:str = phonenumbers.region_code_for_country_code(parsed_number.country_code)
    flag = country_code_to_flag(country)
    '''
    returns {flag} <spaces> {number}
    '''
    return f'{flag}\u00A0\u00A0\u00A0{phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}'


def number_quicksearch(first_num: int, last_num: int, lookup_str: str) -> bool:
    '''
    does the lookup string occur in range  first_num to last_num  ?
    Logic is as follows : 
    - first check is the lookup_str appears either in the first or last numbers
    - if not, check if it could appear in the number sequence between first and last numbers 
    '''
    # Basic sanity checks
    if first_num>last_num:
        raise Exception("first_num must be lte last_num")
    if lookup_str is None or not isinstance(lookup_str, str) or len(lookup_str.strip())==0:
        raise Exception("lookup_str must be a non-empty string")
    # Check for simple text match
    if lookup_str in f"{first_num}" or lookup_str in f"{last_num}":
        #print("match str")
        return True
    # Equal start and end numbers but no text match means no match
    if first_num==last_num:
        return False
    # If the difference between start and end is gte than 10 ^(the number of digits in our lookup) we are guaranteed to match
    ls=len(lookup_str)
    incr = 10 ** ls
    if (last_num-first_num+1) >= incr:
        #print(f"match log {first_num=} {last_num=} {incr=} {lookup_str=} {ls=}")
        return True
    # No luck, we need to loop !
    c = int(lookup_str) 
    #rounds=0
    while last_num>=c:
        # take the last N digits to compare with our lookup value 
        lo = first_num % incr
        hi = last_num % incr 
        if lo > hi:
            hi += incr
        if (lo <= c and c <= hi ):
            #print(f"MATCH {rounds=}  {lo=} {c=} {hi=} ") 
            return True
        #print(f"NO match {rounds=}  {lo=} {c=} {hi=} ") 
        # No luck, we'll shift one digit and retry
        first_num=first_num//10
        last_num=last_num//10
        #print(f"AFTER SHIFT {rounds=}  {first_num=} {last_num=} {lookup_str=} ") 
        # Shortcut here to avoid looping on same prefixes
        if first_num == last_num:
            #print(f"NO match shortcut {rounds=}  {first_num=} {last_num=} {lookup_str=} ") 
            return False
        #rounds += 1
    #print(f"NO match {rounds=}  {first_num=} {last_num=} {lookup_str=} ") 
    return False

#number_quicksearch(4926678733150, 4926678734052, "561")
#number_quicksearch(4926678733150, 4926678734052, "333")
#number_quicksearch(4926678733150, 4926678734052, "149")
