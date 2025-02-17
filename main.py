import pygame
import requests
import sys
import os

API_KEY = '8013b162-6b42-4997-9691-77b7074026e0'

MIN_SPAN = 0.001
MAX_SPAN = 50


def get_map(ll, spn, map_type="map"):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={ll}&spn={spn},{spn}&l={map_type}"
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


def show_map():
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    pygame.display.set_caption("Карта")

    ll = "37.620070,55.753630"
    spn = 0.05

    running = True
    while running:
        map_file = get_map(ll, spn)

        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    spn = max(spn / 2, MIN_SPAN)
                elif event.key == pygame.K_s:
                    spn = min(spn * 2, MAX_SPAN)

        os.remove(map_file)

    pygame.quit()


if __name__ == "__main__":
    show_map()