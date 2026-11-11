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

## Android 1.0.21 · 무선 펌웨어 1.0.11

Android 1.0.21과 무선 펌웨어 1.0.11을 배포합니다.

**실기 검증 전 시험본입니다.** 빌드와 자동 테스트를 통과했으며, 실제 키보드의 8KiB 전송과 이번 펌웨어의 무선 설치는 아직 확인하지 않았습니다.

- 새 앱과 새 펌웨어에서 한 번에 최대 8KiB(8,192바이트)를 보냅니다. 글자 수가 아닌 UTF-8 바이트 기준입니다.
- 새 앱은 키보드의 지원 용량을 확인합니다. 구형 펌웨어는 기존 한도를 사용합니다.
- 용량을 넘으면 새 앱은 잘라 보내지 않고 안내합니다. 구형 앱의 기존 처리 방식은 바뀌지 않습니다.
- Android·iPhone의 직접 입력, 클립보드와 공유 전송에 적용했습니다. iPhone은 내부 TestFlight로 별도 제공합니다.
- USB 장치·HID 정보는 기존 바이너리와 정적 비교했습니다. 실제 USB 동작 확인은 별도입니다.

먼저 앱을 업데이트한 뒤 앱의 ‘업데이트’에서 무선 시험 펌웨어 1.0.11을 확인하세요. 무선 수신 기능이 이미 설치된 KCZKK10M 키보드가 대상입니다. 순정 키보드에는 바로 무선 설치할 수 없습니다.

배터리 80% 이상에서 Fn+U를 3초간 눌러 승인한 뒤 진행하세요. 설치 중 전원과 모드를 유지하세요. **자동 복원은 지원하지 않습니다.** 실패 시 SET 버튼과 USB 복구가 필요할 수 있습니다.

Windows 앱, 일반 USB 펌웨어 1.0.3과 설치 도구는 기존 파일을 유지했습니다. 무선 시험 파일과 구분해 주세요.

## Android Fn+C

앱에서 ‘Fn+C로 선택한 글 보내기’를 설정하고 접근성 기능을 켭니다.
다른 앱에서 글 선택 → Fn+C → 받는 PC에서 Fn+V 순서로 사용합니다.
선택 영역을 제공하지 않는 앱에서는 해당 앱의 복사·공유 기능을 사용해 주세요.
기능을 끄면 기존 ‘복사 → Fn+C’ 방식으로 동작합니다.

## 업데이트

키보드 메뉴나 앱 설정의 ‘업데이트’에서 앱과 키보드의 새 버전을 함께 확인합니다. 업데이트 화면을 열거나 ‘다시 확인’을 누르면 새 버전을 확인합니다.

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
