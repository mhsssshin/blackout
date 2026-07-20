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
        "dialogue": "TQO 터미널 단말기 부팅이 완료되었습니다. 시스템 분석 모드로 진입하기 위해서는 권남훈 파트장의 인가 코드가 필요합니다. 본 화면에는 노출된 단서가 없습니다. 개발자 도구(F12)를 열어 시스템의 원천 코드(HTML 주석)를 분석하십시오.",
        "gimmick_html": "<!-- KEY: 179 -->\n<div class='puzzle-container'>\n    <div class='puzzle-title'>🔒 ACCESS PROTECTION KEY</div>\n    <p style='color: var(--text-muted); font-size: 0.9rem;'>인가 토큰이 보안 커널에 의해 물리 차단되었습니다. HTML 소스코드 주석에 기록된 백업 마스터 키를 찾아 터미널에 입력하십시오.</p>\n</div>"
    },
    {
        "stage": 2,
        "title": "Encrypted Packet (Base64)",
        "filename": "b4bcdd0d.html",
        "verify_hash": "f5334f59cc820a5c99fd2a5b5527884c821c19f1daa7c825368603aba61d6178",
        "speaker": "네트워크 패킷 스니퍼",
        "role": "PACKET MONITOR",
        "avatar": "NET",
        "dialogue": "권남훈 파트장의 보안 단말기(VDI)로 전송된 내부 사설 포트 전송 패킷이 캡처되었습니다. 권 파트장의 망분리 정책에 따라 데이터 페이로드는 64진법 텍스트로 인코딩되어 있습니다. 이 인코딩 패킷을 복호화하여 평문 내에 숨겨진 포트 번호를 도출하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>📡 PACKET PAYLOAD DUMP</div>\n    <p style='font-family: var(--font-mono); color: var(--accent-magenta); font-size: 1.1rem; text-align: center; padding: 10px; background: rgba(0,0,0,0.5); border-radius: 4px; letter-spacing: 1px;'>UG9ydCAyMzIx</p>\n    <p style='color: var(--text-muted); font-size: 0.8rem; margin-top: 10px;'>힌트: Base64 형식으로 인코딩된 포트 번호 페이로드입니다.</p>\n</div>"
    },
    {
        "stage": 3,
        "title": "Log Flood (권한 검색)",
        "filename": "83e5e934.html",
        "verify_hash": "4099ed5ba70aebc5a9dc26bc2093d4b45839f99b306bd12f68cedfd351e6ab7a",
        "speaker": "스토리지 커널 감사 로그",
        "role": "AUDITOR",
        "avatar": "AUD",
        "dialogue": "권남훈 파트장은 모든 결산 데이터 디렉토리 파일들이 규정에 부합하는 표준 권한 마스크(rwxr-xr-x)를 갖고 있다고 주장했습니다. 그러나 감사 결과 단 하나의 백업 파일이 타인에게 쓰기/읽기 권한이 탈취될 수 있는 취약한 권한(rwxr-xr--)으로 잘못 배포되었습니다. 스크롤을 내려 유일한 에러 권한 파일을 찾아 3자리 8진수 권한 값으로 입력하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>📂 DIRECTORY PERMISSIONS SCAN</div>\n    <div class='log-flood-area'>\n" + "\n".join([f"        <div class='log-flood-line'>-rwxr-xr-x  1 tqo_ops  staff  4096 Jul 21 02:00 file_{i:03d}.bin</div>" if i != 273 else "        <div class='log-flood-line log-target'>-rwxr-xr--  1 tqo_ops  staff  8204 Jul 21 01:45 backup_corrupt.bin  &lt;-- WARNING!</div>" for i in range(500)]) + "\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.8rem; margin-top: 10px;'>참고: 8진수 표기법 (r=4, w=2, x=1. 예: rwxr-xr-x = 755)</p>\n</div>"
    },
    {
        "stage": 4,
        "title": "The Blackout (Hidden Text)",
        "filename": "13b3bfc6.html",
        "verify_hash": "7970f1f08c678259aa519bb1beaa3e57186a40b0c3fbfc572d37f874125d38fe",
        "speaker": "시스템 긴급 백업 단말",
        "role": "EMERGENCY CONSOLE",
        "avatar": "CRT",
        "dialogue": "서버가 완전한 블랙아웃 상태에 빠져 화면 신호가 끊겼습니다! 하지만 TQO 대응 절차에 따라 긴급 복구 모듈의 터미널 캔버스 어딘가에 보이지 않는 색상으로 복구 비밀코드가 렌더링되어 있습니다. 마우스 드래그(또는 Ctrl+A)를 사용해 숨겨진 보안 텍스트 코드를 반전시켜 읽어내십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>💡 VISIBILITY RESTORATION OVERLAY</div>\n    <div class='hidden-text-container'>\n        <span class='hidden-error-text'>404500</span>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.8rem; margin-top: 10px;'>드래그하여 숨겨진 에러 코드를 찾아 터미널에 입력하십시오.</p>\n</div>"
    },
    {
        "stage": 5,
        "title": "Zalgo Text (글자 깨짐)",
        "filename": "48b42551.html",
        "verify_hash": "af4883c99558a3f6ef589d7e9a69585135ebac48f6b55c12e5e96849dc3707ee",
        "speaker": "오류 콘솔 리포트",
        "role": "LOG ANALYZER",
        "avatar": "ERR",
        "dialogue": "시스템 셧다운 충격으로 인해 콘솔 메모리 덤프의 일부 텍스트가 심각하게 훼손(Zalgo Text)되었습니다. 노이즈 가득한 기괴한 글자 더미 속에서 일관되게 반복적으로 삽입되어 있는 대문자 알파벳 3자리 단어(B, A, D)를 찾아내십시오. 찾아낸 단어(BAD)의 각 알파벳 아스키코드(ASCII) 10진수 값을 공백 없이 합쳐서 입력하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⚠️ CORRUPTED STRING BUFFER</div>\n    <div class='zalgo-box'>\n        S̶y̶s̶t̶e̶m̶ <b>B̷</b>u̷f̷f̷e̷r̷ <b>A̵</b>n̷o̷m̷a̷l̷y̷ <b>D̵</b>e̷t̷e̷c̷t̷e̷d̷\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.8rem; margin-top: 10px;'>힌트: 아스키코드 표 (B=66, A=65, D=68)</p>\n</div>"
    },
    {
        "stage": 6,
        "title": "Caesar Cipher (시저 암호)",
        "filename": "db590ac0.html",
        "verify_hash": "08434ba9cdf55a02284e2913400586cd289878e0f055f7bb0b07ce392caeb989",
        "speaker": "커널 보안 세션",
        "role": "SECURITY ENGIN",
        "avatar": "SEC",
        "dialogue": "장애 당시 강제로 코어 서버를 파괴한 시스템 침입 명령어의 흔적이 암호 로그에 기록되었습니다. 공격자는 간단한 환자 암호(시저 암호)를 사용했습니다. 암호화 법칙을 풀어 명령어를 평문 영문으로 도출하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔐 DECRYPTION KEY: -3 Shift (Caesar)</div>\n    <div style='background: rgba(0,0,0,0.5); padding: 15px; border-radius: 6px; border: 1px solid var(--border-color); font-family: var(--font-mono); text-align: center;'>\n        <p style='color: var(--accent-magenta); font-size: 1.2rem; letter-spacing: 2px;'>vkXwgrzq</p>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.8rem; margin-top: 10px;'>HINT: 모든 알파벳 문자를 왼쪽(앞쪽)으로 3칸씩 이동시키십시오. (예: d -> a, X -> u, k -> h)</p>\n</div>"
    },
    {
        "stage": 7,
        "title": "SLA Metric (SLA 다운타임 계산)",
        "filename": "4ae9c668.html",
        "verify_hash": "2841dad7e57a80b5a9fdc7cd5799e7108f394e1c6157a8feb8e83db0808d3432",
        "speaker": "박용철 파트장",
        "role": "품질총괄",
        "avatar": "PARK_YC",
        "dialogue": "이보게 TQO! 우리가 이번 차세대 금융 코어 품질 보장 계약에서 약속한 연간 가동률(SLA)이 99.9%일세. 1년 365일을 기준으로 가동률 99.9%를 유지하려면 1년 동안 허용되는 최대 장애 누적 시간이 정확히 몇 '분(Minute)'인지 알고 있나? 계산 착오 예방을 위해 SLA 약식 가동률 기준값(525분)에 우리 부서 내부 통제 보정 계수인 10을 곱한 '최종 가이던스 통제 수치'를 터미널에 기재하여 보고해 주게!",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>📊 SLA METRIC SHEET</div>\n    <ul style='list-style-type: square; padding-left: 20px; font-size: 0.9rem; line-height: 1.6; color: var(--text-primary);'>\n        <li>연간 기준일: 365일 (단순화)</li>\n        <li>보증 가동 범위: 99.9% (연간 최대 허용 정지 0.1%)</li>\n        <li>수치식: (365일 * 24시간 * 60분) * 0.001 = 525.6분</li>\n        <li><strong style='color: var(--accent-magenta);'>입력 요구 조건: 약식 가동 한계값(525분) * 내부 보정 계수(10)</strong></li>\n    </ul>\n</div>"
    },
    {
        "stage": 8,
        "title": "Governance (IT 거버넌스 규정)",
        "filename": "e3ad4d0a.html",
        "verify_hash": "0b483f69c9eaed1e8f96259917fd826bc27d8cc20f8a5715880fb0b8a011def2",
        "speaker": "권남훈 파트장",
        "role": "운영총괄",
        "avatar": "KWON_NH",
        "dialogue": "장애가 발생했을 때 TQO는 임시 조치를 취하는 것에 머물러선 안 됩니다. IT 거버넌스 표준에 의거하여, 장애 현상(Incident)을 넘어 근본적인 원인(Problem)을 규명하고 재발 방지 지식을 구성하는 글로벌 모범 프레임워크의 명칭(소문자 4글자 약어)을 입력하여 거버넌스 교육 이수를 인증하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>📚 IT SERVICE GOVERNANCE FRAMEWORK</div>\n    <p style='color: var(--text-muted); font-size: 0.9rem;'>서비스 품질 보증, 장애 관리, 자산 관리 등을 규정하는 사실상의 국제 표준 4글자 가이드라인 라이브러리.</p>\n</div>"
    },
    {
        "stage": 9,
        "title": "Knowledgebase (지식 정보 조회)",
        "filename": "cee89b5e.html",
        "verify_hash": "27dce682e1ad2f2106be21d27e8025de5de7ee65cecc737d4f27a33af4c29a8a",
        "speaker": "HIS 지식관리 시스템",
        "role": "KNOWLEDGEBASE",
        "avatar": "KB",
        "dialogue": "장애 유형별 대응 SOP 조회를 위한 사내 지식 라이브러리 포털입니다. 현재 차세대 데이터베이스의 파괴 증상이 목격되었습니다. 아래 포털 덤프 리스트 중에서 '스토리지 동기화 실패로 인한 DB 파손 대응 매뉴얼'에 부합하는 올바른 문서 코드의 숫자 4자리를 도출하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔍 KNOWLEDGEBASE DOCUMENT LIST</div>\n    <table style='width: 100%; border-collapse: collapse; font-size: 0.85rem; text-align: left; margin-top: 10px;'>\n        <tr style='border-bottom: 1px solid var(--border-color); color: var(--accent-blue);'>\n            <th style='padding: 6px;'>문서코드</th>\n            <th style='padding: 6px;'>주제</th>\n        </tr>\n        <tr>\n            <td style='padding: 6px;'>KB-7108</td>\n            <td style='padding: 6px;'>웹 애플리케이션 서버 커널 튜닝 규격</td>\n        </tr>\n        <tr style='background: rgba(0, 229, 255, 0.05);'>\n            <td style='padding: 6px; font-weight: bold; color: var(--accent-green);'>KB-8204</td>\n            <td style='padding: 6px; color: var(--text-primary);'>스토리지 동기화 실패로 인한 DB 파손 대응 매뉴얼</td>\n        </tr>\n        <tr>\n            <td style='padding: 6px;'>KB-9321</td>\n            <td style='padding: 6px;'>L4 네트워크 로드밸런서 VIP 이중화 스키마</td>\n        </tr>\n    </table>\n</div>"
    },
    {
        "stage": 10,
        "title": "The Cronjob (Crontab 스케줄링)",
        "filename": "524cfb66.html",
        "verify_hash": "318fb6b0fd6eb7ef86613797123429db40159a50c0b443197c3a229ecefc07fb",
        "speaker": "박재욱 차장",
        "role": "DBA",
        "avatar": "PARK_JW",
        "dialogue": "억울합니다 TQO님! 저는 그날 새벽 데이터베이스 결산 백치를 수동으로 돌려 서버를 죽인 적이 없습니다. 모든 것은 시스템에 등록된 스케줄에 따라 자동화 프로그램(`backup.sh`)이 수행되었을 뿐입니다. 아래 백업 크론탭(crontab) 설정을 분석하여, 해당 백업 배치가 기동하는 정확한 시각을 24시간 표기법의 4자리 숫자(HHMM)로 기록해 제 누명을 벗겨주십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⏰ TARGET CRONTAB CONFIGURATION</div>\n    <div style='background: #020306; font-family: var(--font-mono); padding: 15px; border-radius: 6px; border: 1px solid var(--border-color); text-align: center; font-size: 1.1rem; color: var(--accent-blue);'>\n        45 1 * * * /usr/sbin/backup.sh\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.8rem; margin-top: 10px;'>크론탭 구조: [분] [시] [일] [월] [요일] [명령어]</p>\n</div>"
    },
    {
        "stage": 11,
        "title": "The Command (박주암 과장)",
        "filename": "e3307ab7.html",
        "verify_hash": "53c148b793bd0c621b03b40afe93b7c39bce8b4d00157bc10142b8a848af32ac",
        "speaker": "박주암 과장",
        "role": "WAS 담당",
        "avatar": "PARK_JA",
        "dialogue": "새벽에 서버가 셧다운되는 순간, 누군가가 제 WAS 콘솔 권한을 악용해 로컬 DB에 수동 인증 조작을 시도한 흔적이 잡혔습니다. 원래는 DB 쿼리 연결을 위해 오라클 전용 커맨드 유틸리티를 실행하려 한 것인데, 침입자가 영문 타이핑을 오타 없이 입력했습니다. 이 오라클 인증 질의 클라이언트 명령어의 올바른 소문자 스펠링을 기입해 주십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>💻 INCIDENT COMMAND HISTORY DUMP</div>\n    <p style='font-family: var(--font-mono); color: var(--accent-magenta); font-size: 0.95rem; line-height: 1.6;'>\n        $ cd /u01/app/oracle/product/12.1.0/dbhome_1/bin<br>\n        $ ./<strong style='color: var(--accent-green); text-shadow: 0 0 5px rgba(0,255,102,0.5);'>sqlplus</strong> / as sysdba<br>\n        &gt; SHUTDOWN IMMEDIATE;<br>\n        <span style='color: var(--accent-red);'>[02:13:21] DISCONNECTED FROM DATABASE.</span>\n    </p>\n</div>"
    },
    {
        "stage": 12,
        "title": "The Network Lie (김진혁 차장)",
        "filename": "16417f5b.html",
        "verify_hash": "debdc6fdb6c19c94ff78b653767bfac108d84ed51a54a58a72866dc635b15729",
        "speaker": "김진혁 차장",
        "role": "네트워크 담당",
        "avatar": "KIM_JH",
        "dialogue": "저는 결백합니다. 장애 발생 시각에 기계실 외부 휴게실에서 노트북으로 T5004 라우터의 OOO 안테나 신호를 정상 수신하여 망 장애가 아님을 지속적으로 모니터링하고 있었습니다. 제 접속에는 아무런 유선 플러그인 기록이 없습니다!",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🌐 T5004 ROUTER HARDWARE SPECIFICATION</div>\n    <div class='ascii-diagram'>\n+------------------------------------------------+\n|  T5004 INTERNET RACK HUB                      |\n|                                                |\n|  [LAN1]   [LAN2]   [LAN3]   [LAN4]   [WAN]     |\n|  [ [O] ]  [ [O] ]  [ [X] ]  [ [X] ]  [ [O] ]   |\n|   |  |     |  |                         |  |   |\n|    유선     유선                         인터넷  |\n|                                                |\n|  * WARNING: NO WIRELESS ANTENNA MODULE *       |\n|  * ONLY WIRED ETHERNET CONNECTION SUPPORTED *  |\n+------------------------------------------------+\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.8rem; margin-top: 10px;'>김진혁 차장의 주장: '무선 OOO 신호를 잡아 모니터링했다.'<br>장비 스펙: 무선 지원 불가, 오직 유선 포트만 존재.<br>김 차장이 주장한 거짓말 속 기술 명칭(영문 소문자 4글자)을 쓰십시오.</p>\n</div>"
    },
    {
        "stage": 13,
        "title": "The Server Lie (이재헌 과장)",
        "filename": "94e06050.html",
        "verify_hash": "692e4e5decffcf5eac86471ba27ac56a861268d060e4a53a0c768617f4d3a56f",
        "speaker": "이재헌 과장",
        "role": "서버 담당",
        "avatar": "LEE_JH",
        "dialogue": "품질 테스트 당시 CPU 자원을 풍부하게 튜닝해 두어, 서버 스펙이나 하드웨어 부족으로 중단될 리는 없다고 장담합니다. 충분히 여유가 있었을 텐데요?",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⚙️ VM INSTANCE SPECIFICATION OVERVIEW</div>\n    <div class='cpu-widget'>\n        <div>INSTANCE_NAME: Core-WAS-01</div>\n        <div>ALLOCATED_VCPU: 1 Core (Shared)</div>\n        <div>RESERVED_RAM: 512MB (Overcommitted)</div>\n        <div class='cpu-bar'>CPU USAGE: [██████████] 99.6% (Overload)</div>\n        <div style='color: var(--accent-magenta); margin-top: 5px;'>AVAILABLE_MARGIN: 0.4%</div>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px;'>시스템 튜닝이 충분히 넉넉한 상태가 아니라, 자원이 고갈 직전이어서 물리 장비의 숨통만 겨우 붙여놓은 한계 튜닝 상태를 의미하는 IT 용어(영문 소문자 7자)를 기재하십시오.</p>\n</div>"
    },
    {
        "stage": 14,
        "title": "The Motivation (박용철 총괄)",
        "filename": "c70ec350.html",
        "verify_hash": "838940b6f1deea2e9aca2c69a4df9a484139e1d8ab954a1b2366df3777ae416b",
        "speaker": "박용철 파트장",
        "role": "품질총괄",
        "avatar": "PARK_YC",
        "dialogue": "서버 셧다운 직전, 데이터베이스에 심각한 로지컬 블록 깨짐(Block Corruption)이 잡혔다는 보고가 있네. 아래의 타겟 정규표현식(Regex)을 이용해 아래의 내부 로그 중에서 데이터 무결성을 파괴하고 물리 손상을 가져온 오라클 핵심 내부 오류 코드 명칭을 식별해 내어 소문자로 보고하게!",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔍 CORRUPTION PATTERN DETECTION FILTER</div>\n    <ul style='list-style-type: square; padding-left: 20px; font-size: 0.85rem; line-height: 1.6; color: var(--accent-blue); font-family: var(--font-mono);'>\n        <li>정규식 필터: ^[A-Za-z]+-[0-9]{5}$</li>\n        <li>[DB ERROR LOG DUMP]:</li>\n        <li style='color: var(--text-muted);'>- sys-info-10023: buffer read</li>\n        <li style='color: var(--accent-magenta); font-weight: bold;'>- ORA-00600: internal error code</li>\n        <li style='color: var(--text-muted);'>- DB-CONN-5020: timeout error</li>\n    </ul>\n</div>"
    },
    {
        "stage": 15,
        "title": "The VDI Rule (권남훈 총괄)",
        "filename": "aac380d4.html",
        "verify_hash": "6f89bddf8582a8d223e132d10c9436e788687f159fbbf5ac36a6eb14d307a3fa",
        "speaker": "권남훈 파트장",
        "role": "운영총괄",
        "avatar": "KWON_NH",
        "dialogue": "우리 센터의 가동 규칙에 의하면, SRE 엔지니어들의 VDI 세션이 접속 종료되는 즉시 할당된 내부 IP는 즉각 풀(Pool)로 반환되며, 다음 접속자에게 순차 재할당됩니다. 이 동적 IP 분배와 자원 자동 관리를 담당하는 네트워크 표준 프로토콜 약어(H C P D)의 철자가 해커 공격으로 뒤섞여 버렸습니다. 올바른 영문 소문자 4자리를 정렬하여 규약의 원형을 입력하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🧩 ANAGRAM SOLVER: H C P D</div>\n    <p style='color: var(--text-muted); font-size: 0.9rem;'>IP 동적 자동 할당 프로토콜의 약어를 알파벳 재배열을 통해 도출하십시오.</p>\n</div>"
    },
    {
        "stage": 16,
        "title": "Subnet Mistake (김진혁의 실수 1)",
        "filename": "ef5ad16e.html",
        "verify_hash": "8527a891e224136950ff32ca212b45bc93f69fbb801c3b1ebedac52775f99e61",
        "speaker": "네트워크 라우팅 로그",
        "role": "ROUTING ERROR",
        "avatar": "NET",
        "dialogue": "김진혁 차장이 장애 발생 30분 전, 라우터 서브넷 마스크 대역을 조작하면서 실수로 CIDR 마스크 범위를 `/28` 로 지정해 버렸습니다. 이로 인해 스토리지와 서버 대역이 끊겼습니다. 서브넷 마스크 `/28` 등급 대역에서 서브넷 대표 주소(Network ID)와 브로드캐스트 주소(Broadcast)를 제외하고 장비에 유효하게 수동 분배해 줄 수 있는 최대 IP(호스트) 개수를 정수 숫자로 계산하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔢 CIDR SUBMETMASK SUITE: /28</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;'>\n        전체 비트수: 32비트<br>\n        호스트 할당 가능 비트수: 32 - 28 = 4비트 (2^4 = 16개)<br>\n        사용 불가 특수 IP 주소 개수: 2개 (네트워크 주소 & 브로드캐스트 주소)<br>\n        <span style='color: var(--accent-magenta); font-weight: bold;'>공식: 2^(32 - Mask) - 2</span>\n    </p>\n</div>"
    },
    {
        "stage": 17,
        "title": "SAN Storage (김진혁의 실수 2)",
        "filename": "0e3d9fd2.html",
        "verify_hash": "2fac394011e7d326f9c7ff5e532316be43ce2e7d88b4f1377f585e8c8c083672",
        "speaker": "iSCSI 연결 관리자",
        "role": "STORAGE LOG",
        "avatar": "SAN",
        "dialogue": "서브넷 격리 사고 이후 SAN(Storage Area Network) 스토리지 모듈과 IP 통신 링크가 완전히 오프라인되었습니다. 유효 호스트 링크를 재수립하고 데이터베이스와 블록 저장소 간의 통신을 정상화시키기 위해, iSCSI 통신용 프로토콜 규격이 기본적으로 점유하여 작동시키는 전용 TCP 포트 번호를 입력하여 포트 바인딩을 허가해 주십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔌 PROTOCOL PORT CHECK: iSCSI TARGET</div>\n    <p style='color: var(--text-muted); font-size: 0.9rem;'>인터넷 소형 컴퓨터 시스템 인터페이스(iSCSI) 통신 프로토콜의 표준 Well-known TCP 포트 번호 4자리를 도출하십시오.</p>\n</div>"
    },
    {
        "stage": 18,
        "title": "Time Drift (이재헌의 실수)",
        "filename": "58addc3e.html",
        "verify_hash": "f020272c938ba0a213d31613fd5a1a8b053c693d489551f8b24e900db43d6873",
        "speaker": "이재헌 과장",
        "role": "서버 담당",
        "avatar": "LEE_JH",
        "dialogue": "아차... TQO님, 제가 이번 서버 증설 당시에 NTP(Network Time Protocol) 자동 동기화 크론을 정지해 두는 바람에, 현재 WAS 물리 서버의 시스템 시간 클럭이 실제 한국 표준시(VDI 시간)보다 정확히 '15분 느리게' 흘러가고 있는 것을 발견했습니다. WAS 감사 로그 기록상 강제 셧다운이 수행된 시각은 '01:58'입니다. 이 기록에 시간 편차(Time Drift)를 보정한 올바른 실제 세상의 표준 시각(HHMM)을 4자리 숫자로 입력해 주십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⏳ TIME SYNC DRIFT LOGS</div>\n    <ul style='list-style-type: square; padding-left: 20px; font-size: 0.85rem; line-height: 1.6; color: var(--text-primary);'>\n        <li>WAS 서버 기록 시각: 01:58 (서버 내부 시계가 15분 느린 상태)</li>\n        <li>물리적 실제 시각 = 서버 기록 시각 + 15분 오차 보정</li>\n        <li><strong style='color: var(--accent-magenta);'>요구 포맷: 4자리 디지털 형식 (예: 02:00 -> 0200)</strong></li>\n    </ul>\n</div>"
    },
    {
        "stage": 19,
        "title": "The Culprit (진범 도출)",
        "filename": "60268820.html",
        "verify_hash": "3a693a0e2772b93bc89e4ba6167e17118923d7bdae9e10f1857a89d30540d85f",
        "speaker": "TQO 사건 합동 수사반",
        "role": "INVESTIGATION",
        "avatar": "TQO",
        "dialogue": "모든 사실이 밝혀졌습니다! 보정된 실제 시간 타임라인 분석에 근거하면, 진범의 정체가 나옵니다. DBA 박재욱 차장은 결산 배치를 마친 뒤 02:05에 완전히 시스템에서 로그아웃하여 VDI IP를 반납했습니다. 권남훈 파트장의 IP 동적 유동 할당 규약(DHCP)에 따라 그 비어 버린 IP를 곧바로 가로채서, 02:13에 은밀하게 WAS 서버에 침투해 sqlplus로 DB를 중단시키고 서버를 강제 다운시킨 진짜 범인의 이름 3글자를 입력하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔎 REAL-TIME TIMELINE COMPARISON</div>\n    <table style='width: 100%; border-collapse: collapse; font-size: 0.85rem; text-align: left; margin-top: 10px; color: var(--text-primary);'>\n        <tr style='border-bottom: 1px solid var(--border-color); color: var(--accent-blue);'>\n            <th style='padding: 6px;'>실제시각</th>\n            <th style='padding: 6px;'>사건/행동 기록</th>\n        </tr>\n        <tr>\n            <td style='padding: 6px;'>01:45</td>\n            <td style='padding: 6px;'>DBA 박재욱 차장, backup.sh 자동 예약 수행 시작</td>\n        </tr>\n        <tr>\n            <td style='padding: 6px;'>02:05</td>\n            <td style='padding: 6px;'>DBA 결산 완료. VDI 세션 강제 해제 및 사용 IP 반납 완료</td>\n        </tr>\n        <tr style='background: rgba(255, 0, 85, 0.08);'>\n            <td style='padding: 6px; font-weight: bold; color: var(--accent-magenta);'>02:13</td>\n            <td style='padding: 6px; font-weight: bold; color: var(--accent-magenta);'>누군가가 DBA의 유동 IP를 받아 DB를 폭파하고 WAS 중단 커맨드 실행</td>\n        </tr>\n    </table>\n    <p style='color: var(--text-muted); font-size: 0.8rem; margin-top: 10px;'>* 주요 용의자: 박용철, 권남훈, 김진혁, 박재욱, 박주암, 이재헌</p>\n</div>"
    },
    {
        "stage": 20,
        "title": "Ticket Closed (최종 결재)",
        "filename": "6c46331e.html",
        "verify_hash": "a4c3ed04a95a3da14a9d235c83d868bed7c0f45cf7f3faa751ee8f50598d2211",
        "speaker": "박용철 파트장",
        "role": "품질총괄",
        "avatar": "PARK_YC",
        "dialogue": "훌륭하네 TQO! 김진혁 차장이 자신의 라우팅 작업 실수를 감추고 데이터 파손의 독박을 박 차장에게 씌우기 위해 이 모든 공작을 꾸몄음이 입증되었군! 자네의 과학적 데이터 분석 덕분에 억울한 누명을 풀고 시스템 무결성을 수호했네. 장애 관제 티켓 최종 결재 승인을 완료하기 위해 마무릿말 영단어(소문자 4자)를 입력하고 퇴근해 주게!",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>✅ RESOLUTION REPORT APPROVAL</div>\n    <p style='color: var(--text-primary); font-size: 0.9rem; line-height: 1.6;'>\n        - 장애 등급: HIGH Critical<br>\n        - 원인: 네트워크 관리자 라우팅 조작 실수 은폐 시도<br>\n        - 최종 결과: 시스템 복구 완료 및 진범 확보<br>\n        <span style='color: var(--accent-green); font-weight: bold;'>- 상태 코드 변경 대기 중... '완료' 처리를 위해 영단어 [ done ]를 입력하십시오.</span>\n    </p>\n</div>"
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
                <p>당신은 사내 최고 권위의 인프라 정밀 품질 위원회로부터 <strong>1등급(Grade S: reliability Master)</strong> 인증서 수여자로 결정되었습니다. 복잡하게 꼬인 인프라 아키텍처의 물리적 모순을 추적하고, 인적 방해와 누명을 뚫고 장애 원인을 완벽히 실증하였습니다.</p>
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
