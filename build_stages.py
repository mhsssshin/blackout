import os
import json
import hashlib

stages = [
    {
        "stage": 1,
        "title": "System Boot (F12)",
        "filename": "a7f93b2c.html",
        "verify_hash": "",
        "narrative": "금융 코어 WAS 서버가 알 수 없는 명령어로 강제 종료된 대형 장애 현장. 부서장과 본부장의 압박 속에 권남훈 파트장이 단말기 제어 콘솔을 켜고 다급히 움직이기 시작합니다.",
        "dialogue_list": [
            {
                "speaker": "권남훈 파트장",
                "role": "운영총괄 (예민한 리더)",
                "avatar": "avatar_kwon_nh.png",
                "text": "부팅 인가 코드가 막혀 있군요. 박용철 파트장이 VDI 보안 정책을 잠가둔 모양인데, 언제 정식 결재 올리고 승인 대기합니까!\n\n당장 F12(개발자 도구)를 열어 소스코드의 백업용 주석 키를 찾아 로그인 절차를 돌파하십시오!"
            }
        ],
        "gimmick_html": "<!-- KEY: 179 -->\n<div class='puzzle-container'>\n    <div class='puzzle-title'>🔒 ACCESS PROTECTION KEY</div>\n    <p style='color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;'>\n        인가 토큰이 보안 커널에 의해 물리 차단되었습니다.<br>\n        F12(개발자 도구)를 통해 HTML 소스코드의 주석을 분석하고 백업 마스터 키를 찾아 터미널에 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 2,
        "title": "Encrypted Packet (Base64)",
        "filename": "",
        "verify_hash": "",
        "narrative": "터미널 부팅에 성공하자마자 박용철 파트장이 다가와 방어적인 경고를 보내고, 권남훈 파트장이 격렬하게 언성을 높입니다.",
        "dialogue_list": [
            {
                "speaker": "박용철 파트장",
                "role": "품질총괄 (규정 맹신자)",
                "avatar": "avatar_park_yc.png",
                "text": "정식 승인 절차 없는 임의 시스템 조작은 심각한 규정 위반입니다. 당장 로그 분석을 중단하십시오."
            },
            {
                "speaker": "권남훈 파트장",
                "role": "운영총괄 (예민한 리더)",
                "avatar": "avatar_kwon_nh.png",
                "text": "박 파트장! 지금 본사 임원들 불호령이 안 들립니까? 규정 타령할 때가 아니니 비켜서세요!"
            },
            {
                "speaker": "박용철 파트장",
                "role": "품질총괄 (규정 맹신자)",
                "avatar": "avatar_park_yc.png",
                "text": "좋습니다. 그렇다면 우선 망의 무결성을 입증하기 위해, VDI 단말에 기록된 암호화 패킷 페이로드부터 해독해 보십시오. Base64 데이터를 디코딩해 당시 사용한 포트 번호를 입력해 인증 세션을 성립해야 수사를 승인하겠습니다."
            }
        ],
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>📡 PACKET PAYLOAD DUMP</div>\n    <div style='display: flex; gap: 15px; align-items: center; justify-content: center; background: rgba(0,0,0,0.5); padding: 15px; border-radius: 4px;'>\n        <p style='font-family: var(--font-mono); color: var(--accent-magenta); font-size: 1.25rem; letter-spacing: 1px;'>UG9ydCAyMzIx</p>\n        <button class='copy-btn' onclick=\"copyToClipboard('UG9ydCAyMzIx', this)\">COPY</button>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.5;'>\n        힌트: Base64 형식으로 변환된 포트 정보 페이로드입니다.<br>\n        디코딩 시 문자 뒤에 기재된 숫자 4자리를 찾아 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 3,
        "title": "Log Flood (권한 검색)",
        "filename": "",
        "verify_hash": "",
        "narrative": "품질총괄 박용철 파트장의 완고한 원칙 고수와 달리, 파일 배포 프로세스 상에 심각한 보안 허점이 감지됩니다.",
        "dialogue_list": [
            {
                "speaker": "박용철 파트장",
                "role": "품질총괄 (규정 맹신자)",
                "avatar": "avatar_park_yc.png",
                "text": "표준 형상 배포 도구인 rwxr-xr-x(755) 권한 규격에 맞춰 전개했기 때문에, 배포 디렉토리 보안은 완전무결합니다."
            },
            {
                "speaker": "권남훈 파트장",
                "role": "운영총괄 (예민한 리더)",
                "avatar": "avatar_kwon_nh.png",
                "text": "말도 안 되는 소리! 박 파트장의 말은 신뢰하기 어렵습니다. 즉시 스토리지의 디렉토리 권한 감사 덤프를 전수 스캔하십시오.\n\n관리 소홀로 인해 쓰기 권한이 허용된 비정상 파일(rwxr-xr--)을 가려내야 합니다. 찾아내서 수치값으로 변환해 주십시오!"
            }
        ],
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>📂 DIRECTORY PERMISSIONS SCAN</div>\n    <div class='log-flood-area'>\n" + "\n".join([f"        <div class='log-flood-line'>-rwxr-xr-x  1 tqo_ops  staff  4096 Jul 21 02:00 file_{i:03d}.bin</div>" if i != 273 else "        <div class='log-flood-line log-target'>-rwxr-xr--  1 tqo_ops  staff  8204 Jul 21 01:45 backup_corrupt.bin</div>" for i in range(500)]) + "\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.5;'>\n        힌트: 수백 줄의 리스트 속에서 무언가 다른 파일 하나가 숨어 있습니다.<br>\n        찾아낸 취약 마스크(rwxr-xr--) 값을 8진수 변환식(r=4, w=2, x=1, -=0 합산)에 대입하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 4,
        "title": "PDU Power Overload (PDU 전력 임계치 초과 적발)",
        "filename": "",
        "verify_hash": "",
        "narrative": "권남훈 파트장이 스토리지 블록 전체에 대규모 동시 디렉토리 권한 스캔을 가동시키자, 백업 전력망 선로에 급격한 과전류 오버헤드가 발생합니다. 정전 경보 장치가 작동하며 제어 터미널 화면 신호가 끊어지고 서버실 전체가 암전 상태에 직면합니다.",
        "dialogue_list": [
            {
                "speaker": "이재헌 과장",
                "role": "서버 담당 (가상화 엔지니어)",
                "avatar": "avatar_lee_jh.png",
                "text": "으악! 권 파트장님이 실행하신 권한 스캔 명령어 과부하 때문인지 주 차단기(Circuit Breaker)가 강제 트립되어 정전이 터졌습니다!"
            },
            {
                "speaker": "박주암 과장",
                "role": "WAS 담당 (실무 운영자)",
                "avatar": "avatar_park_ja.png",
                "text": "각 PDU(전력 분배 장치)의 단일 라인 한계 정격 전류는 최대 80A입니다. 이 과장님, 정전 직전에 결선되어 부하를 가하던 각 장비들의 전류 소모량 합계를 PDU별로 감사해 보십시오."
            },
            {
                "speaker": "이재헌 과장",
                "role": "서버 담당 (가상화 엔지니어)",
                "avatar": "avatar_lee_jh.png",
                "text": "아! 임계치 80A를 단독으로 초과해 서지 부하를 가하고 전체 정전을 유도한 범인 PDU의 식별 코드(pdu01, pdu02, pdu03 중 하나)를 찾아 터미널에 입력하십시오!"
            }
        ],
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔌 PDU CURRENT LOAD INVENTORY (80A MAX LIMIT)</div>\n    <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-top: 10px;'>\n        <div style='background: rgba(0,0,0,0.5); padding: 12px; border-radius: 6px; border: 1px solid var(--border-color); text-align: left;'>\n            <h4 style='color: var(--accent-blue); margin-bottom: 8px;'>[PDU-01]</h4>\n            <ul style='list-style: none; font-family: var(--font-mono); font-size: 0.8rem; padding: 0; line-height: 1.6;'>\n                <li>- Core-WAS-01 : 25A</li>\n                <li>- Core-WAS-02 : 25A</li>\n                <li>- L4-LoadBalancer : 10A</li>\n                <li>- Switch-Hub-01 : 15A</li>\n            </ul>\n        </div>\n        <div style='background: rgba(0,0,0,0.5); padding: 12px; border-radius: 6px; border: 1px solid var(--border-color); text-align: left;'>\n            <h4 style='color: var(--accent-blue); margin-bottom: 8px;'>[PDU-02]</h4>\n            <ul style='list-style: none; font-family: var(--font-mono); font-size: 0.8rem; padding: 0; line-height: 1.6;'>\n                <li>- DB-Oracle-Node1 : 35A</li>\n                <li>- DB-Oracle-Node2 : 35A</li>\n                <li>- SAN-Fibre-Switch : 12A</li>\n            </ul>\n        </div>\n        <div style='background: rgba(0,0,0,0.5); padding: 12px; border-radius: 6px; border: 1px solid var(--border-color); text-align: left;'>\n            <h4 style='color: var(--accent-blue); margin-bottom: 8px;'>[PDU-03]</h4>\n            <ul style='list-style: none; font-family: var(--font-mono); font-size: 0.8rem; padding: 0; line-height: 1.6;'>\n                <li>- Web-Server-01 : 15A</li>\n                <li>- Web-Server-02 : 15A</li>\n                <li>- NAS-Storage-Unit : 20A</li>\n                <li>- Dev-VM-Host : 15A</li>\n            </ul>\n        </div>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 15px; line-height: 1.5;'>\n        힌트: 각 PDU 분전반 하위에 가동되던 장비의 전류 소모량 합산값을 계산하여, 80A 허용 상한선을 홀로 위반하여 차단기 트립을 초래한 분전반 식별 기호(pdu01, pdu02, pdu03)를 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 5,
        "title": "Zalgo Text (글자 깨짐)",
        "filename": "",
        "verify_hash": "",
        "narrative": "정전된 터미널이 비상 UPS 라인으로 임시 구동되었으나, 메모리 버퍼 영역 전체가 완전히 깨진 특수문자 노이즈로 덮여 복구가 난해한 상황입니다.",
        "dialogue_list": [
            {
                "speaker": "이재헌 과장",
                "role": "서버 담당 (가상화 엔지니어)",
                "avatar": "avatar_lee_jh.png",
                "text": "큰일났습니다. 정전 여파로 콘솔 버퍼가 심각하게 훼손되어 원천 데이터 파악이 완전히 막혔습니다."
            },
            {
                "speaker": "박재욱 차장",
                "role": "DBA (울분을 토하는 실무자)",
                "avatar": "avatar_park_jw.png",
                "text": "이 과장님, 정신 차리세요! 보안 커널이 복구 세션 수립을 위해 '현재 시스템의 작동 불량 상태'를 지칭하는 영문 대문자 3글자 상태 플래그 입력을 요구하고 있습니다!"
            },
            {
                "speaker": "이재헌 과장",
                "role": "서버 담당 (가상화 엔지니어)",
                "avatar": "avatar_lee_jh.png",
                "text": "아! 시스템이 다운되어 작동이 '나쁜(불량)' 상태에 직면했음을 뜻하는 대표적인 영어 대문자 3글자 단어(B _ _)군요. 아스키 코드 레퍼런스 표에서 그 10진수 값을 찾아 순서대로 나열하여 입력합시다!"
            }
        ],
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⚠️ CORRUPTED STRING BUFFER</div>\n    <div class='zalgo-box' style='font-family: var(--font-sans); font-size: 1.4rem; text-align: center; padding: 20px; color: var(--text-primary);'>\n        #$@%&amp;* #$@%&amp;* SYSTEM_LOCKED *&amp;%@$# *&amp;%@$#\n    </div>\n    <div style='margin-top: 15px; text-align: center;'>\n        <p style='color: var(--accent-blue); font-size: 0.85rem; margin-bottom: 8px; font-family: var(--font-title);'>📖 ASCII REFERENCE CHART</p>\n        <img src='ascii_table.png' alt='ASCII Code Table' style='max-width: 100%; border: 1px solid var(--border-color); border-radius: 6px; box-shadow: 0 0 15px rgba(0,229,255,0.15);'>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.5;'>\n        힌트: 시스템의 오작동 및 불량 상태를 의미하는 영문 대문자 3글자 단어(B _ _)의 아스키 10진수 코드값을 표에서 순서대로 찾아 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 6,
        "title": "System Halt Signal (시스템 종료 명령어)",
        "filename": "",
        "verify_hash": "",
        "narrative": "비상 전원 하에서 콘솔 메모리 버퍼가 복구되자, 권남훈 파트장이 사고 서버의 OS Syslog에서 정전 발생 직전 시각(01시 58분)에 구동된 결정적인 기동 중단 감사 흔적을 관측해 냅니다.",
        "dialogue_list": [
            {
                "speaker": "권남훈 파트장",
                "role": "운영총괄 (예민한 리더)",
                "avatar": "avatar_kwon_nh.png",
                "text": "박 파트장, 이 로그를 보십시오! 셧다운 감사 시각인 01시 58분, 누군가가 root 권한 세션을 획득해 프로세스 가동을 강제로 차단하고 커널을 Halt시키는 바이너리를 호출했습니다. 이건 고의적인 테러입니다!"
            },
            {
                "speaker": "박용철 파트장",
                "role": "품질총괄 (규정 맹신자)",
                "avatar": "avatar_park_yc.png",
                "text": "단순 장비 노후화로 인한 전원 서지일 수도 있습니다. 정밀 규격부터 맞춰 대조하시죠."
            },
            {
                "speaker": "권남훈 파트장",
                "role": "운영총괄 (예민한 리더)",
                "avatar": "avatar_kwon_nh.png",
                "text": "우길 걸 우겨야지! 공격자가 서버 자체를 완전히 정지시키기 위해 실행한 UNIX/Linux 표준 시스템 종료 명령어(영문 소문자 8자)를 식별하십시오!"
            }
        ],
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⚙️ UNIX/Linux SYSTEM LOG DUMP</div>\n    <div style='background: rgba(0,0,0,0.6); padding: 15px; border-radius: 6px; border: 1px solid var(--border-color); font-family: var(--font-mono); font-size: 0.9rem; line-height: 1.6; color: var(--text-primary); text-align: left;'>\n        <span style='color: var(--text-muted);'>[Jul 21 01:58:05] authpriv.info sudo: root : TTY=pts/0 ; PWD=/ ; USER=root ; COMMAND=/sbin/shutdown</span><br>\n        <span style='color: var(--accent-magenta);'>[Jul 21 01:58:08] kern.info kernel: System is going down for halt NOW!</span><br>\n        <span style='color: var(--accent-red);'>[Jul 21 01:58:10] systemd[1]: Sent signal SIGTERM to all processes...</span>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.5;'>\n        힌트: `/sbin/` 경로 하위에서 호출되어 운영체제를 강제 종료시키는 대표적인 8글자 Linux 표준 명령어(영문 소문자)를 식별하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 7,
        "title": "CPU Overload PID (악성 프로세스 PID 추적)",
        "filename": "",
        "verify_hash": "",
        "narrative": "강제 종료 명령어가 호출되기 바로 직전, 물리 서버 자원을 강제로 고갈시켜 인프라 응답 불능 상태를 유도한 백그라운드 공격 프로세스의 활성 기록이 발견됩니다.",
        "dialogue_list": [
            {
                "speaker": "권남훈 파트장",
                "role": "운영총괄 (예민한 리더)",
                "avatar": "avatar_kwon_nh.png",
                "text": "이재헌 과장! 서버가 강제 종료되기 직전에 CPU를 98% 이상 과독점하며 인프라 마비를 유도한 백그라운드 프로세스가 기동 중이었습니다. 평소에 프로세스 모니터링도 안 하고 뭐 한 겁니까!"
            },
            {
                "speaker": "이재헌 과장",
                "role": "서버 담당 (가상화 엔지니어)",
                "avatar": "avatar_lee_jh.png",
                "text": "억울합니다 파트장님! 당시 결산 배치 스레드 외에는 특별한 명령을 인가한 적이 없습니다. 시스템의 정상 부하 분산 범위였습니다."
            },
            {
                "speaker": "권남훈 파트장",
                "role": "운영총괄 (예민한 리더)",
                "avatar": "avatar_kwon_nh.png",
                "text": "입 다물고 당시 CPU 점유율을 비정상적으로 과점하며 시스템 리소스를 잠식한 주범 프로세스의 PID(프로세스 ID) 4자리를 프로세스 활성 로그(top/ps)에서 식별하십시오!"
            }
        ],
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🖥️ OS ACTIVE PROCESS MONITOR (TOP/PS DUMP)</div>\n    <div style='max-height: 200px; overflow-y: auto; border: 1px solid var(--border-color); border-radius: 4px; background: rgba(0,0,0,0.45); text-align: left;'>\n        <table style='width: 100%; border-collapse: collapse; font-family: var(--font-mono); font-size: 0.8rem; color: var(--text-primary);'>\n            <tr style='position: sticky; top: 0; background: #080b11; color: var(--accent-blue); border-bottom: 1px solid var(--border-color); font-weight: bold;'>\n                <th style='padding: 6px;'>PID</th>\n                <th style='padding: 6px;'>USER</th>\n                <th style='padding: 6px;'>%CPU</th>\n                <th style='padding: 6px;'>%MEM</th>\n                <th style='padding: 6px;'>COMMAND</th>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1024</td>\n                <td style='padding: 5px 6px;'>systemd</td>\n                <td style='padding: 5px 6px;'>0.1%</td>\n                <td style='padding: 5px 6px;'>0.2%</td>\n                <td style='padding: 5px 6px;'>/usr/lib/systemd/systemd</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1028</td>\n                <td style='padding: 5px 6px;'>kthreadd</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>[kthreadd]</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1035</td>\n                <td style='padding: 5px 6px;'>kworker/0</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>[kworker/0:1H]</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1124</td>\n                <td style='padding: 5px 6px;'>journald</td>\n                <td style='padding: 5px 6px;'>0.2%</td>\n                <td style='padding: 5px 6px;'>1.5%</td>\n                <td style='padding: 5px 6px;'>/usr/lib/systemd/systemd-journald</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1180</td>\n                <td style='padding: 5px 6px;'>dbus</td>\n                <td style='padding: 5px 6px;'>0.1%</td>\n                <td style='padding: 5px 6px;'>0.4%</td>\n                <td style='padding: 5px 6px;'>/usr/bin/dbus-daemon --system</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1202</td>\n                <td style='padding: 5px 6px;'>rsyslogd</td>\n                <td style='padding: 5px 6px;'>0.1%</td>\n                <td style='padding: 5px 6px;'>0.8%</td>\n                <td style='padding: 5px 6px;'>/usr/sbin/rsyslogd -n</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1240</td>\n                <td style='padding: 5px 6px;'>sshd</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>0.6%</td>\n                <td style='padding: 5px 6px;'>/usr/sbin/sshd -D</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>2109</td>\n                <td style='padding: 5px 6px;'>oracle</td>\n                <td style='padding: 5px 6px;'>0.5%</td>\n                <td style='padding: 5px 6px;'>12.4%</td>\n                <td style='padding: 5px 6px;'>oracleHIS (LOCAL=NO)</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>2120</td>\n                <td style='padding: 5px 6px;'>oracle</td>\n                <td style='padding: 5px 6px;'>0.2%</td>\n                <td style='padding: 5px 6px;'>8.5%</td>\n                <td style='padding: 5px 6px;'>ora_pmon_HIS</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>3120</td>\n                <td style='padding: 5px 6px;'>tqo_ops</td>\n                <td style='padding: 5px 6px;'>1.2%</td>\n                <td style='padding: 5px 6px;'>2.1%</td>\n                <td style='padding: 5px 6px;'>python3 diagnostics.py</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>3211</td>\n                <td style='padding: 5px 6px;'>nginx</td>\n                <td style='padding: 5px 6px;'>0.1%</td>\n                <td style='padding: 5px 6px;'>1.2%</td>\n                <td style='padding: 5px 6px;'>nginx: worker process</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>3212</td>\n                <td style='padding: 5px 6px;'>nginx</td>\n                <td style='padding: 5px 6px;'>0.1%</td>\n                <td style='padding: 5px 6px;'>1.2%</td>\n                <td style='padding: 5px 6px;'>nginx: worker process</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>4081</td>\n                <td style='padding: 5px 6px;'>root</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>0.3%</td>\n                <td style='padding: 5px 6px;'>/usr/sbin/crond -n</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>5102</td>\n                <td style='padding: 5px 6px;'>postfix</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>0.5%</td>\n                <td style='padding: 5px 6px;'>/usr/libexec/postfix/master</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>5250</td>\n                <td style='padding: 5px 6px;'>unknown</td>\n                <td style='padding: 5px 6px;'>98.7%</td>\n                <td style='padding: 5px 6px;'>84.2%</td>\n                <td style='padding: 5px 6px;'>/tmp/dummy_exploit_daemon</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>5301</td>\n                <td style='padding: 5px 6px;'>root</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>[kworker/u2:2]</td>\n            </tr>\n            <tr>\n                <td style='padding: 5px 6px;'>5420</td>\n                <td style='padding: 5px 6px;'>tqo_ops</td>\n                <td style='padding: 5px 6px;'>0.3%</td>\n                <td style='padding: 5px 6px;'>1.0%</td>\n                <td style='padding: 5px 6px;'>bash</td>\n            </tr>\n        </table>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 12px; line-height: 1.5;'>\n        힌트: CPU 자원을 비정상적으로 98% 이상 독점 점유하고 있는 범인 프로세스의 PID 4자리를 표에서 찾아 입력하십시오. (필요 시 테이블 스크롤 가능)\n    </p>\n</div>"
    },
    {
        "stage": 8,
        "title": "Governance (IT 거버넌스 규정)",
        "filename": "",
        "verify_hash": "",
        "narrative": "악성 프로세스 구동 정황이 밝혀지며 긴급 조치가 전개되자, 품질총괄 박용철 파트장이 수사 절차의 공식 IT 서비스 거버넌스 등록을 완강히 요구하고 나섭니다.",
        "dialogue_list": [
            {
                "speaker": "박용철 파트장",
                "role": "품질총괄 (규정 맹신자)",
                "avatar": "avatar_park_yc.png",
                "text": "정형화된 절차를 우회하는 임의 조사는 명백한 규정 위반입니다. 장애 상황 관리 시에는 임시 조치 단계부터 근본 문제(Problem)를 정식 식별하여 등록해야 합니다."
            },
            {
                "speaker": "권남훈 파트장",
                "role": "운영총괄 (예민한 리더)",
                "avatar": "avatar_kwon_nh.png",
                "text": "박 파트장, 이 난리에 거버넌스 절차가 밥을 먹여줍니까? 당장 문제 해결이 우선이지!"
            },
            {
                "speaker": "박용철 파트장",
                "role": "품질총괄 (규정 맹신자)",
                "avatar": "avatar_park_yc.png",
                "text": "무작정 들쑤시는 건 장애를 더 키울 뿐입니다. 품질 보증 표준 프로세스를 승인하기 위해, 사내 거버넌스가 따르는 정식 IT 서비스 관리 프레임워크의 영문 소문자 4글자 약어를 터미널에 입력하십시오."
            }
        ],
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>📚 IT SERVICE GOVERNANCE FRAMEWORK</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;'>\n        힌트: 정보 기술 인프라 라이브러리(IT Infrastructure Library)의 영문 앞글자들을 딴 4글자 약어로, 전 세계 IT 부서의 표준 운영 가이드라인입니다.\n    </p>\n</div>"
    },
    {
        "stage": 9,
        "title": "Physical Device Map (물리 인프라 맵 감사)",
        "filename": "",
        "verify_hash": "",
        "narrative": "장애 수사가 정식 인시던트로 등록되자, DBA 박재욱 차장이 데이터베이스 스토리지 연결망의 물리적 단절(I/O error)을 주장하며 품질총괄 박용철 파트장에게 결선 상태 조사를 긴급 요구합니다.",
        "dialogue_list": [
            {
                "speaker": "박재욱 차장",
                "role": "DBA (억울한 실무자)",
                "avatar": "avatar_park_jw.png",
                "text": "박 파트장님, WAS 셧다운 직전에 금융 DB 스토리지 동기화 데몬이 I/O 디스크 오류로 끊겼습니다. 이건 제 쿼리 작업 실수가 아니라 백업 스토리지 물리망 연결 장치 자체의 단절입니다!"
            },
            {
                "speaker": "박용철 파트장",
                "role": "품질총괄 (규정 맹신자)",
                "avatar": "avatar_park_yc.png",
                "text": "스토리지망 물리적 단절이라고요? 김 차장, 박 차장 말이 사실인지 검증해야겠네. 티켓 조회를 기동할 테니 스토리지 장비가 보관된 랙 번호 2자리(Rack ID)와 결선된 스위치 포트 번호 2자리(Port ID)를 조합한 4자리 물리 감사 코드를 대조해 보게."
            },
            {
                "speaker": "김진혁 차장",
                "role": "네트워크 담당 (능글맞은 엔지니어)",
                "avatar": "avatar_kim_jh.png",
                "text": "물리 결선 정보 대장은 기계실 콘솔 단말의 배치 맵과 광 스위치 포트 로그를 대조해 보면 바로 나옵니다. 랙 ID(2자리)와 포트(2자리)를 합친 4자리 감사 코드를 입력하시면 즉시 스위치 상태를 모니터링하겠습니다."
            }
        ],
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⚙️ PHYSICAL SERVER ROOM RACK MAP</div>\n    <div class='ascii-diagram' style='text-align: left; font-size: 0.8rem; line-height: 1.5; background: rgba(0,0,0,0.5); padding: 12px; border-radius: 6px; border: 1px solid var(--border-color); color: var(--text-primary);'>\n+-------------------------------------------------------------+\n|  [SERVER ROOM ZONE A - RACK ARRANGEMENT]                    |\n|                                                             |\n|  [Rack 80] : L4 load balancer VIP suite                     |\n|  [Rack 81] : Financial Core WAS clusters (01-08)            |\n|  [Rack 82] : SAN Storage Target controller units            |\n|  [Rack 83] : Oracle RAC database engine nodes               |\n+-------------------------------------------------------------+\n    </div>\n    \n    <div class='puzzle-title' style='margin-top: 15px;'>📡 SWITCH ROUTER PORT INTERFACE LOG</div>\n    <div style='background: rgba(0,0,0,0.6); padding: 12px; border-radius: 6px; border: 1px solid var(--border-color); font-family: var(--font-mono); font-size: 0.8rem; line-height: 1.6; text-align: left; color: var(--text-primary);'>\n        [Port 01] - LINK UP   - target: Core-WAS-Switch<br>\n        [Port 02] - LINK UP   - target: Enterprise-Backbone<br>\n        [Port 03] - LINK DOWN - target: Internal-VDI-Hub<br>\n        [Port 04] - LINK UP   - target: SAN-Storage-Fibre-Switch\n    </div>\n    \n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 12px; line-height: 1.5;'>\n        힌트: 배치 맵에서 'SAN Storage' 장비가 속한 랙 번호 2자리와 스위치 로그에서 'SAN-Storage-Fibre-Switch'가 결선된 포트 번호 2자리를 찾아 차례대로 조합하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 10,
        "title": "The Cronjob (Crontab 스케줄링)",
        "filename": "",
        "verify_hash": "",
        "narrative": "스토리지 단절 시점과 백업 작업 동작 시각이 겹친다는 네트워크 담당 김진혁 차장의 주장에 대해, DBA 박재욱 차장은 백업이 임의 수동 조작이 아닌 정상적인 예약 배치 스케줄러 기동이었음을 밝혀내려 합니다.",
        "dialogue_list": [
            {
                "speaker": "김진혁 차장",
                "role": "네트워크 담당 (능글맞은 엔지니어)",
                "avatar": "avatar_kim_jh.png",
                "text": "스토리지 장애 핑계를 대고 있지만, 실상은 박 차장이 승인받지 않은 무거운 수동 백업 명령을 날려 디스크를 폭사시킨 겁니다. 로그가 말해주고 있습니다."
            },
            {
                "speaker": "박재욱 차장",
                "role": "DBA (울분을 토하는 실무자)",
                "avatar": "avatar_park_jw.png",
                "text": "김 차장님, 무슨 헛소립니까! 전 수동으로 명령을 친 적이 없습니다! 스케줄러가 정해진 시간에 작동했을 뿐입니다."
            },
            {
                "speaker": "김진혁 차장",
                "role": "네트워크 담당 (능글맞은 엔지니어)",
                "avatar": "avatar_kim_jh.png",
                "text": "그래요? 타겟 서버의 크론탭(Crontab) 스케줄링 설정 데이터를 분석해 보면 진실이 밝혀지겠지요. 이 배치 스크립트가 기동되도록 예약되어 있던 매일 정기 시각(24시간 형식 4자리 HHMM)을 도출해 검증해 봅시다."
            }
        ],
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⏰ TARGET CRONTAB CONFIGURATION</div>\n    <div style='background: #020306; font-family: var(--font-mono); padding: 15px; border-radius: 6px; border: 1px solid var(--border-color); text-align: center; font-size: 1.1rem; color: var(--accent-blue);'>\n        45 1 * * * /usr/sbin/backup.sh\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.5;'>\n        힌트: 크론탭 시간 설정 구조는 [분] [시] [일] [월] [요일] 순서입니다.\n        위 설정은 매일 '1시 45분'에 구동됨을 의미합니다. 포맷에 맞춰 4자리 숫자로 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 11,
        "title": "The Privilege Role (권한 롤 식별)",
        "filename": "",
        "verify_hash": "",
        "narrative": "정상적인 백업 배치 기동이었음이 실증되자, WAS 담당 박주암 과장이 명령어 이력에서 또 다른 결정적인 모순을 포착합니다. 자동 백업 도중 누군가 관리자 권한을 도용해 최고 권한 DB 관리 롤로 강제 종료를 호출한 것입니다.",
        "dialogue_list": [
            {
                "speaker": "박주암 과장",
                "role": "WAS 담당 (실무 운영자)",
                "avatar": "avatar_park_ja.png",
                "text": "백업 배치 과부하 때문에 죽은 게 아닙니다! 단말기 명령어 히스토리를 보니 셧다운 직전인 01시 58분경, 누군가 제 WAS 관리자 ID를 무단 도용해 DB 관리 클라이언트를 실행했습니다!"
            },
            {
                "speaker": "김진혁 차장",
                "role": "네트워크 담당 (능글맞은 엔지니어)",
                "avatar": "avatar_kim_jh.png",
                "text": "침입 흔적이라고요? WAS 서버 권한 관리를 헐겁게 한 박 과장님의 과실 아닙니까?"
            },
            {
                "speaker": "박주암 과장",
                "role": "WAS 담당 (실무 운영자)",
                "avatar": "avatar_park_ja.png",
                "text": "그건 차차 규명할 일이고, 침입자가 데이터베이스를 강제로 즉시 종료시키기(SHUTDOWN IMMEDIATE) 위해 무단 도용한 이 오라클 최고 권한 관리자 롤(Role) 명칭(영문 소문자 6자)을 식별하십시오!"
            }
        ],
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>💻 INCIDENT COMMAND HISTORY DUMP</div>\n    <p style='font-family: var(--font-mono); color: var(--text-primary); font-size: 0.95rem; line-height: 1.6;'>\n        $ cd /u01/app/oracle/product/12.1.0/dbhome_1/bin<br>\n        $ ./sqlplus / as [ MASKED_ROLE ]<br>\n        &gt; SHUTDOWN IMMEDIATE;<br>\n        <span style='color: var(--accent-red);'>[01:58:21] DISCONNECTED FROM DATABASE.</span>\n    </p>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.5;'>\n        힌트: 데이터베이스의 커널 상태를 직접 제어하고 종료하기 위해 사용하는 오라클의 대표적인 최고 시스템 권한 관리자 롤 명칭(영문 소문자 6자)을 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 12,
        "title": "The Encryption Shell (보안 접속 프로토콜)",
        "filename": "",
        "verify_hash": "",
        "narrative": "누군가 무단으로 데이터베이스 클라이언트를 인가한 시각, 네트워크 담당 김진혁 차장은 본인이 휴게실에서 안전하게 switch 콘솔 원격 접속을 기동하고 있었다고 강변하지만 보안 정책적 모순이 드러납니다.",
        "dialogue_list": [
            {
                "speaker": "김진혁 차장",
                "role": "네트워크 담당 (능글맞은 엔지니어)",
                "avatar": "avatar_kim_jh.png",
                "text": "장애 시각, 저는 휴게실에서 보안 규정 준수 하에 switch 원격 접속을 위해 비암호화 프로토콜인 telnet을 통해 모니터링을 돌리고 있었습니다. 접속은 지극히 양호했습니다."
            },
            {
                "speaker": "권남훈 파트장",
                "role": "운영총괄 (예민한 리더)",
                "avatar": "avatar_kwon_nh.png",
                "text": "거짓말 마십시오! 평문으로 계정이 노출되는 telnet 접속은 사내 인프라 관리 보안 지침상 전사 장비에서 완전 차단되어 있습니다!"
            },
            {
                "speaker": "권남훈 파트장",
                "role": "운영총괄 (예민한 리더)",
                "avatar": "avatar_kwon_nh.png",
                "text": "스위치 제어를 위해 오직 포트 22번으로만 개방되어 작동하는 암호화 원격 터미널 접속 표준 보안 프로토콜 규격(영문 소문자 3자)을 파악하여 김 차장의 진술 모순을 실증하십시오!"
            }
        ],
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🌐 HIS INFRASTRUCTURE SECURITY POLICY</div>\n    <div class='ascii-diagram' style='text-align: left; font-size: 0.8rem; line-height: 1.5; background: rgba(0,0,0,0.5); padding: 12px; border-radius: 6px; border: 1px solid var(--border-color); color: var(--text-primary);'>\n+------------------------------------------------+\n|  [HIS INFRASTRUCTURE SECURITY STANDARD v4.2]   |\n|                                                |\n|  * REMOTE CONSOLE PRIVILEGE:                   |\n|    - Telnet (Port 23) : [ DISABLED / BLOCK ]   |\n|    - ???    (Port 22) : [ ENABLED / REQUIRED ] |\n|                                                |\n|  * Policy Rule: All administrative sessions    |\n|    must be encrypted using secure shell.       |\n+------------------------------------------------+\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.6;'>\n        김진혁 차장의 주장: 'telnet 통신(평문 전송)을 사용해 스위치에 정상 원격 접속했다.'<br>\n        보안 표준 명세: telnet은 엄격 차단, 포트 22번을 점유하는 이 프로토콜만 보안상 개방됨.<br>\n        사내 정책에 의거해 강제 적용되는 암호화 원격 접속 프로토콜 규격 명칭(영문 소문자 3자)을 기입하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 13,
        "title": "The Server Overload (서버 과부하 발생)",
        "filename": "",
        "verify_hash": "",
        "narrative": "네트워크 무선 거짓 진술이 발각된 와중, 서버 담당 이재헌 과장이 가상화 서버 자원 분배는 지극히 풍부하고 넉넉한 상태였다고 다급히 주장하기 시작합니다.",
        "dialogue_list": [
            {
                "speaker": "이재헌 과장",
                "role": "서버 담당 (가상화 엔지니어)",
                "avatar": "avatar_lee_jh.png",
                "text": "물리 서버 자원은 평소에 아주 풍부하게 할당해 두어 넉넉한 상태였습니다. 자원 부족으로 죽은 게 절대 아닙니다!"
            },
            {
                "speaker": "권남훈 파트장",
                "role": "운영총괄 (예민한 리더)",
                "avatar": "avatar_kwon_nh.png",
                "text": "이 과장님, 메인 WAS 인스턴스의 자원 상태 명세를 보십시오. CPU 점유율이 99.6%에 육박해 여유 마진이 0.4%밖에 남지 않았습니다!"
            },
            {
                "speaker": "권남훈 파트장",
                "role": "운영총괄 (예민한 리더)",
                "avatar": "avatar_kwon_nh.png",
                "text": "CPU 점유율이 임계치를 초과하여 시스템의 동작이 심각하게 마비되거나 다운되는 '치명적 과부하' 상태를 일컫는 대표적인 IT 용어(영문 소문자 8자)를 기입하십시오!"
            }
        ],
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⚙️ VM INSTANCE SPECIFICATION OVERVIEW</div>\n    <div class='cpu-widget'>\n        <div>INSTANCE_NAME: Core-WAS-01</div>\n        <div class='cpu-bar'>CPU USAGE: [██████████] 99.6% ( MASKED )</div>\n        <div style='color: var(--accent-magenta); margin-top: 5px;'>AVAILABLE_MARGIN: 0.4%</div>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.6;'>\n        CPU 여유 마진이 0.4%밖에 되지 않는 위태로운 상태입니다.<br>\n        시스템 자원이 허용 한도를 초과해 극도의 과부하에 직면한 상태를 뜻하는 영문 소문자 8자 단어를 기입하십시오.<br>\n        <strong style='color: var(--accent-blue);'>힌트: '위(Over)'에 '짐(Load)'을 과도하게 실어 인프라가 감당할 수 없는 한계 상태를 의미하는 8글자 합성어(O로 시작)입니다. 도로 위의 과적 차량을 표현할 때도 널리 쓰이는 용어입니다.</strong>\n    </p>\n</div>"
    },
    {
        "stage": 14,
        "title": "The Motivation (권남훈 총괄)",
        "filename": "",
        "verify_hash": "",
        "narrative": "극심한 자원 고갈 속에서 스토리지 단절이 덮쳐옴에 따라 발생한 데이터베이스 내부의 치명적 무결성 깨짐(Block Corruption) 오류 코드가 식별됩니다. 범인은 이 심각한 장애 원인을 덮고 책임을 회피하기 위해 강제 셧다운을 내린 동기가 포착됩니다.",
        "dialogue_list": [
            {
                "speaker": "권남훈 파트장",
                "role": "운영총괄 (예민한 리더)",
                "avatar": "avatar_kwon_nh.png",
                "text": "리소스 부족 상태에서 스토리지 물리 볼륨이 통째로 이탈하며 DB에 복구 불가능한 블록 깨짐 흔적이 터졌습니다. 이 치명적인 내부 감사 오류 코드를 특정하십시오."
            },
            {
                "speaker": "박용철 파트장",
                "role": "품질총괄 (규정 맹신자)",
                "avatar": "avatar_park_yc.png",
                "text": "정규표현식 패턴 필터링을 사용하면 감사 로그 상의 오류 코드를 정확히 식별해 낼 수 있겠군요."
            },
            {
                "speaker": "권남훈 파트장",
                "role": "운영총괄 (예민한 리더)",
                "avatar": "avatar_kwon_nh.png",
                "text": "그렇습니다. 제시된 정규표현식 검출 필터를 로그 덤프에 매칭해, 디스크 파손을 유발한 오라클 내부의 치명적 에러 코드 명칭을 소문자로 기입하십시오."
            }
        ],
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔍 CORRUPTION PATTERN DETECTION FILTER</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-bottom: 12px; line-height: 1.5;'>\n        아래 로그 덤프에서 정규식 패턴 <strong>^[A-Za-z]+-[0-9]{{5}}$</strong> 에 완벽히 부합하는 오라클 치명적 오류 코드를 식별하여 소문자로 입력하십시오.\n    </p>\n    <ul style='list-style-type: square; padding-left: 20px; font-size: 0.85rem; line-height: 1.8; color: var(--text-primary); font-family: var(--font-mono); text-align: left;'>\n        <li>sys-info-10023</li>\n        <li>ORA-9941</li>\n        <li>ERR-DB-CONN-5020</li>\n        <li>ORA-00600</li>\n        <li>oracle-752119</li>\n    </ul>\n</div>"
    },
    {
        "stage": 15,
        "title": "The VDI Rule (박용철 총괄)",
        "filename": "",
        "verify_hash": "",
        "narrative": "무단 종료 접속이 기록된 IP가 DBA 박재욱 차장의 VDI 할당 IP로 밝혀지자, 박용철 파트장이 VDI 세션 종료 즉시 수행되는 IP 회수 정책의 메커니즘을 들어 IP 도용 가능성을 진단합니다.",
        "dialogue_list": [
            {
                "speaker": "박용철 파트장",
                "role": "품질총괄 (규정 맹신자)",
                "avatar": "avatar_park_yc.png",
                "text": "VDI 보안 정책 하에서는 타인의 IP를 탈취해 무단 상주하는 행위가 원천 불가능합니다. 사용자가 세션을 종료하는 즉시 할당되어 있던 사설 IP 주소는 풀에 회수되며 즉각 다른 사람에게 순차 배분됩니다."
            },
            {
                "speaker": "박재욱 차장",
                "role": "DBA (울분을 토하는 실무자)",
                "avatar": "avatar_park_jw.png",
                "text": "박 파트장님, 만약 로그아웃된 IP가 즉시 공격자에게 재할당되어 악용되었다면 주소 도용이 성립할 수도 있는 것 아닙니까?"
            },
            {
                "speaker": "박용철 파트장",
                "role": "품질총괄 (규정 맹신자)",
                "avatar": "avatar_park_yc.png",
                "text": "음... 그렇다면 IP 주소의 동적 배분을 담당하는 이 자동 할당 네트워크 규약 약어(H C P D)의 아나그램을 풀어 회수 규칙의 맹점을 추론해 보십시오."
            }
        ],
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔌 PROTOCOL PORT CHECK: iSCSI TARGET</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;'>\n        힌트: 인터넷 소형 컴퓨터 시스템 인터페이스(iSCSI) 통신 프로토콜이 표준으로 점유하여 사용하는 포트 번호입니다.\n    </p>\n</div>"
    },
    {
        "stage": 16,
        "title": "Subnet Mistake (김진혁의 실수 1)",
        "filename": "",
        "verify_hash": "",
        "narrative": "스토리지 물리 단절의 근본 원인을 파악하기 위해 네트워크 라우터 콘솔 로그를 파고든 결과, 네트워크 담당 김진혁 차장이 설정 변경 중 대역폭 마스크를 잘못 격리하여 스토리지가 끊겨나간 결정적인 조작 실책이 발각됩니다.",
        "dialogue_list": [
            {
                "speaker": "권남훈 파트장",
                "role": "운영총괄 (예민한 리더)",
                "avatar": "avatar_kwon_nh.png",
                "text": "김진혁 차장! 장애 30분 전, 백업망 라우팅 대역 테이블을 임의 조작하다가 CIDR 서브넷 마스크 대역 폭을 `/28` 로 잘못 격리했더군요. 이것 때문에 스토리지 물리 볼륨 통신이 모조리 끊긴 겁니다!"
            },
            {
                "speaker": "김진혁 차장",
                "role": "네트워크 담당 (능글맞은 엔지니어)",
                "avatar": "avatar_kim_jh.png",
                "text": "아... 단순 라우팅 경로 복구를 위한 테스트 단계에서 비트 연산 실수로 오설정이 들어간 모양입니다. 의도한 것은 아닙니다."
            },
            {
                "speaker": "권남훈 파트장",
                "role": "운영총괄 (예민한 리더)",
                "avatar": "avatar_kwon_nh.png",
                "text": "변명은 필요 없고, 서브넷 마스크 `/28` 등급 대역에서 예약 주소 2개를 제외하고 실제 내부 장비들에 유효하게 분배할 수 있는 최대 호스트 IP 개수를 산출해 보십시오!"
            }
        ],
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔢 CIDR SUBMETMASK SUITE: /28</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; line-height: 1.6;'>\n        - 전체 IP 주소 표현 비트: 32비트<br>\n        - 호스트 할당 비트수: 32비트 - 28비트 = 4비트 (2^4 = 총 16개 주소)<br>\n        - 사용 불가 특수한 주소: 2개 (네트워크 ID 주소 & 브로드캐스트 IP)<br>\n        - <strong style='color: var(--accent-magenta);'>계산 공식: 2^(32 - 28) - 2</strong>\n    </p>\n</div>"
    },
    {
        "stage": 17,
        "title": "SAN Storage (김진혁의 실수 2)",
        "filename": "",
        "verify_hash": "",
        "narrative": "김 차장의 서브넷 오설정이 스토리지 통신 물리 단절을 유발하고, 그에 따른 ORA-00600 에러를 숨기고자 무단 종료를 유도했음이 최종 입증됩니다. DBA 박 차장은 격리된 스토리지 복구를 긴급히 독촉합니다.",
        "dialogue_list": [
            {
                "speaker": "박재욱 차장",
                "role": "DBA (울분을 토하는 실무자)",
                "avatar": "avatar_park_jw.png",
                "text": "김 차장님의 오설정으로 인해 제 결산 백업 중에 DB가 파손된 것이 밝혀졌습니다. 당장 끊긴 블록 스토리지 연결부터 긴급 복구해 주십시오!"
            },
            {
                "speaker": "김진혁 차장",
                "role": "네트워크 담당 (능글맞은 엔지니어)",
                "avatar": "avatar_kim_jh.png",
                "text": "크흠... 알겠습니다. 단순 실수였으니 바로 프로토콜 수동 연결 절차를 기동하겠습니다."
            },
            {
                "speaker": "박재욱 차장",
                "role": "DBA (울분을 토하는 실무자)",
                "avatar": "avatar_park_jw.png",
                "text": "iSCSI 프로토콜 통신 채널을 수동 결선하여 동작을 복구하기 위해, 해당 스토리지 장비가 기본 점유하여 사용하는 표준 TCP 포트 번호 4자리를 도출하십시오!"
            }
        ],
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔌 PROTOCOL PORT CHECK: iSCSI TARGET</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;'>\n        힌트: 인터넷 소형 컴퓨터 시스템 인터페이스(iSCSI) 통신 프로토콜이 표준으로 점유하여 사용하는 포트 번호입니다.\n    </p>\n</div>"
    },
    {
        "stage": 18,
        "title": "Time Drift (이재헌의 실수)",
        "filename": "",
        "verify_hash": "",
        "narrative": "스토리지 프로토콜 복구 선로를 재결선한 순간, 서버 담당 이재헌 과장이 셧다운 기록 분석을 뒤흔든 결정적인 시간 설정 결함(Time Drift)을 실토합니다.",
        "dialogue_list": [
            {
                "speaker": "이재헌 과장",
                "role": "서버 담당 (가상화 엔지니어)",
                "avatar": "avatar_lee_jh.png",
                "text": "파트장님, 대단히 죄송합니다! 인프라 증설 당시에 시간 동기화 데몬(NTP) 동작 설정을 수동으로 누락하여, WAS 서버들의 시스템 시간이 실제 세상 표준시보다 정확히 '15분 느리게' 가동 중인 것을 발견했습니다."
            },
            {
                "speaker": "권남훈 파트장",
                "role": "운영총괄 (예민한 리더)",
                "avatar": "avatar_kwon_nh.png",
                "text": "이 과장! 자네 진짜 제정신인가! 타임스탬프 동기화도 안 맞춰놓다니!"
            },
            {
                "speaker": "이재헌 과장",
                "role": "서버 담당 (가상화 엔지니어)",
                "avatar": "avatar_lee_jh.png",
                "text": "WAS의 감사 기록 상 셧다운 명령이 인가된 시각은 '01:58'입니다. 이 15분의 오차를 물리적으로 정상 환산하여 보정한, 실제 세상의 실제 셧다운 구동 표준 시각(24시간 형식 4자리 HHMM)을 도출해야 VDI 접속 이력 대조가 가능합니다!"
            }
        ],
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⏳ TIME SYNC DRIFT LOGS</div>\n    <ul style='list-style-type: square; padding-left: 20px; font-size: 0.85rem; line-height: 1.6; color: var(--text-primary);'>\n        <li>WAS 서버 기록 시각: 01:58 (서버 시계가 15분 느린 상태)</li>\n        <li>물리적 실제 표준 시각 = 서버 기록 시각 + 15분 오차 보정</li>\n        <li><strong style='color: var(--accent-magenta);'>요구 포맷: 4자리 디지털 형식 (예: 01시 10분 -> 0110)</strong></li>\n    </ul>\n</div>"
    },
    {
        "stage": 19,
        "title": "The Culprit (진범 도출)",
        "filename": "",
        "verify_hash": "",
        "narrative": "서버의 느린 클럭 오차를 보정한 진짜 셧다운 명령 구동 시간은 실제 시간 기준으로 정확히 '02:13'이었습니다. DBA 박재욱 차장은 '02:05'에 공식 로그아웃하여 세션을 해제하고 사용하던 IP를 이미 반납해 둔 상태였습니다.",
        "dialogue_list": [
            {
                "speaker": "박용철 파트장",
                "role": "품질총괄 (규정 맹신자)",
                "avatar": "avatar_park_yc.png",
                "text": "박 차장님이 02시 05분에 로그아웃하여 IP를 반납한 뒤, DHCP 재분배 규칙에 따라 그 IP는 즉각 풀에 회수되었겠군요."
            },
            {
                "speaker": "박재욱 차장",
                "role": "DBA (울분을 토하는 실무자)",
                "avatar": "avatar_park_jw.png",
                "text": "확실히 그렇습니다! 그리고 단 8분 뒤인 02시 13분에 누군가 제가 사용하던 그 똑같은 IP 주소를 DHCP 시스템을 통해 동적 할당받아 WAS 강제 셧다운 명령을 내렸습니다. 02시 13분에 그 IP로 접속해 있던 자가 진짜 범인입니다!"
            },
            {
                "speaker": "박용철 파트장",
                "role": "품질총괄 (규정 맹신자)",
                "avatar": "avatar_park_yc.png",
                "text": "당일 라우터의 무선(wifi) 신호로 접속하여 노트북으로 안전하게 모니터링 중이었다고 거짓 기술 진술을 한 인물이 범인으로 좁혀집니다. 그 진짜 범인의 이름을 기입하십시오."
            }
        ],
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔎 REAL-TIME TIMELINE COMPARISON</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;'>\n        누군가가 DHCP의 규약 허점을 이용하여 DBA 박 차장이 사용하다가 반납한 IP 주소를 곧바로 할당받아 악용한 물증을 확보했습니다.<br>\n        조직도 상의 진범 이름 3글자를 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 20,
        "title": "Ticket Closed (최종 결재)",
        "filename": "",
        "verify_hash": "",
        "narrative": "진범의 정체가 최종 확인되었습니다. OSPF 라우팅 오설정을 숨기기 위한 김진혁 차장의 전말이 드러납니다. 결국 공격자가 내세운 무선 모니터링이라는 하드웨어적 모순이 자가당착을 유발했습니다.",
        "dialogue_list": [
            {
                "speaker": "김진혁 차장",
                "role": "네트워크 담당 (능글맞은 엔지니어)",
                "avatar": "avatar_kim_jh.png",
                "text": "죄송합니다... 라우팅 CIDR 오설정 실수를 조용히 메우려다 일이 이렇게 커질 줄 몰랐습니다. 책임을 회피하기 위해 DBA 박 차장의 세션을 유도하고 WAS를 강제 정지시켰습니다."
            },
            {
                "speaker": "권남훈 파트장",
                "role": "운영총괄 (예민한 리더)",
                "avatar": "avatar_kwon_nh.png",
                "text": "본인 설정을 덮기 위해 코어 인프라를 마비시키고 동료에게 누명까지 씌우다니! 엄중한 처벌을 받게 될 겁니다."
            },
            {
                "speaker": "박용철 파트장",
                "role": "품질총괄 (규정 맹신자)",
                "avatar": "avatar_park_yc.png",
                "text": "장애 수사 및 음모 규명이 완료되었습니다. 최종 승인 확인 키 [ done ]를 기입하여 이 새벽의 장애 인시던트 티켓을 공식 클리어하고 종결 처리하십시오."
            }
        ],
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>✅ RESOLUTION REPORT APPROVAL</div>\n    <p style='color: var(--text-primary); font-size: 0.85rem; line-height: 1.6;'>\n        - 장애 명칭: Core WAS Shutdown Incident<br>\n        - 조치 상태: 진범 식별 완료 및 DBA 누명 해소<br>\n        - 최종 승인 코드: done\n    </p>\n</div>"
    }
]

# Canonical Game Passcodes (chained logic)
answers = [
    "179",
    "2321",
    "754",
    "pdu02",  
    "666568",
    "shutdown",
    "5250",
    "itil",
    "8204",
    "0145",
    "sysdba",  
    "ssh",  # Stage 12 new answer
    "overload",  # Stage 13 new answer
    "ora00600",
    "dhcp",
    "14",
    "3260",
    "0213",
    "김진혁",
    "done"
]

def get_sha256(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

# Dynamic pre-calculation of cryptographic filenames and verify_hashes
current_file = "a7f93b2c"  # Fixed Stage 1 entry name
for idx, ans in enumerate(answers):
    normalized_ans = "".join(ans.split()).lower()
    stages[idx]["verify_hash"] = get_sha256(normalized_ans)
    stages[idx]["filename"] = f"{current_file}.html"
    
    # Cascade hashing to build the deterministic link chain
    current_file = get_sha256(current_file + normalized_ans)[:8]

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
                <h1>OPERATION: BLACKOUT <span class="tqo-badge">장애조사관 CORE</span></h1>
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
                    <!-- 3rd-person neutral narrative text block -->
                    <div class="narrative-panel" style="background: rgba(0, 229, 255, 0.07); border-left: 4px solid var(--accent-blue); box-shadow: -5px 0 15px rgba(0, 229, 255, 0.15); padding: 16px; margin-bottom: 20px; font-size: 0.95rem; line-height: 1.6; color: var(--text-primary); border-radius: 0 6px 6px 0; font-family: var(--font-sans);">
                        <div style="font-family: var(--font-title); font-size: 0.75rem; color: var(--accent-blue); font-weight: bold; letter-spacing: 1px; margin-bottom: 8px; text-transform: uppercase;">📡 SITUATION BRIEFING</div>
                        <div style="white-space: pre-wrap; margin: 0; padding: 0;">{narrative}</div>
                    </div>

                    <!-- Pure character dialogue feed (KakaoTalk / Chat style list) -->
                    <div class="dialogue-feed-container" style="display: flex; flex-direction: column; gap: 12px;">
                        {dialogue_html}
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
                    <div class="terminal-title">investigator@his-system:~/incident_monitor</div>
                </div>

                <div class="terminal-body">
                    <div class="terminal-output">
                        <p class="system-log">HIS Incident Management Subsystem v1.0.4</p>
                        <p class="system-log">Loading kernel security context for Stage {stage_num:02d}...</p>
                        <p class="system-log">Ready. Enter decrypted passcode or entity key to route next file.</p>
                        <p style="color: var(--text-muted);">--------------------------------------------------------</p>
                    </div>

                    <div class="terminal-prompt">
                        <span class="prompt-symbol">[root@investigator-system ~]#</span>
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
                    <div style="color: var(--text-muted);">ASSIGNED OFFICER:</div><div style="color: var(--accent-blue); font-weight: bold;">장애조사관</div>
                    <div style="color: var(--text-muted);">ROOT CAUSE:</div><div>네트워크 담당 김진혁 차장의 OSPF 라우팅 오설정 은폐 공작. (DBA 누명 해소)</div>
                    <div style="color: var(--text-muted);">SLA IMPACT:</div><div style="color: var(--accent-green); font-weight: bold;">99.90% (KPI TARGET ACHIEVED)</div>
                    <div style="color: var(--text-muted);">STATUS:</div><div style="color: var(--accent-green);">CLOSED (SUCCESS)</div>
                </div>
            </div>

            <div style="text-align: left; line-height: 1.6; font-size: 0.9rem; margin-top: 10px;">
                <h3 style="font-family: var(--font-title); color: var(--accent-blue); margin-bottom: 10px;">🏆 장애조사관 종합 평가 등급</h3>
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
    # Build dialogue list HTML structure (KakaoTalk / Feed style with hidden default display)
    dialogue_html = ""
    for d in s["dialogue_list"]:
        if d["avatar"].endswith(".png"):
            card_avatar = f'<img src="{d["avatar"]}" alt="Suspect Avatar" style="width: 100%; height: 100%; object-fit: cover;">'
        else:
            card_avatar = f'<div class="avatar-placeholder" style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; background: rgba(0,229,255,0.1); border: 1px solid var(--border-color); border-radius: 4px; font-family: var(--font-mono); font-weight: bold; color: var(--accent-blue); font-size: 0.75rem;">{d["avatar"]}</div>'
            
        dialogue_html += f"""
        <div class="dialogue-card speaker-suspect" style="margin-bottom: 5px; display: none; gap: 15px; background: rgba(15, 61, 89, 0.12); border: 1px solid rgba(15, 61, 89, 0.35); border-radius: 8px; padding: 12px; border-left: 4px solid var(--accent-magenta);">
            <div class="avatar-container" style="flex-shrink: 0; width: 48px; height: 48px; border-radius: 4px; overflow: hidden; border: 1px solid var(--border-color);">
                {card_avatar}
            </div>
            <div class="dialogue-body" style="flex: 1; display: flex; flex-direction: column; gap: 4px;">
                <div class="dialogue-speaker" style="font-family: var(--font-title); font-size: 0.8rem; font-weight: bold; color: var(--accent-blue); display: flex; justify-content: space-between;">
                    <span>{d["speaker"]}</span>
                    <span class="speaker-role" style="font-size: 0.7rem; color: var(--text-muted);">{d["role"]}</span>
                </div>
                <div class="dialogue-text typing-text" data-text="{d["text"].replace('"', '&quot;')}" style="font-size: 0.88rem; line-height: 1.5; color: var(--text-primary); white-space: pre-wrap;">
                    {d["text"]}
                </div>
            </div>
        </div>
        """

    content = html_template.format(
        stage_num=s["stage"],
        stage_title=s["title"],
        verify_hash=s["verify_hash"],
        dialogue_html=dialogue_html,
        narrative=s["narrative"],
        gimmick_html=s["gimmick_html"]
    )
    with open(s["filename"], "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {s['filename']}")

# Write clear page (dynamic endpoint to match end-of-chain hash)
clear_filename = f"{current_file}.html"
with open(clear_filename, "w", encoding="utf-8") as f:
    f.write(clear_page_html)
print(f"Generated Clear Page: {clear_filename}")
print("All stages generated successfully.")
