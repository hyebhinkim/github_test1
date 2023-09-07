import random
import string


def return_shuffle(str_list):
    random.shuffle(str_list)
    return ''.join(map(str, str_list))


class TextTypeFixture:
    def __init__(self):
        self.korean: str = "ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣ"
        self.english: str = string.ascii_letters + string.ascii_uppercase
        self.number: str = string.digits
        self.special_characters: str = "`-=~!@#$%^&*()_+[]\\{}|;':,./<>?"


    @property
    def random_korean(self):
        return return_shuffle(list(self.korean))

    @property
    def random_english(self):
        return return_shuffle(list(self.english))

    @property
    def random_number(self):
        return return_shuffle(list(self.number))

    @property
    def random_special_characters(self):
        return return_shuffle(list(self.special_characters))


    def generate_random_mixed_string(self, length):
        characters = self.korean + self.english + self.number + self.special_characters
        return ''.join(random.choice(characters) for _ in range(length))

    def generate_random_email(self):
        # 이메일 형식: 임의의 문자열 + '@' + 임의의 문자열 + '.' + com/org/net 등
        domains = ['gmail.', 'naver', 'labelearth']

        # 임의의 문자열 생성
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        domain = random.choice(domains)

        email = f"{username}@{domain}.com"
        return email
