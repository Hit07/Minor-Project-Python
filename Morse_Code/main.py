import requests

from morse import Morse_Code

# string = ' '.join(str(input())).split(' ')
# translated_string = [Morse_Code.get(_) for _ in string]
# translated_string = ''.join(translated_string)


strings = input()
params = {
    'text': strings
}
r = requests.get('http://api.funtranslations.com/translate/morse', params=params)
r.raise_for_status()


if __name__ == '__main__':
    # print(translated_string)
    data = r.json()['contents']
    print(f'Entered String:{data["text"]}\nTranslated String:{data["translated"]}')

