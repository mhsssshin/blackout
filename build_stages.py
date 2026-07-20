import os
import json

stages = [
    {
        "stage": 1,
        "title": "System Boot (F12)",
        "filename": "a7f93b2c.html",
        "verify_hash": "3068430da9e4b7a674184035643d9e19af3dc7483e31cc03b35f75268401df77",
        "speaker": "시스템 인가 모듈",
        "role": "SYSTEM LOBBY",
        "avatar": "SYS",
        "dialogue": "TQO 터미널 단말기 부팅이 완료되었습니다.\n\n시스템 분석 모드로 진입하기 위해서는 박용철 파트장의 인가 코드가 필요합니다.\n본 화면에는 노출된 단서가 없습니다.\n\n시스템 구조의 원천 설계 코드(HTML 소스) 내부를 분석해 보십시오.\n그곳에 개발자가 적어둔 마스터 비밀 번호(KEY) 3자리 숫자가 기록되어 있을 것입니다.",
        "gimmick_html": "<!-- KEY: 179 -->\n<div class='puzzle-container'>\n    <div class='puzzle-title'>🔒 ACCESS PROTECTION KEY</div>\n    <p style='color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;'>\n        인가 토큰이 보안 커널에 의해 물리 차단되었습니다.<br>\n        F12(개발자 도구)를 통해 HTML 소스코드의 주석을 분석하고 백업 마스터 키를 찾아 터미널에 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 2,
        "title": "Encrypted Packet (Base64)",
        "filename": "b4bcdd0d.html",
        "verify_hash": "f5334f59cc820a5c99fd2a5b5527884c821c19f1daa7c825368603aba61d6178",
        "speaker": "네트워크 패킷 스니퍼",
        "role": "PACKET MONITOR",
        "avatar": "NET",
        "dialogue": "권남훈 파트장의 보안 단말기(VDI)로 전송된 내부 사설 포트 전송 패킷이 캡처되었습니다.\n\n이 데이터는 문자나 숫자를 안전하게 전송하기 위해 64진법 텍스트로 인코딩되어 있습니다.\n인터넷의 Base64 디코더 등을 활용해 이 값을 원래대로 풀어내면,\n비밀 사설 포트 번호 4자리가 나옵니다.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>📡 PACKET PAYLOAD DUMP</div>\n    <p style='font-family: var(--font-mono); color: var(--accent-magenta); font-size: 1.2rem; text-align: center; padding: 15px; background: rgba(0,0,0,0.5); border-radius: 4px; letter-spacing: 1px;'>UG9ydCAyMzIx</p>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.5;'>\n        힌트: Base64 형식으로 변환된 포트 정보 페이로드입니다.<br>\n        디코딩 시 문자 뒤에 기재된 숫자 4자리를 찾아 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 3,
        "title": "Log Flood (권한 검색)",
        "filename": "83e5e934.html",
        "verify_hash": "4099ed5ba70aebc5a9dc26bc2093d4b45839f99b306bd12f68cedfd351e6ab7a",
        "speaker": "스토리지 커널 감사 로그",
        "role": "AUDITOR",
        "avatar": "AUD",
        "dialogue": "권남훈 파트장은 모든 백업 파일들이 규정에 맞춰 정상 권한(rwxr-xr-x)을 가지고 있다고 주장했습니다.\n\n그러나 스캔 감사 결과, 단 하나의 백업 파일이 권한 관리 부주의로 인해 취약한 설정(rwxr-xr--)으로 배포된 것이 확인되었습니다.\n\n마우스 스크롤을 이용해 수많은 파일 리스트 중에서 이 잘못 설정된 파일을 찾아내십시오.\n그 후 아래 규칙에 따라 3자리 8진수 숫자로 변환하여 입력해 주십시오.\n\n[권한 변환 규칙]\nr = 4, w = 2, x = 1, - = 0\n각 문자군(rwx / xr- / xr-)의 숫자를 합산하여 3자리 숫자로 만듭니다.\n예시: rwxr-xr-x = (4+2+1)(4+0+1)(4+0+1) = 755",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>📂 DIRECTORY PERMISSIONS SCAN</div>\n    <div class='log-flood-area'>\n" + "\n".join([f"        <div class='log-flood-line'>-rwxr-xr-x  1 tqo_ops  staff  4096 Jul 21 02:00 file_{i:03d}.bin</div>" if i != 273 else "        <div class='log-flood-line log-target'>-rwxr-xr--  1 tqo_ops  staff  8204 Jul 21 01:45 backup_corrupt.bin</div>" for i in range(500)]) + "\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.5;'>\n        힌트: 수백 줄의 리스트 속에서 무언가 다른 파일 하나가 숨어 있습니다.<br>\n        찾아낸 취약 마스크(rwxr-xr--) 값을 위의 변환식에 대입하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 4,
        "title": "The Blackout (Hidden Text)",
        "filename": "13b3bfc6.html",
        "verify_hash": "7970f1f08c678259aa519bb1beaa3e57186a40b0c3fbfc572d37f874125d38fe",
        "speaker": "시스템 긴급 백업 단말",
        "role": "EMERGENCY CONSOLE",
        "avatar": "CRT",
        "dialogue": "서버가 완전한 블랙아웃 상태에 빠져 화면 신호가 끊겼습니다! 눈으로는 터미널의 어떤 글자도 읽을 수 없습니다.\n\n하지만 TQO 긴급 복구 매뉴얼에 따라 단말기 중앙 캔버스 영역에 투명한(검은색) 글씨로 복구 비밀코드가 적혀 있습니다.\n\n마우스 드래그(또는 전체 선택 Ctrl+A)를 사용해 검은색 배경 뒤에 숨겨진 텍스트를 반전시켜 에러 코드를 확인하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>💡 VISIBILITY RESTORATION OVERLAY</div>\n    <div class='hidden-text-container'>\n        <span class='hidden-error-text'>404500</span>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px;'>\n        드래그하여 숨겨진 에러 코드를 찾아 터미널에 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 5,
        "title": "Zalgo Text (글자 깨짐)",
        "filename": "48b42551.html",
        "verify_hash": "af4883c99558a3f6ef589d7e9a69585135ebac48f6b55c12e5e96849dc3707ee",
        "speaker": "오류 콘솔 리포트",
        "role": "LOG ANALYZER",
        "avatar": "ERR",
        "dialogue": "시스템 강제 중단 여파로 로그 덤프 텍스트에 심각한 노이즈가 발생했습니다.\n\n하지만 눈을 가늘고 뜨고 자세히 살펴보면, 깨진 문자들 틈바구니 속에 영문 대문자 B, A, D가 순서대로 숨어 있습니다.\n\n이 글자들을 아스키(ASCII) 10진수 코드로 각각 치환하여 공백 없이 합쳐 입력하십시오.\n\n[아스키 코드 정보]\n- B = 66\n- A = 65\n- D = 68",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⚠️ CORRUPTED STRING BUFFER</div>\n    <div class='zalgo-box'>\n        S̶y̶s̶t̶e̶m̶ <b>B̷</b>u̷f̷f̷e̷r̷ <b>A̵</b>n̷o̷m̷a̷l̷y̷ <b>D̵</b>e̷t̷e̷c̷t̷e̷d̷\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.5;'>\n        힌트: 본문에서 찾아낸 세 개의 문자 B, A, D의 아스키 10진수 숫자를 순서대로 이어 붙인 6자리 보안 코드가 답입니다.\n    </p>\n</div>"
    },
    {
        "stage": 6,
        "title": "Caesar Cipher (시저 암호)",
        "filename": "db590ac0.html",
        "verify_hash": "08434ba9cdf55a02284e2913400586cd289878e0f055f7bb0b07ce392caeb989",
        "speaker": "커널 보안 세션",
        "role": "SECURITY ENGIN",
        "avatar": "SEC",
        "dialogue": "서버를 다운시킨 침입자의 명령어가 세션 암호 로그에 복착되었습니다.\n침입자는 각 글자를 알파벳 순서상 뒤로 3칸씩 밀어 적는 간단한 암호(시저 암호)를 적용해 두었습니다.\n\n[복구 힌트: -3 Shift]\n암호문: vkXwgrzq\n\n모든 문자를 알파벳 순서상 앞으로 3칸씩 당겨 복구하십시오.\n(예: d -> a, k -> h, X -> u ...)\n최종 도출되는 영어 소문자 명령어를 입력하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔐 DECRYPTION KEY: -3 Shift (Caesar)</div>\n    <div style='background: rgba(0,0,0,0.5); padding: 15px; border-radius: 6px; border: 1px solid var(--border-color); font-family: var(--font-mono); text-align: center;'>\n        <p style='color: var(--accent-magenta); font-size: 1.2rem; letter-spacing: 2px;'>vkXwgrzq</p>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.5;'>\n        알파벳 순서: a b c d e f g h i j k l m n o p q r s t u v w x y z<br>\n        예를 들어, 'v'에서 앞으로 3칸 이동하면 's'가 됩니다.\n    </p>\n</div>"
    },
    {
        "stage": 7,
        "title": "SLA Metric (SLA 다운타임 계산)",
        "filename": "4ae9c668.html",
        "verify_hash": "2841dad7e57a80b5a9fdc7cd5799e7108f394e1c6157a8feb8e83db0808d3432",
        "speaker": "박용철 파트장",
        "role": "품질총괄",
        "avatar": "PARK_YC",
        "dialogue": "이보게 TQO! 우리가 이번 차세대 금융 코어 계약에서 약속한 연간 가동률(SLA)이 99.9%일세.\n1년 365일 중 시스템이 멈춰 있을 수 있는 시간(장애 시간)은 단 0.1% 미만이어야 해.\n\n그렇다면 연간 가동률 99.9%를 유지하기 위해 허용되는 연간 최대 장애 정지 시간은 총 몇 '분(Minute)'인가?\n\n계산 오차 방지를 위해 공식으로 나온 약식 기준값(525분)에 우리 부서 내부 통제 계수인 '10'을 곱한 최종 통제 코드를 터미널에 입력하여 내게 보고해 주게!",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>📊 SLA METRIC SHEET</div>\n    <ul style='list-style-type: square; padding-left: 20px; font-size: 0.85rem; line-height: 1.6; color: var(--text-primary);'>\n        <li>연간 기준 시간: 365일 = 8,760시간 = 525,600분</li>\n        <li>보증 허용 정지 범위: 0.1%</li>\n        <li>수치식: 525,600분 * 0.001 = 525.6분</li>\n        <li><strong style='color: var(--accent-magenta);'>입력 요구 조건: 약식 정수 기준값(525분) * 통제 계수(10)</strong></li>\n    </ul>\n</div>"
    },
    {
        "stage": 8,
        "title": "Governance (IT 거버넌스 규정)",
        "filename": "e3ad4d0a.html",
        "verify_hash": "0b483f69c9eaed1e8f96259917fd826bc27d8cc20f8a5715880fb0b8a011def2",
        "speaker": "권남훈 파트장",
        "role": "운영총괄",
        "avatar": "KWON_NH",
        "dialogue": "장애가 발생했을 때 단순 땜질 조치를 넘어서야 합니다.\n\nIT 거버넌스 표준에 따라, 단기 장애 현상(Incident)을 넘어 근본적인 시스템 원인(Problem)을 도출하여 통제하고 품질 지식을 체계적으로 관리하는 글로벌 IT 서비스 관리 모범 기준 프레임워크가 존재합니다.\n\n이 글로벌 표준 프레임워크의 명칭(영문 소문자 4글자 약어)을 입력하여 프로세스 숙지 여부를 인증하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>📚 IT SERVICE GOVERNANCE FRAMEWORK</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;'>\n        힌트: 정보 기술 인프라 라이브러리(IT Infrastructure Library)의 영문 앞글자들을 딴 4글자 약어로, 전 세계 IT 부서의 표준 운영 가이드라인입니다.\n    </p>\n</div>"
    },
    {
        "stage": 9,
        "title": "Knowledgebase (지식 정보 조회)",
        "filename": "cee89b5e.html",
        "verify_hash": "27dce682e1ad2f2106be21d27e8025de5de7ee65cecc737d4f27a33af4c29a8a",
        "speaker": "HIS 지식관리 시스템",
        "role": "KNOWLEDGEBASE",
        "avatar": "KB",
        "dialogue": "장애 대응 가이드라인 조회를 위한 사내 지식 정보 포털입니다.\n\n현재 데이터베이스 서버의 일부 데이터가 파손된 정황이 발견되었습니다.\n아래의 문서 목록에서 '스토리지 동기화 실패로 인한 DB 파손 대응 매뉴얼'에 해당하는 문서 코드의 숫자 4자리를 찾아 입력하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔍 KNOWLEDGEBASE DOCUMENT LIST</div>\n    <table style='width: 100%; border-collapse: collapse; font-size: 0.85rem; text-align: left; margin-top: 10px; color: var(--text-primary);'>\n        <tr style='border-bottom: 1px solid var(--border-color); color: var(--accent-blue);'>\n            <th style='padding: 6px;'>문서코드</th>\n            <th style='padding: 6px;'>주제</th>\n        </tr>\n        <tr>\n            <td style='padding: 6px;'>KB-7108</td>\n            <td style='padding: 6px;'>웹 애플리케이션 서버 커널 튜닝 규격</td>\n        </tr>\n        <tr>\n            <td style='padding: 6px;'>KB-8204</td>\n            <td style='padding: 6px;'>스토리지 동기화 실패로 인한 DB 파손 대응 매뉴얼</td>\n        </tr>\n        <tr>\n            <td style='padding: 6px;'>KB-9321</td>\n            <td style='padding: 6px;'>L4 네트워크 로드밸런서 VIP 이중화 스키마</td>\n        </tr>\n    </table>\n</div>"
    },
    {
        "stage": 10,
        "title": "The Cronjob (Crontab 스케줄링)",
        "filename": "524cfb66.html",
        "verify_hash": "318fb6b0fd6eb7ef86613797123429db40159a50c0b443197c3a229ecefc07fb",
        "speaker": "박재욱 차장",
        "role": "DBA",
        "avatar": "PARK_JW",
        "dialogue": "억울합니다 TQO님! 저는 그날 새벽에 데이터베이스 백업을 수동으로 임의 기동하지 않았습니다.\n\n모든 백업은 시스템에 사전에 자동 예약된 스케줄(Crontab)에 의해서만 돌아갔습니다.\n아래 서버의 백업 스케줄 크론 설정을 분석해 보십시오.\n\n이 백업 스크립트가 매일 자동으로 도는 구동 시각을 24시간 형식의 4자리 숫자(HHMM)로 변환해 입력해 주십시오.\n(예: 오전 8시 5분 -> 0805)",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⏰ TARGET CRONTAB CONFIGURATION</div>\n    <div style='background: #020306; font-family: var(--font-mono); padding: 15px; border-radius: 6px; border: 1px solid var(--border-color); text-align: center; font-size: 1.1rem; color: var(--accent-blue);'>\n        45 1 * * * /usr/sbin/backup.sh\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.5;'>\n        힌트: 크론탭 시간 설정 구조는 [분] [시] [일] [월] [요일] 순서입니다.\n        위 설정은 매일 '1시 45분'에 구동됨을 의미합니다. 포맷에 맞춰 4자리 숫자로 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 11,
        "title": "The Command (박주암 과장)",
        "filename": "e3307ab7.html",
        "verify_hash": "53c148b793bd0c621b03b40afe93b7c39bce8b4d00157bc10142b8a848af32ac",
        "speaker": "박주암 과장",
        "role": "WAS 담당",
        "avatar": "PARK_JA",
        "dialogue": "새벽에 서버가 셧다운되는 당시에 누군가 제 WAS 콘솔 권한을 악용해 로컬 DB에 수동 인증 조작을 시도한 흔적이 로그에 남아 있었습니다.\n\n침입자는 오라클 데이터베이스에 직접 명령어를 날리기 위해 전용 데이터베이스 쿼리 접속 CLI 유틸리티를 실행하려 했습니다.\n\n서버 로그 히스토리에 기록된 이 오라클 질의용 다이렉트 접속 명령어의 정확한 영어 소문자 스펠링을 기입해 주십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>💻 INCIDENT COMMAND HISTORY DUMP</div>\n    <p style='font-family: var(--font-mono); color: var(--text-primary); font-size: 0.95rem; line-height: 1.6;'>\n        $ cd /u01/app/oracle/product/12.1.0/dbhome_1/bin<br>\n        $ ./sqlplus / as sysdba<br>\n        &gt; SHUTDOWN IMMEDIATE;<br>\n        <span style='color: var(--accent-red);'>[02:13:21] DISCONNECTED FROM DATABASE.</span>\n    </p>\n</div>"
    },
    {
        "stage": 12,
        "title": "The Network Lie (김진혁 차장)",
        "filename": "16417f5b.html",
        "verify_hash": "debdc6fdb6c19c94ff78b653767bfac108d84ed51a54a58a72866dc635b15729",
        "speaker": "김진혁 차장",
        "role": "네트워크 담당",
        "avatar": "KIM_JH",
        "dialogue": "저는 결백합니다 TQO님!\n장애 당시 기계실 외부 휴게실 소파에서 노트북을 사용해 T5004 공유기의 무선 신호를 안정적으로 송수신하며 서버들을 원격으로 정상 모니터링하고 있었습니다!\n\n제 단말기에는 무선 접속 안테나가 원활하게 표시되어 있었습니다.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🌐 T5004 ROUTER HARDWARE SPECIFICATION</div>\n    <div class='ascii-diagram'>\n+------------------------------------------------+\n|  T5004 INTERNET RACK HUB                      |\n|                                                |\n|  [LAN1]   [LAN2]   [LAN3]   [LAN4]   [WAN]     |\n|  [ [O] ]  [ [O] ]  [ [X] ]  [ [X] ]  [ [O] ]   |\n|   |  |     |  |                         |  |   |\n|    유선     유선                         인터넷  |\n|                                                |\n|  * WARNING: NO WIRELESS ANTENNA MODULE *       |\n|  * ONLY WIRED ETHERNET CONNECTION SUPPORTED *  |\n+------------------------------------------------+\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.6;'>\n        김진혁 차장의 주장: '공유기의 무선 전파 안테나 신호를 잡아 노트북으로 모니터링했다.'<br>\n        장비 매뉴얼: 무선 모듈 없음, 오직 유선 포트만 존재.<br>\n        김 차장이 접속 기술이라고 주장한 이 거짓말 속의 무선 인터넷 명칭(영문 소문자 4자)을 기입하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 13,
        "title": "The Server Lie (이재헌 과장)",
        "filename": "94e06050.html",
        "verify_hash": "692e4e5decffcf5eac86471ba27ac56a861268d060e4a53a0c768617f4d3a56f",
        "speaker": "이재헌 과장",
        "role": "서버 담당",
        "avatar": "LEE_JH",
        "dialogue": "서버 자원은 풍부하게 할당해 두어 넉넉한 튜닝 상태였습니다.\n물리적 스펙 부족으로 중단되었을 리는 절대 없습니다. 충분히 여유가 있었을 텐데요?",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⚙️ VM INSTANCE SPECIFICATION OVERVIEW</div>\n    <div class='cpu-widget'>\n        <div>INSTANCE_NAME: Core-WAS-01</div>\n        <div class='cpu-bar'>CPU USAGE: [██████████] 99.6% (Overload)</div>\n        <div style='color: var(--accent-magenta); margin-top: 5px;'>AVAILABLE_MARGIN: 0.4%</div>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.6;'>\n        CPU 여유 마진이 0.4%밖에 되지 않는 위태로운 상태입니다.<br>\n        서버 튜닝이 충분히 넉넉한 상태가 아니라, 자원이 고갈 직전이어서 물리 장비의 숨통만 겨우 붙여놓은 한계 튜닝 상태를 의미하는 IT 영단어(영문 소문자 7자)를 기입하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 14,
        "title": "The Motivation (박용철 총괄)",
        "filename": "c70ec350.html",
        "verify_hash": "838940b6f1deea2e9aca2c69a4df9a484139e1d8ab954a1b2366df3777ae416b",
        "speaker": "박용철 파트장",
        "role": "품질총괄",
        "avatar": "PARK_YC",
        "dialogue": "서버가 멈추기 직전에 데이터베이스에 심각한 블록 손상 오류가 감지되었네.\n\n오라클 데이터베이스의 물리적 파일 파손을 일으키는 고유한 장애 에러 패턴을 정규표현식(Regex) 필터로 검출해 내려 하네.\n아래 필터에 일치하는 로그 에러 코드 명칭을 찾아 영어 소문자로 기입해 주게.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔍 CORRUPTION PATTERN DETECTION FILTER</div>\n    <ul style='list-style-type: square; padding-left: 20px; font-size: 0.85rem; line-height: 1.6; color: var(--accent-blue); font-family: var(--font-mono);'>\n        <li>정규식 필터 패턴: ^[A-Za-z]+-[0-9]{5}$ (영문 단어 + 붙임표 + 정확히 5자리 숫자)</li>\n        <li>[DB ERROR LOG DUMP]:</li>\n        <li style='color: var(--text-muted);'>- sys-info-10023</li>\n        <li style='color: var(--text-primary); font-weight: bold;'>- ORA-00600 (internal error)</li>\n        <li style='color: var(--text-muted);'>- DB-CONN-5020</li>\n    </ul>\n</div>"
    },
    {
        "stage": 15,
        "title": "The VDI Rule (권남훈 총괄)",
        "filename": "aac380d4.html",
        "verify_hash": "6f89bddf8582a8d223e132d10c9436e788687f159fbbf5ac36a6eb14d307a3fa",
        "speaker": "권남훈 파트장",
        "role": "운영총괄",
        "avatar": "KWON_NH",
        "dialogue": "인프라 보안 규정상 세션이 종료되면 할당된 사설 IP는 즉시 반납 처리됩니다.\n\n이후 새로 세션을 맺는 타인에게 해당 IP 주소가 동적으로 자동 재분배되도록 관리해 주는 표준 네트워크 규약이 존재합니다.\n철자가 뒤섞여 있는 프로토콜 문자 'H C P D'의 순서를 바르게 나열해 표준 약어(소문자 4자)를 도출하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🧩 ANAGRAM SOLVER: H C P D</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;'>\n        IP 주소를 동적으로 할당해 주는 대표적인 네트워크 표준 규약의 영어 약어로 재정렬하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 16,
        "title": "Subnet Mistake (김진혁의 실수 1)",
        "filename": "ef5ad16e.html",
        "verify_hash": "8527a891e224136950ff32ca212b45bc93f69fbb801c3b1ebedac52775f99e61",
        "speaker": "네트워크 라우팅 로그",
        "role": "ROUTING ERROR",
        "avatar": "NET",
        "dialogue": "김진혁 차장이 장애 발생 30분 전,\n라우터 서브넷 마스크 대역을 조작하면서 실수로 CIDR 마스크 범위를 `/28` 로 지정해 버렸습니다.\n이로 인해 스토리지와 서버 대역이 끊겼습니다.\n\n서브넷 마스크 `/28` 등급 대역에서 서브넷 대표 주소(Network ID)와 브로드캐스트 주소(Broadcast)를 제외하고\n장비에 유효하게 수동 분배해 줄 수 있는 최대 IP(호스트) 개수를 정수 숫자로 계산하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔢 CIDR SUBMETMASK SUITE: /28</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; line-height: 1.6;'>\n        - 전체 IP 주소 표현 비트: 32비트<br>\n        - 호스트 할당 비트수: 32비트 - 28비트 = 4비트 (2^4 = 총 16개 주소)<br>\n        - 사용 불가 특수한 주소: 2개 (네트워크 ID 주소 & 브로드캐스트 IP)<br>\n        - <strong style='color: var(--accent-magenta);'>계산 공식: 2^(32 - 28) - 2</strong>\n    </p>\n</div>"
    },
    {
        "stage": 17,
        "title": "SAN Storage (김진혁의 실수 2)",
        "filename": "0e3d9fd2.html",
        "verify_hash": "2fac394011e7d326f9c7ff5e532316be43ce2e7d88b4f1377f585e8c8c083672",
        "speaker": "iSCSI 연결 관리자",
        "role": "STORAGE LOG",
        "avatar": "SAN",
        "dialogue": "서브넷 격리 사고 이후 스토리지(SAN)와 데이터베이스 간의 블록 데이터 통신 연결이 오프라인되었습니다.\n\n스토리지와 서버 간의 디스크 읽기/쓰기 채널을 재연결하고 iSCSI 프로토콜 통신을 정상화시키기 위해, 네트워크 장비가 사용하는 기본 표준 TCP 포트 번호 4자리를 기입해 주십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔌 PROTOCOL PORT CHECK: iSCSI TARGET</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;'>\n        힌트: 인터넷 소형 컴퓨터 시스템 인터페이스(iSCSI) 통신 프로토콜이 표준으로 점유하여 사용하는 포트 번호입니다.\n    </p>\n</div>"
    },
    {
        "stage": 18,
        "title": "Time Drift (이재헌의 실수)",
        "filename": "58addc3e.html",
        "verify_hash": "f020272c938ba0a213d31613fd5a1a8b053c693d489551f8b24e900db43d6873",
        "speaker": "이재헌 과장",
        "role": "서버 담당",
        "avatar": "LEE_JH",
        "dialogue": "아차... TQO님, 제가 이번 서버 증설 당시에 시간 자동 동기화(NTP) 스케줄을 꺼두는 바람에,\n현재 WAS 물리 서버의 시계가 실제 시간(VDI 표준 시간)보다 정확히 '15분 느리게' 흘러가고 있는 것을 뒤늦게 확인했습니다.\n\nWAS 내부 로그기록 상 강제 셧다운이 수행된 기록 시각은 '01:58'입니다.\n이 기록에 15분 오차를 정상적으로 보정한 실제 세상의 정확한 표준 시간(HHMM)을 4자리 숫자로 계산하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⏳ TIME SYNC DRIFT LOGS</div>\n    <ul style='list-style-type: square; padding-left: 20px; font-size: 0.85rem; line-height: 1.6; color: var(--text-primary);'>\n        <li>WAS 서버 기록 시각: 01:58 (서버 시계가 15분 느린 상태)</li>\n        <li>물리적 실제 표준 시각 = 서버 기록 시각 + 15분 오차 보정</li>\n        <li><strong style='color: var(--accent-magenta);'>요구 포맷: 4자리 디지털 형식 (예: 01시 10분 -> 0110)</strong></li>\n    </ul>\n</div>"
    },
    {
        "stage": 19,
        "title": "The Culprit (진범 도출)",
        "filename": "60268820.html",
        "verify_hash": "3a693a0e2772b93bc89e4ba6167e17118923d7bdae9e10f1857a89d30540d85f",
        "speaker": "TQO 사건 합동 수사반",
        "role": "INVESTIGATION",
        "avatar": "TQO",
        "dialogue": "모든 인프라 모순을 추적한 결과 사건 당일의 실제 표준 시간 타임라인이 규명되었습니다.\n\n- 01:45 : DBA 박재욱 차장, backup.sh 백업 스케줄 자동 기동 시작\n- 02:05 : 백업 프로세스 정상 종료. DBA 세션 로그아웃 및 VDI 사용 IP 반납 완료\n- 02:13 : (실제 시각 기준) 코어 WAS 서버 강제 중단 명령어 실행 및 중단 장애 발생\n\n운영 규정에 따르면, DBA가 02:05에 로그아웃하고 반납한 IP는 비어 있는 상태였습니다. 이 빈 IP를 가로채 02:13에 은밀하게 서버에 침투해 중단 명령을 내리고 DBA 박 차장에게 누명을 씌우려 한 진범의 이름을 기재하십시오.\n\n[용의자 후보]\n박용철, 권남훈, 김진혁, 박재욱, 박주암, 이재헌",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔎 REAL-TIME TIMELINE COMPARISON</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;'>\n        누군가가 DHCP의 규약 허점을 이용하여 DBA 박 차장이 사용하다가 반납한 IP 주소를 곧바로 할당받아 악용한 물증을 확보했습니다.<br>\n        조직도 상의 진범 이름 3글자를 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 20,
        "title": "Ticket Closed (최종 결재)",
        "filename": "6c46331e.html",
        "verify_hash": "a4c3ed04a95a3da14a9d235c83d868bed7c0f45cf7f3faa751ee8f50598d2211",
        "speaker": "박용철 파트장",
        "role": "품질총괄",
        "avatar": "PARK_YC",
        "dialogue": "훌륭하네 TQO! 김진혁 차장이 본인의 라우팅 작업 실수를 감추기 위해 WAS 서버를 다운시키고 DBA에게 혐의를 뒤집어 씌우려 한 사실이 명백히 입증되었군!\n\n자네 덕분에 장애 관제 티켓 최종 결재 단계까지 도달했네. 티켓을 최종 승인 종결(Incident Closed) 처리하고 시스템을 정상 롤백하기 위해 마지막 확인 단어로 영문 소문자 [ done ]를 기입해 주게!",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>✅ RESOLUTION REPORT APPROVAL</div>\n    <p style='color: var(--text-primary); font-size: 0.85rem; line-height: 1.6;'>\n        - 장애 명칭: Core WAS Shutdown Incident<br>\n        - 조치 상태: 진범 식별 완료 및 DBA 누명 해소<br>\n        - 최종 승인 코드: done\n    </p>\n</div>"
    }
]

html_template = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Operation: 블랙아웃 - Stage {stage_num:02d}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body class="terminal-theme">
    <div class="grid-bg"></div>
    
    <div class="app-container">
        <!-- Common Header -->
        <header>
            <div class="logo-section">
                <h1>OPERATION: BLACKOUT <span class="tqo-badge">TQO CORE</span></h1>
            </div>
            
            <div class="system-status">
                <div class="status-item">
                    <span class="status-indicator red"></span>
                    <span class="status-label">SYS STATUS:</span>
                    <span class="status-value">CRITICAL EMERGENCY</span>
                </div>
                <div class="status-item">
                    <span class="status-label">CURR STAGE:</span>
                    <span class="status-value">{stage_num:02d} / 20</span>
                </div>
            </div>

            <!-- Dynamic SLA metric widget -->
            <div class="sla-widget">
                <span class="sla-title">SLA RATIO</span>
                <div class="sla-bar-container">
                    <div class="sla-bar"></div>
                </div>
                <span class="sla-value" style="font-family: var(--font-mono); font-size: 0.8rem; font-weight: bold;">99.90%</span>
            </div>
        </header>

        <!-- Stage Game Body -->
        <div class="dashboard-grid" id="stage-container" data-stage="{stage_num}" data-verify="{verify_hash}">
            <!-- Left Narrative Area -->
            <main class="main-stage-panel">
                <div class="panel-header">
                    <div class="panel-title">
                        📡 DETECTED LOG FILE & SUSPECT SHIELD
                    </div>
                    <div class="stage-badge">
                        STAGE {stage_num:02d} : {stage_title}
                    </div>
                </div>

                <div class="story-container">
                    <!-- Dialogue representation -->
                    <div class="dialogue-card speaker-suspect">
                        <div class="avatar-container">
                            <div class="avatar-placeholder">{avatar}</div>
                        </div>
                        <div class="dialogue-body">
                            <div class="dialogue-speaker">
                                <span>{speaker}</span>
                                <span class="speaker-role">{role}</span>
                            </div>
                            <div class="dialogue-text typing-text" data-text="{dialogue}">
                                {dialogue}
                            </div>
                        </div>
                    </div>

                    <!-- Gimmick HTML rendering -->
                    {gimmick_html}
                </div>
            </main>

            <!-- Right Terminal Input Area -->
            <aside class="terminal-panel">
                <div class="terminal-header">
                    <div class="terminal-controls">
                        <span class="control-dot close"></span>
                        <span class="control-dot minimize"></span>
                        <span class="control-dot maximize"></span>
                    </div>
                    <div class="terminal-title">tqo@his-system:~/incident_monitor</div>
                </div>

                <div class="terminal-body">
                    <div class="terminal-output">
                        <p class="system-log">HIS Incident Management Subsystem v1.0.4</p>
                        <p class="system-log">Loading kernel security context for Stage {stage_num:02d}...</p>
                        <p class="system-log">Ready. Enter decrypted passcode or entity key to route next file.</p>
                        <p style="color: var(--text-muted);">--------------------------------------------------------</p>
                    </div>

                    <div class="terminal-prompt">
                        <span class="prompt-symbol">[root@tqo-system ~]#</span>
                        <input type="text" class="terminal-input" placeholder="Enter key..." autofocus autocomplete="off" spellcheck="false">
                        <button class="submit-btn">EXEC</button>
                    </div>
                </div>
            </aside>
        </div>
    </div>

    <script src="game.js"></script>
</body>
</html>
"""

clear_page_html = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Operation: 블랙아웃 | 클리어</title>
    <link rel="stylesheet" href="style.css">
</head>
<body class="terminal-theme">
    <div class="grid-bg"></div>
    
    <div class="app-container" style="justify-content: center;">
        <div class="landing-panel" style="border: 2px solid var(--accent-green); box-shadow: var(--shadow-green);">
            <div>
                <span class="tqo-badge" style="background: var(--accent-green); font-size: 0.9rem; padding: 4px 12px; margin-bottom: 15px; display: inline-block;">INCIDENT STATUS: CLOSED & RESOLVED</span>
                <h1 class="landing-title glitch" data-text="OPERATION COMPLETE" style="color: var(--accent-green); text-shadow: var(--shadow-green);">OPERATION COMPLETE</h1>
                <p class="landing-subtitle" style="color: var(--accent-blue);">SLA 가동률 99.90% 수호 완료 • 인프라 신뢰성 복구 성공</p>
            </div>
            
            <div style="border: 1px solid var(--accent-green); padding: 25px; border-radius: 8px; background: rgba(0,0,0,0.6); text-align: left; line-height: 1.8; font-size: 0.95rem; font-family: var(--font-mono);">
                <p style="color: var(--accent-green); font-weight: bold; margin-bottom: 15px; font-family: var(--font-title); font-size: 1.1rem; border-bottom: 1px solid rgba(0,255,102,0.3); padding-bottom: 5px;">[TICKET RESOLUTION REPORT]</p>
                <div style="display: grid; grid-template-columns: 140px 1fr; gap: 8px; color: var(--text-primary);">
                    <div style="color: var(--text-muted);">INCIDENT TICKET:</div><div>HIS-20260721-0200</div>
                    <div style="color: var(--text-muted);">ASSIGNED OFFICER:</div><div style="color: var(--accent-blue); font-weight: bold;">Technical Quality Officer (TQO)</div>
                    <div style="color: var(--text-muted);">ROOT CAUSE:</div><div>네트워크 담당 김진혁 차장의 OSPF 라우팅 오설정 은폐 공작. (DBA 누명 해소)</div>
                    <div style="color: var(--text-muted);">SLA IMPACT:</div><div style="color: var(--accent-green); font-weight: bold;">99.90% (KPI TARGET ACHIEVED)</div>
                    <div style="color: var(--text-muted);">STATUS:</div><div style="color: var(--accent-green);">CLOSED (SUCCESS)</div>
                </div>
            </div>

            <div style="text-align: left; line-height: 1.6; font-size: 0.9rem; margin-top: 10px;">
                <h3 style="font-family: var(--font-title); color: var(--accent-blue); margin-bottom: 10px;">🏆 TQO 종합 평가 등급</h3>
                <p>당신은 사내 최고 권위의 인프라 정밀 품질 위원회로부터 <strong>1등급(Grade S: Reliability Master)</strong> 인증서 수여자로 결정되었습니다. 복잡하게 꼬인 인프라 아키텍처의 물리적 모순을 추적하고, 인적 방해와 누명을 뚫고 장애 원인을 완벽히 실증하였습니다.</p>
            </div>

            <div style="display: flex; gap: 20px; justify-content: center; margin-top: 15px;">
                <button onclick="startNewGame()" class="btn-cyber btn-secondary">다시 플레이 (Restart)</button>
            </div>
            
            <footer style="margin-top: 20px; font-family: var(--font-mono); font-size: 0.75rem; color: var(--text-muted);">
                HIS (HYPER INFORMATION SYSTEM) • TQO INCIDENT ANALYZER v1.0.4
            </footer>
        </div>
    </div>

    <script src="game.js"></script>
</body>
</html>
"""

# Write stage pages
for s in stages:
    content = html_template.format(
        stage_num=s["stage"],
        stage_title=s["title"],
        verify_hash=s["verify_hash"],
        avatar=s["avatar"],
        speaker=s["speaker"],
        role=s["role"],
        dialogue=s["dialogue"],
        gimmick_html=s["gimmick_html"]
    )
    with open(s["filename"], "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {s['filename']}")

# Write clear page (8505f529.html)
with open("8505f529.html", "w", encoding="utf-8") as f:
    f.write(clear_page_html)
print("Generated Clear Page: 8505f529.html")
print("All stages generated successfully.")
