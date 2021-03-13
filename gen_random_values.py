# gen_random_values.py
import random
import rstr
import datetime

def gen_age():
    return random.randint(18, 120)

def gen_cpf():
    return rstr.rstr('1234567890', 11)

def gen_phone():
    return '({0}) {1}-{2}'.format(
        rstr.rstr('1234567890', 2),
        rstr.rstr('1234567890', 4),
        rstr.rstr('1234567890', 4))

def gen_timestamp():
    year = random.randint(2019, 2020)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(1, 23)
    minute = random.randint(1, 59)
    second = random.randint(1, 59)
    microsecond = random.randint(1, 999999)
    date = datetime.datetime(
        year, month, day, hour, minute, second, microsecond).isoformat(" ")
    return date

def gen_city():
    list_city = [
        [u'Rio Branco', 'AC'],
        [u'Maceió', 'AL'],
        [u'Macapá', 'AP'],
        [u'Manaus', 'AM'],
        [u'Salvador', 'BA'],
        [u'Fortaleza', 'CE'],
        [u'Brasília', 'DF'],
        [u'Vitória', 'ES'],
        [u'Goiânia', 'GO'],
        [u'São Luís', 'MA'],
        [u'Cuiabá', 'MT'],
        [u'Campo Grande', 'MS'],
        [u'Belo Horizonte', 'MG'],
        [u'Belém', 'PA'],
        [u'João Pessoa', 'PB'],
        [u'Curitiba', 'PR'],
        [u'Recife', 'PE'],
        [u'Teresina', 'PI'],
        [u'Rio de Janeiro', 'RJ'],
        [u'Natal', 'RN'],
        [u'Porto Alegre', 'RS'],
        [u'Porto Velho', 'RO'],
        [u'Boa Vista', 'RR'],
        [u'Florianópolis', 'SC'],
        [u'São Paulo', 'SP'],
        [u'Aracaju', 'SE'],
        [u'Palmas', 'TO'],
    return random.choice(list_city)