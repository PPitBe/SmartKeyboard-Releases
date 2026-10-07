"""iPhone 배포 정보가 바뀌면 새 릴리스를 만든다."""
import datetime
import hashlib
import json
import re
import subprocess
from pathlib import Path

REPO = 'PPitBe/SmartKeyboard-Releases'
NAMES = ['SkApp.exe', 'SkApp-android-arm64.apk', 'SmartKeyboard-K10Pro-ANSI.bin',
         'SmartKeyboard-Installer.exe', 'SmartKeyboard-iOS.url', 'update.json']


def gh(*args):
    return subprocess.check_output(['gh', *args], text=True)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ios = json.loads(Path('ios.json').read_text())
    if not re.fullmatch(r'\d+\.\d+\.\d+', ios['version']) or not isinstance(ios['build'], int):
        raise ValueError('잘못된 버전입니다')
    if ios['url'] != 'https://testflight.apple.com/join/XjTpuFMJ' or not isinstance(ios.get('available'), bool):
        raise ValueError('잘못된 배포 정보입니다')
    latest = json.loads(gh('api', f'repos/{REPO}/releases/latest'))
    assets = {a['name']: a for a in latest['assets']}
    stage = Path('release-files')
    stage.mkdir()
    for name in NAMES:
        gh('release', 'download', latest['tag_name'], '--repo', REPO, '--pattern', name, '--dir', str(stage))
        if 'sha256:' + digest(stage / name) != assets[name]['digest']:
            raise ValueError('파일 해시가 다릅니다: ' + name)
    manifest = json.loads((stage / 'update.json').read_text())
    previous = manifest['components'].get('ios')
    if previous == ios:
        print('변경 없음')
        return
    def version(item):
        return tuple(map(int, item['version'].split('.'))) + (item['build'],)
    if previous and version(ios) < version(previous):
        print('이전 버전은 게시하지 않습니다')
        return
    today = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime('v%Y.%m.%d')
    releases = json.loads(gh('release', 'list', '--repo', REPO, '--limit', '100', '--json', 'tagName'))
    existing = {r['tagName'] for r in releases}
    tag = today
    number = 2
    while tag in existing:
        tag = f'{today}-{number}'
        number += 1
    manifest['release'] = tag
    manifest['components']['ios'] = ios
    for entry in manifest['components'].values():
        if 'sha256' in entry:
            name = entry['url'].rsplit('/', 1)[-1]
            if name not in NAMES or digest(stage / name) != entry['sha256']:
                raise ValueError('배포 정보가 파일과 다릅니다')
            entry['url'] = f'https://github.com/{REPO}/releases/download/{tag}/{name}'
    (stage / 'update.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    (stage / 'SmartKeyboard-iOS.url').write_bytes(f"[InternetShortcut]\r\nURL={ios['url']}\r\n".encode())
    (stage / 'SHA256SUMS.txt').write_text(''.join(f'{digest(p)}  {p.name}\n' for p in sorted(stage.iterdir())))
    status = f"iPhone 앱 {ios['version']} ({ios['build']})을 TestFlight에서 설치할 수 있습니다." if ios['available'] else 'iPhone 공개 테스트를 준비 중입니다.'
    Path('release-notes.md').write_text(status + '\n\nWindows·Android 앱과 펌웨어는 이전 배포와 같습니다.\n')
    gh('release', 'create', tag, '--repo', REPO, '--title', f'SmartKeyboard {tag[1:]}',
       '--notes-file', 'release-notes.md', '--latest', *map(str, stage.iterdir()))


if __name__ == '__main__':
    main()
