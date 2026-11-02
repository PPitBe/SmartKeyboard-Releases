# SmartKeyboard

Keychron K10 Pro SE2 ZMK ANSI용 펌웨어와 앱을 배포합니다. 펌웨어 모델은 `KCZKK10M`입니다.

## 다운로드

| 종류 | 파일 |
| --- | --- |
| Windows | [SkApp.exe](https://github.com/PPitBe/SmartKeyboard-Releases/releases/latest/download/SkApp.exe) |
| Android | [SkApp-android-arm64.apk](https://github.com/PPitBe/SmartKeyboard-Releases/releases/latest/download/SkApp-android-arm64.apk) |
| iPhone | [TestFlight](https://testflight.apple.com/join/XjTpuFMJ) |
| 펌웨어 | [SmartKeyboard-K10Pro-ANSI.bin](https://github.com/PPitBe/SmartKeyboard-Releases/releases/latest/download/SmartKeyboard-K10Pro-ANSI.bin) |

## 설치

- Windows: 실행 파일을 열면 됩니다.
- Android: APK를 내려받아 설치합니다. 기존 앱은 삭제하지 않아도 됩니다.
- iPhone: TestFlight를 이용합니다. 공개 초대 링크 설치는 외부 테스트 승인 전까지 준비 상태입니다.
- 펌웨어: 키보드를 USB로 연결하고 [설치 도구](https://github.com/PPitBe/SmartKeyboard-Releases/releases/latest/download/SmartKeyboard-Installer.exe)를 실행합니다. 설치 중에는 케이블을 분리하지 마세요. 설치 도구에서 순정 펌웨어로 되돌릴 수 있습니다.

## Android 1.0.18

내용을 펼칠 때 회색 빈 영역이 생기던 오류를 수정했습니다.
펼침 상태와 스크롤 위치의 저장 항목을 분리했습니다.
제보된 오류를 자동 테스트에서 재현한 뒤 수정 후 통과를 확인했습니다. 수정본의 단말 확인은 별도입니다.
1.0.16에서 연결 성공을 확인한 기기 선택 수정과 새 UI를 유지합니다.
앱 설정에서 업데이트를 다시 확인하고 설치하세요. 앱 데이터와 페어링은 유지합니다.

## Android Fn+C

앱에서 ‘Fn+C로 선택한 글 보내기’를 설정하고 접근성 기능을 켭니다.
다른 앱에서 글 선택 → Fn+C → 받는 PC에서 Fn+V 순서로 사용합니다.
선택 영역을 제공하지 않는 앱에서는 해당 앱의 복사·공유 기능을 사용해 주세요.
기능을 끄면 기존 ‘복사 → Fn+C’ 방식으로 동작합니다.

## 업데이트

앱 자체 업데이트는 설정에서, 펌웨어 업데이트는 키보드 메뉴에서 확인합니다. 앱을 열 때도 새 버전을 확인합니다.

iPhone 공개 설치 상태는 최신 릴리스 설명에서 확인할 수 있습니다.

일반 펌웨어는 USB 설치 도구를 사용합니다. 무선 업데이트는 지원 펌웨어가 설치된 키보드에서 시험할 수 있습니다. 해당 키보드에 Bluetooth로 연결된 단말의 앱에서 진행합니다. 배터리 80% 이상과 Fn+U 승인이 필요합니다. 순정 펌웨어에는 앱만으로 무선 업데이트 기능을 추가할 수 없습니다.

BLE 버전 조회를 지원하는 펌웨어는 앱에서 설치 버전을 확인할 수 있습니다. 구형 펌웨어는 버전 확인을 지원하지 않을 수 있습니다.

앱 1.0.11부터 완료 후 상세 정보에 확인된 펌웨어와 업데이트 전 펌웨어를 구분해 표시합니다. 전송 당시 MTU·전원은 과거 기록입니다. 상세 내용을 복사하려면 ‘업데이트 정보 복사’를 누릅니다. 이전 앱에서는 ‘오류 정보 복사’로 표시됩니다.

파일별 버전과 SHA-256은 [배포 정보](https://github.com/PPitBe/SmartKeyboard-Releases/releases/latest/download/update.json)에 있습니다. 이전 파일은 [릴리스 목록](https://github.com/PPitBe/SmartKeyboard-Releases/releases)에서 받을 수 있습니다.

## 무선 업데이트 실기 결과

2026-11-02, 같은 키보드에서 344,628바이트 파일로 확인했습니다.

| 항목 | 이전 시험 | 개선 후 시험 |
| --- | --- | --- |
| 펌웨어 교체 | 1.0.6 → 1.0.8 | 1.0.8 → 1.0.9 |
| MTU | 23 | 247 |
| 전체 완료 시간 | 21분 33초 | 2분 |
| 전체 수신·설치 요청 기록 시점 | 21분 17초 | 1분 15초 |

전체 시간은 약 10.8배 빨라졌고 90.7% 줄었습니다. 개선 후 재연결과 설치 버전 1.0.9를 확인했습니다. 전후 각 1회 결과이며 단말과 연결 상태에 따라 시간은 달라집니다. 설치 요청 기록의 경과 시간은 순수 전송 시간과 다릅니다.

이 결과는 전송·설치 후 재연결·버전 확인에 대한 것입니다. 입력·모드 자동 재연결의 추가 확인과 실패 시 자동 복원 검증을 대신하지 않습니다. 무선 시험 펌웨어의 자동 복원은 지원하지 않습니다.
