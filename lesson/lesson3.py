# Nikita.kg
# Twilio.com

# Наследование - Инкапсуляция - Полиморфизм - Абстракция

from abc import ABC, abstractmethod

import random



class OTPService(ABC):
    
    @abstractmethod
    def sms_send():
        pass
    
    
class NikitaOTP(OTPService):
    
    def sms_send(self, phone):
        phone = input("Введите номер телефона в формате +996xxx xxx xxx")
        

class TwilioOTP(OTPService):
    
    def sms_send(self, phone):
        phone = input("Введите номер телефона в формате +7xxx xxx xxx")



class Animal(ABC):
    
    
    # Декоратор @abstractmethod
    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    
    def make_sound(self):
        return print('Gaf gaf')

    def move(self):
        return print('run')

#dog = Dog()
#dog.make_sound()






