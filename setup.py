import os


restricted_packages = [
    'lame',
    'unrar',
    'gstreamer1.0-fluendo-mp3',
    'gstreamer1.0-plugins-bad',
    'gstreamer1.0-plugins-ugly',
    'gstreamer1.0-libav',
    'gstreamer1.0-fluendo-mp3',
    'libdvdread4',
    'libk3b6-extracodecs',
    'oxideqt-codecs-extra',
    'libavcodec-extra',
    'libavcodec-ffmpeg-extra56',
]

extra_packages = [
    'chromium-browser',
    'gimp',
    'python3-pip',
    'inkscape',
    'vlc',
]

remove_packages = [
    'aisleriot',
    'gnome-mahjongg',
    'gnome-mines',
    'gnome-sudoku',
    'vino',
    'remmina',
]

ppa = [
    'ppa:numix/ppa',
]


def packages(items, action=''):
    """ add, remove, install packages"""
    item = ' '.join(items)

    if action == 'install':
        if len(items) > 0:
            os.system('sudo apt install {}'.format(item))
    elif action == 'remove':
        if len(items) > 0:
            os.system('sudo apt purge {}'.format(item))
    elif action == 'ppa':
        if len(items) > 0:
            for l in items:
                os.system('sudo add-apt-repository {}'.format(l))
            os.system('sudo apt update')
    else:
        print('\n[!]Invalid Action..\n')


def main():
    packages(ppa, action='ppa')
    packages(restricted_packages, action='install')
    packages(extra_packages, action='install')
    packages(remove_packages, action='remove')


if __name__ == '__main__':
    main()
