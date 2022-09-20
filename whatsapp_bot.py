import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
from whatsapp_responses import response

# Mouse click workaround for MAC OS
mouse = Controller()


# Instructions
class WhatsApp:

    def __init__(self, speed=.5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''

    # navigates to the green dots for new msgs
    def nav_green_dot(self):
        try:
            # pega a notificação pelo arquivo e com confiabilidade de 70%, assim ele aceita os numeros dentro
            position = pt.locateOnScreen('green_dot.png', confidence=.8)
            # vai até a posição do green dot
            pt.moveTo(position[0:2], duration=self.speed)
            # move o mouse para a esquerda para entrar na conversa
            pt.moveRel(-100, 0, duration=self.speed)
            # clica na conversa
            pt.doubleClick(interval=self.click_speed)

        except Exception as e:
            print(f'Exception (nav_green_dot): {e}')

    def nav_input_bot(self):
        try:
            # pega a notificação pelo arquivo e com confiabilidade de 70%, assim ele aceita os numeros dentro
            position = pt.locateOnScreen('paperclip.png', confidence=.8)
            # vai até a posição do green dot
            pt.moveTo(position[0:2], duration=self.speed)
            # move o mouse para a esquerda para entrar na conversa
            pt.moveRel(100, 10, duration=self.speed)
            # clica na conversa
            pt.doubleClick(interval=self.click_speed)

        except Exception as e:
            print(f'Exception (nav_input_bot): {e}')

    def nav_message(self):
        try:
            # pega a notificação pelo arquivo e com confiabilidade de 70%, assim ele aceita os numeros dentro
            position = pt.locateOnScreen('paperclip.png', confidence=.8)
            # vai até a posição do green dot
            pt.moveTo(position[0:2], duration=self.speed)
            # move o mouse para a esquerda para entrar na conversa
            pt.moveRel(10, -50, duration=self.speed)


        except Exception as e:
            print(f'Exception (nav_message): {e}')

    def get_message(self):
        try:
            pt.tripleClick()
            mouse.click(Button.left, 3)
            sleep(self.speed)
            mouse.click(Button.right, 1)
            sleep(self.speed)
            pt.moveRel(10, -120, duration=self.speed)
            mouse.click(Button.left, 1)
            sleep(1)

            self.message = pc.paste()
            print(self.message)

        except Exception as e:
            print(f'Exception (get_message): {e}')

    def send_message(self):
        try:
            if self.message != self.last_message:
                bot_response = response(self.message)
                print(f"you say: {bot_response}")
                pt.typewrite(bot_response, interval=.1)
                pt.typewrite('\n')
                self.last_message = self.message
            else:
                print('no new msgs')

        except Exception as e:
            print(f'Exception (send_message): {e}')

    def nav_x(self):
        try:
            position = pt.locateOnScreen('x.png', confidence=.8)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(10, 10, duration=self.speed)
            mouse.click(Button.left, 1)

        except Exception as e:
            print(f'Exception (nav_x): {e}')

wa_bot = WhatsApp(speed=.5, click_speed=.4)

sleep(2)
c = 0

while c < 2:
    wa_bot.nav_green_dot()
    wa_bot.nav_input_bot()
    wa_bot.nav_message()
    wa_bot.get_message()
    wa_bot.send_message()

    sleep(10)
    c += 1
