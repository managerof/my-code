import qrcode

def get_qrcode(url='https://google.com', name='defult'):
    qr = qrcode.make(data=url)
    qr.sabe(stream=f'{name}.png')
    
    return f'QR code was creaed! Open the {name}.png'

def main():
    print(get_qrcode(url = 'https://youtube.com', name = 'youtube'))
    print(get_qrcode(url = 'https://instagram.com', name = 'instagram'))
    
if __name__ == '__main__':
    main()