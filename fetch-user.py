import requests
from bs4 import BeautifulSoup

def fetch_html(username='riplols1tos4', region='NA'):
    url = 'https://lolchess.gg/profile/{}/{}/s7/matches/turbo'.format(region, username)

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    html_rounds = soup.find_all('div', {'data-region':region})

    placements = []

    for h_round in html_rounds:
        place = h_round.find('div', {'class':'placement'})
        if len(place) > 0:
            place = int(place.text[1])
            placements.append(place)

    total_score = 0
    for x in placements:
        total_score += x

    return total_score / len(placements)


def main():
    print('Average score:', fetch_html())

if __name__ == '__main__':
    main()