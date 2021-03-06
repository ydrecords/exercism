#setup begin
NUMBERS = (
        ('zeroth', 'zero'),
        ('first', 'one'),
        ('second', 'two'),
        ('third', 'three'),
        ('fourth', 'four'),
        ('fifth', 'five'),
        ('sixth', 'six'),
        ('seventh', 'seven'),
        ('eighth', 'eight'),
        ('ninth', 'nine'),
        ('tenth', 'ten'),
        ('eleventh', 'eleven'),
        ('twelfth', 'twelve')
        )
GIFTS = (
        'Nothing at all',
        'Partridge in a Pear Tree',
        'Turtle Doves',
        'French Hens',
        'Calling Birds',
        'Gold Rings',
        'Geese-a-Laying',
        'Swans-a-Swimming',
        'Maids-a-Milking',
        'Ladies Dancing',
        'Lords-a-Leaping',
        'Pipers Piping',
        'Drummers Drumming'
        )

def ordinal(num):
    return NUMBERS[num][0]

def cardinal(num):
    return NUMBERS[num][1]

def verse(verse_num):
    """
    Return the specfied verse of 'The Twelve Days of Christmas'.
    """
    parts = [
            f'{"a" if v == 1 else cardinal(v)} '
            f'{GIFTS[v]}'
            f'{", " if v != 1 else ""}'
            f'{"and " if v == 2 else ""}'
            for v in range(verse_num, 0, -1)
            ]

    return(
            f'On the {ordinal(verse_num)} day of Christmas '
            f'my true love gave to me: {"".join(parts)}.'
            )

#setup end


def recite(start_verse, end_verse):
    """
    Return a list of the specified verses of 'The Twelve Days of Christmas'.
    """
    return [verse(v) for v in range(start_verse, end_verse + 1)]
