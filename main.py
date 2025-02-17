import pygame
import requests
import sys
import os

API_KEY = '8013b162-6b42-4997-9691-77b7074026e0'


def get_map(ll, spn, map_type="map"):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={ll}&spn={spn}&l={map_type}"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    return map_file


def show_map(ll, spn):
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    pygame.display.set_caption("Карта")

    map_file = get_map(ll, spn)

    map_image = pygame.image.load(map_file)
    screen.blit(map_image, (0, 0))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    os.remove(map_file)


if __name__ == "__main__":
    ll = "37.620070,55.753630"
    spn = "0.05,0.05"

    show_map(ll, spn)

