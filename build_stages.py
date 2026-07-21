import os
import json

stages = [
    {
        "stage": 1,
        "title": "System Boot (F12)",
        "filename": "a7f93b2c.html",
        "verify_hash": "3068430da9e4b7a674184035643d9e19af3dc7483e31cc03b35f75268401df77",
        "speaker": "박용철 파트장",
        "role": "품질총괄 (예민한 리더)",
        "avatar": "avatar_park_yc.png",
        "dialogue": "금융 코어 WAS 서버가 알 수 없는 명령어로 강제 종료된 대형 장애 현장.\n부서장과 본부장의 압박 속에 박용철 파트장이 단말기 제어 콘솔을 켜고 다급히 움직이기 시작합니다.\n\n부팅 인가 코드가 막혀 있군요. 권남훈 파트장이 VDI 보안 정책을 잠가둔 모양인데,\n언제 정식 결재 올리고 승인 대기합니까! 당장 F12(개발자 도구)를 열어 소스코드의 백업용 주석 키를 찾아 로그인 절차를 돌파하십시오!",
        "gimmick_html": "<!-- KEY: 179 -->\n<div class='puzzle-container'>\n    <div class='puzzle-title'>🔒 ACCESS PROTECTION KEY</div>\n    <p style='color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;'>\n        인가 토큰이 보안 커널에 의해 물리 차단되었습니다.<br>\n        F12(개발자 도구)를 통해 HTML 소스코드의 주석을 분석하고 백업 마스터 키를 찾아 터미널에 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 2,
        "title": "Encrypted Packet (Base64)",
        "filename": "b4bcdd0d.html",
        "verify_hash": "f5334f59cc820a5c99fd2a5b5527884c821c19f1daa7c825368603aba61d6178",
        "speaker": "권남훈 파트장",
        "role": "운영총괄 (규정 맹신자)",
        "avatar": "avatar_kwon_nh.png",
        "dialogue": "터미널 부팅에 성공하자마자 권남훈 파트장이 다가와 방어적인 경고를 보냅니다.\n\n정식 승인 절차 없는 임의 시스템 조작은 심각한 규정 위반입니다.\n망의 무결성을 입증하기 위해, VDI 단말에 기록된 암호화 패킷 페이로드를 제공할 테니 이를 분석하십시오.\n\n제시된 Base64 데이터를 디코딩해 당시 WAS 서버가 사용한 백그라운드 사설 포트 번호를 입력하여 정식 인증 세션을 성립하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>📡 PACKET PAYLOAD DUMP</div>\n    <div style='display: flex; gap: 15px; align-items: center; justify-content: center; background: rgba(0,0,0,0.5); padding: 15px; border-radius: 4px;'>\n        <p style='font-family: var(--font-mono); color: var(--accent-magenta); font-size: 1.25rem; letter-spacing: 1px;'>UG9ydCAyMzIx</p>\n        <button class='copy-btn' onclick=\"copyToClipboard('UG9ydCAyMzIx', this)\">COPY</button>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.5;'>\n        힌트: Base64 형식으로 변환된 포트 정보 페이로드입니다.<br>\n        디코딩 시 문자 뒤에 기재된 숫자 4자리를 찾아 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 3,
        "title": "Log Flood (권한 검색)",
        "filename": "83e5e934.html",
        "verify_hash": "4099ed5ba70aebc5a9dc26bc2093d4b45839f99b306bd12f68cedfd351e6ab7a",
        "speaker": "박용철 파트장",
        "role": "품질총괄 (예민한 리더)",
        "avatar": "avatar_park_yc.png",
        "dialogue": "권남훈 파트장의 장담과 달리, 파일 배포 프로세스 상에 허점이 감지됩니다.\n\n권 파트장은 표준 rwxr-xr-x(755) 권한으로 배포했으니 무결하다고 강력히 주장합니다.\n하지만 그의 말은 신뢰하기 어렵습니다. 즉시 스토리지의 디렉토리 권한 감사 덤프를 전수 스캔하십시오.\n관리 소홀로 인해 쓰기 권한이 허용된 비정상 파일(rwxr-xr--)을 가려내야 합니다. 찾아내서 수치값으로 변환해 제출하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>📂 DIRECTORY PERMISSIONS SCAN</div>\n    <div class='log-flood-area'>\n" + "\n".join([f"        <div class='log-flood-line'>-rwxr-xr-x  1 tqo_ops  staff  4096 Jul 21 02:00 file_{i:03d}.bin</div>" if i != 273 else "        <div class='log-flood-line log-target'>-rwxr-xr--  1 tqo_ops  staff  8204 Jul 21 01:45 backup_corrupt.bin</div>" for i in range(500)]) + "\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.5;'>\n        힌트: 수백 줄의 리스트 속에서 무언가 다른 파일 하나가 숨어 있습니다.<br>\n        찾아낸 취약 마스크(rwxr-xr--) 값을 8진수 변환식(r=4, w=2, x=1, -=0 합산)에 대입하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 4,
        "title": "The Blackout (Hidden Text)",
        "filename": "13b3bfc6.html",
        "verify_hash": "7970f1f08c678259aa519bb1beaa3e57186a40b0c3fbfc572d37f874125d38fe",
        "speaker": "시스템 경고음",
        "role": "ALERT CONSOLE",
        "avatar": "CRT",
        "dialogue": "[위이이이잉- 삐- 삐-]\n\n서버실 내부의 전압 경보 장치가 작동하며 갑작스럽게 단말기 모니터 화면의 신호가 끊어집니다.\n모든 텍스트가 사라지고 서버실 내부가 어둠으로 물듭니다.\n\n누군가가 강제로 단말기 모니터 신호를 차단해 분석을 방해하려는 구동으로 추정됩니다.\n터미널 장치의 비상 자체 안전 장치에 의해, 화면 중앙 캔버스 어딘가에 마스크 처리된 복구 코드가 숨겨져 있습니다. 드래그(Ctrl+A)를 수행해 코드를 읽어내십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>💡 VISIBILITY RESTORATION OVERLAY</div>\n    <div class='hidden-text-container'>\n        <span class='hidden-error-text'>404500</span>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px;'>\n        드래그하여 숨겨진 에러 코드를 찾아 터미널에 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 5,
        "title": "Zalgo Text (글자 깨짐)",
        "filename": "48b42551.html",
        "verify_hash": "af4883c99558a3f6ef589d7e9a69585135ebac48f6b55c12e5e96849dc3707ee",
        "speaker": "이재헌 과장",
        "role": "서버 담당 (식은땀 흘리는 실무자)",
        "avatar": "avatar_lee_jh.png",
        "dialogue": "정전의 여파로 서버 콘솔 메모리 버퍼 영역 전체가 완전히 깨진 특수문자 노이즈로 덮여 복구가 난해해진 상황.\n\n정전 영향으로 콘솔 버퍼가 심각하게 훼손되어 원천 데이터 파악이 어렵습니다.\n하지만 보안 커널은 복구 세션 수립을 위해 '현재 시스템의 작동 불량 상태'를 지칭하는 영문 대문자 3글자 상태 플래그 입력을 요구하고 있습니다.\n시스템이 다운되어 작동이 '나쁜(불량)' 상태에 직면했음을 뜻하는 대표적인 영어 대문자 3글자 단어(B _ _)를 도출한 뒤, 아스키 코드 레퍼런스 표에서 10진수 값을 찾아 순서대로 나열하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⚠️ CORRUPTED STRING BUFFER</div>\n    <div class='zalgo-box' style='font-family: var(--font-mono); font-size: 1.25rem; letter-spacing: 2px; color: var(--accent-magenta); text-align: center; padding: 20px;'>\n        #$@%&amp;* #$@%&amp;* SYSTEM_LOCKED *&amp;%@$# *&amp;%@$#\n    </div>\n    <div style='margin-top: 15px; text-align: center;'>\n        <p style='color: var(--accent-blue); font-size: 0.85rem; margin-bottom: 8px; font-family: var(--font-title);'>📖 ASCII REFERENCE CHART</p>\n        <img src='ascii_table.png' alt='ASCII Code Table' style='max-width: 100%; border: 1px solid var(--border-color); border-radius: 6px; box-shadow: 0 0 15px rgba(0,229,255,0.15);'>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.5;'>\n        힌트: 시스템의 오작동 및 불량 상태를 의미하는 영문 대문자 3글자 단어(B _ _)의 아스키 10진수 코드값을 표에서 순서대로 찾아 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 6,
        "title": "System Halt Signal (시스템 종료 명령어)",
        "filename": "db590ac0.html",
        "verify_hash": "08434ba9cdf55a02284e2913400586cd289878e0f055f7bb0b07ce392caeb989",
        "speaker": "박용철 파트장",
        "role": "품질총괄 (예민한 리더)",
        "avatar": "avatar_park_yc.png",
        "dialogue": "콘솔 메모리 버퍼가 복구되자, OS Syslog에서 결정적인 기동 중단 감사 흔적이 관측됩니다.\n\n셧다운 직전인 02시 13분, 누군가가 root 권한 세션을 획득해 프로세스 가동을 강제로 차단하고 커널을 Halt시키는 바이너리를 실행한 흔적이 포착되었습니다.\n공격자가 서버 자체를 완전히 정지시켜 물리 분석을 무력화하기 위해 실행한 UNIX/Linux 표준 시스템 종료 명령어(영문 소문자 8자)를 파악하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⚙️ UNIX/Linux SYSTEM LOG DUMP</div>\n    <div style='background: rgba(0,0,0,0.6); padding: 15px; border-radius: 6px; border: 1px solid var(--border-color); font-family: var(--font-mono); font-size: 0.9rem; line-height: 1.6; color: var(--text-primary); text-align: left;'>\n        <span style='color: var(--text-muted);'>[Jul 21 02:13:05] authpriv.info sudo: root : TTY=pts/0 ; PWD=/ ; USER=root ; COMMAND=/sbin/XXXXXXXX</span><br>\n        <span style='color: var(--accent-magenta);'>[Jul 21 02:13:08] kern.info kernel: System is going down for halt NOW!</span><br>\n        <span style='color: var(--accent-red);'>[Jul 21 02:13:10] systemd[1]: Sent signal SIGTERM to all processes...</span>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.5;'>\n        힌트: `/sbin/` 경로 하위에서 호출되어 운영체제를 강제 종료시키는 대표적인 8글자 Linux 표준 명령어(영문 소문자)를 식별하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 7,
        "title": "CPU Overload PID (악성 프로세스 PID 추적)",
        "filename": "4ae9c668.html",
        "verify_hash": "2841dad7e57a80b5a9fdc7cd5799e7108f394e1c6157a8feb8e83db0808d3432",
        "speaker": "박용철 파트장",
        "role": "품질총괄 (예민한 리더)",
        "avatar": "avatar_park_yc.png",
        "dialogue": "시스템 가동이 중단되기 직전, 물리 자원을 독점하여 과부하를 가하던 프로세스 내역이 발견됩니다.\n\n서버가 강제 종료되기 직전에 CPU를 98% 이상 과독점하며 인프라 마비를 유도한 백그라운드 프로세스가 기동 중이었습니다.\n이것 때문에 인프라 전체에 연쇄 병목이 발생해 가동 정지 임계치가 돌파된 것으로 추정됩니다.\n당시 CPU 점유율을 비정상적으로 과점하며 시스템 리소스를 잠식한 주범 프로세스의 PID(프로세스 ID) 4자리를 프로세스 활성 로그(top/ps)에서 식별하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🖥️ OS ACTIVE PROCESS MONITOR (TOP/PS DUMP)</div>\n    <div style='max-height: 200px; overflow-y: auto; border: 1px solid var(--border-color); border-radius: 4px; background: rgba(0,0,0,0.45); text-align: left;'>\n        <table style='width: 100%; border-collapse: collapse; font-family: var(--font-mono); font-size: 0.8rem; color: var(--text-primary);'>\n            <tr style='position: sticky; top: 0; background: #080b11; color: var(--accent-blue); border-bottom: 1px solid var(--border-color); font-weight: bold;'>\n                <th style='padding: 6px;'>PID</th>\n                <th style='padding: 6px;'>USER</th>\n                <th style='padding: 6px;'>%CPU</th>\n                <th style='padding: 6px;'>%MEM</th>\n                <th style='padding: 6px;'>COMMAND</th>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1024</td>\n                <td style='padding: 5px 6px;'>systemd</td>\n                <td style='padding: 5px 6px;'>0.1%</td>\n                <td style='padding: 5px 6px;'>0.2%</td>\n                <td style='padding: 5px 6px;'>/usr/lib/systemd/systemd</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1028</td>\n                <td style='padding: 5px 6px;'>kthreadd</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>[kthreadd]</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1035</td>\n                <td style='padding: 5px 6px;'>kworker/0</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>[kworker/0:1H]</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1124</td>\n                <td style='padding: 5px 6px;'>journald</td>\n                <td style='padding: 5px 6px;'>0.2%</td>\n                <td style='padding: 5px 6px;'>1.5%</td>\n                <td style='padding: 5px 6px;'>/usr/lib/systemd/systemd-journald</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1180</td>\n                <td style='padding: 5px 6px;'>dbus</td>\n                <td style='padding: 5px 6px;'>0.1%</td>\n                <td style='padding: 5px 6px;'>0.4%</td>\n                <td style='padding: 5px 6px;'>/usr/bin/dbus-daemon --system</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1202</td>\n                <td style='padding: 5px 6px;'>rsyslogd</td>\n                <td style='padding: 5px 6px;'>0.1%</td>\n                <td style='padding: 5px 6px;'>0.8%</td>\n                <td style='padding: 5px 6px;'>/usr/sbin/rsyslogd -n</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1240</td>\n                <td style='padding: 5px 6px;'>sshd</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>0.6%</td>\n                <td style='padding: 5px 6px;'>/usr/sbin/sshd -D</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>2109</td>\n                <td style='padding: 5px 6px;'>oracle</td>\n                <td style='padding: 5px 6px;'>0.5%</td>\n                <td style='padding: 5px 6px;'>12.4%</td>\n                <td style='padding: 5px 6px;'>oracleHIS (LOCAL=NO)</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>2120</td>\n                <td style='padding: 5px 6px;'>oracle</td>\n                <td style='padding: 5px 6px;'>0.2%</td>\n                <td style='padding: 5px 6px;'>8.5%</td>\n                <td style='padding: 5px 6px;'>ora_pmon_HIS</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>3120</td>\n                <td style='padding: 5px 6px;'>tqo_ops</td>\n                <td style='padding: 5px 6px;'>1.2%</td>\n                <td style='padding: 5px 6px;'>2.1%</td>\n                <td style='padding: 5px 6px;'>python3 diagnostics.py</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>3211</td>\n                <td style='padding: 5px 6px;'>nginx</td>\n                <td style='padding: 5px 6px;'>0.1%</td>\n                <td style='padding: 5px 6px;'>1.2%</td>\n                <td style='padding: 5px 6px;'>nginx: worker process</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>3212</td>\n                <td style='padding: 5px 6px;'>nginx</td>\n                <td style='padding: 5px 6px;'>0.1%</td>\n                <td style='padding: 5px 6px;'>1.2%</td>\n                <td style='padding: 5px 6px;'>nginx: worker process</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>4081</td>\n                <td style='padding: 5px 6px;'>root</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>0.3%</td>\n                <td style='padding: 5px 6px;'>/usr/sbin/crond -n</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>5102</td>\n                <td style='padding: 5px 6px;'>postfix</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>0.5%</td>\n                <td style='padding: 5px 6px;'>/usr/libexec/postfix/master</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>5250</td>\n                <td style='padding: 5px 6px;'>unknown</td>\n                <td style='padding: 5px 6px;'>98.7%</td>\n                <td style='padding: 5px 6px;'>84.2%</td>\n                <td style='padding: 5px 6px;'>/tmp/dummy_exploit_daemon</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>5301</td>\n                <td style='padding: 5px 6px;'>root</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>[kworker/u2:2]</td>\n            </tr>\n            <tr>\n                <td style='padding: 5px 6px;'>5420</td>\n                <td style='padding: 5px 6px;'>tqo_ops</td>\n                <td style='padding: 5px 6px;'>0.3%</td>\n                <td style='padding: 5px 6px;'>1.0%</td>\n                <td style='padding: 5px 6px;'>bash</td>\n            </tr>\n        </table>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 12px; line-height: 1.5;'>\n        힌트: CPU 자원을 비정상적으로 98% 이상 독점 점유하고 있는 범인 프로세스의 PID 4자리를 표에서 찾아 입력하십시오. (필요 시 테이블 스크롤 가능)\n    </p>\n</div>"
    },
    {
        "stage": 8,
        "title": "Governance (IT 거버넌스 규정)",
        "filename": "e3ad4d0a.html",
        "verify_hash": "0b483f69c9eaed1e8f96259917fd826bc27d8cc20f8a5715880fb0b8a011def2",
        "speaker": "권남훈 파트장",
        "role": "운영총괄",
        "avatar": "avatar_kwon_nh.png",
        "dialogue": "박용철 파트장이 일방적인 일정 독촉 속에서 조사를 밀어붙이자, 권남훈 파트장이 정식 통제 절차의 당위성을 들고 나옵니다.\n\n정형화된 절차를 우회하는 조사는 규정 위반입니다. 장애 상황 관리 시에는 임시 조치 단계부터 근본 문제(Problem)를 정식 식별하여 등록하는 모범 체계가 요구됩니다.\n\n품질 보증 표준 프로세스를 이수하기 위해, 사내 거버넌스가 따르는 정식 IT 서비스 관리 프레임워크의 영문 소문자 4글자 약어를 입력하여 수사 무결성을 확보하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>📚 IT SERVICE GOVERNANCE FRAMEWORK</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;'>\n        힌트: 정보 기술 인프라 라이브러리(IT Infrastructure Library)의 영문 앞글자들을 딴 4글자 약어로, 전 세계 IT 부서의 표준 운영 가이드라인입니다.\n    </p>\n</div>"
    },
    {
        "stage": 9,
        "title": "Physical Device Map (물리 인프라 맵 감사)",
        "filename": "cee89b5e.html",
        "verify_hash": "27dce682e1ad2f2106be21d27e8025de5de7ee65cecc737d4f27a33af4c29a8a",
        "speaker": "권남훈 & 박재욱",
        "role": "파트장 vs DBA (대립 관계)",
        "avatar": "avatar_park_jw.png",
        "dialogue": "권남훈 파트장이 소명 검증을 위해 뜬금없이 복잡한 물리 보안 관리 식별 코드를 요구하며 앞길을 막아 세우고 있습니다.\n\n소명 티켓 접수를 위해서는 실제 동기화 오류를 일으킨 스토리지 장비가 보관된 랙 식별 번호 2자리(Rack ID)와 결선된 라우터 광포트 번호 2자리(Port ID)를 조합한 4자리 장비 관리 코드를 대라는 억지 요구입니다.\n이 새벽에 그런 복잡한 대장 번호를 다 외우는 것은 불가능합니다. 기계실 단말기에 기록된 물리 장비 배치 맵과 광 스위치 포트 인터페이스 상태 로그를 대조해 4자리 장비 식별자(8204)를 확인하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⚙️ PHYSICAL SERVER ROOM RACK MAP</div>\n    <div class='ascii-diagram' style='text-align: left; font-size: 0.8rem; line-height: 1.5; background: rgba(0,0,0,0.5); padding: 12px; border-radius: 6px; border: 1px solid var(--border-color); color: var(--text-primary);'>\n+-------------------------------------------------------------+\n|  [SERVER ROOM ZONE A - RACK ARRANGEMENT]                    |\n|                                                             |\n|  [Rack 80] : L4 load balancer VIP suite                     |\n|  [Rack 81] : Financial Core WAS clusters (01-08)            |\n|  [Rack 82] : SAN Storage Target controller units            |\n|  [Rack 83] : Oracle RAC database engine nodes               |\n+-------------------------------------------------------------+\n    </div>\n    \n    <div class='puzzle-title' style='margin-top: 15px;'>📡 SWITCH ROUTER PORT INTERFACE LOG</div>\n    <div style='background: rgba(0,0,0,0.6); padding: 12px; border-radius: 6px; border: 1px solid var(--border-color); font-family: var(--font-mono); font-size: 0.8rem; line-height: 1.6; text-align: left; color: var(--text-primary);'>\n        [Port 01] - LINK UP   - target: Core-WAS-Switch<br>\n        [Port 02] - LINK UP   - target: Enterprise-Backbone<br>\n        [Port 03] - LINK DOWN - target: Internal-VDI-Hub<br>\n        [Port 04] - LINK UP   - target: SAN-Storage-Fibre-Switch\n    </div>\n    \n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 12px; line-height: 1.5;'>\n        힌트: 배치 맵에서 'SAN Storage' 장비가 속한 랙 번호 2자리와 스위치 로그에서 'SAN-Storage-Fibre-Switch'가 결선된 포트 번호 2자리를 찾아 차례대로 조합하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 10,
        "title": "The Cronjob (Crontab 스케줄링)",
        "filename": "524cfb66.html",
        "verify_hash": "318fb6b0fd6eb7ef86613797123429db40159a50c0b443197c3a229ecefc07fb",
        "speaker": "김진혁 차장",
        "role": "네트워크 담당",
        "avatar": "avatar_kim_jh.png",
        "dialogue": "네트워크 담당 김진혁 차장이 개입하여 박재욱 차장의 임의 수동 조작 혐의를 주장하고 나섭니다.\n\n스토리지 장애를 핑계 대고 있지만, 본질은 박 차장이 임의로 스크립트를 수동 가동해 시스템을 과부하시킨 겁니다. 로그가 명백히 증명하고 있습니다.\n이에 대해 박 차장은 수동으로 가동한 적이 없으며, 스케줄에 따른 정기 기동이 돌았을 뿐이라고 항변합니다.\n의혹을 규명하기 위해, 타겟 서버의 크론탭(Crontab) 작업 설정 데이터 상 배치 스크립트가 기동되도록 자동 스케줄링되어 있던 시각(24시간 형식 4자리 HHMM)을 도출하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⏰ TARGET CRONTAB CONFIGURATION</div>\n    <div style='background: #020306; font-family: var(--font-mono); padding: 15px; border-radius: 6px; border: 1px solid var(--border-color); text-align: center; font-size: 1.1rem; color: var(--accent-blue);'>\n        45 1 * * * /usr/sbin/backup.sh\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.5;'>\n        힌트: 크론탭 시간 설정 구조는 [분] [시] [일] [월] [요일] 순서입니다.\n        위 설정은 매일 '1시 45분'에 구동됨을 의미합니다. 포맷에 맞춰 4자리 숫자로 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 11,
        "title": "The Command (박주암 과장)",
        "filename": "e3307ab7.html",
        "verify_hash": "53c148b793bd0c621b03b40afe93b7c39bce8b4d00157bc10142b8a848af32ac",
        "speaker": "박주암 과장",
        "role": "WAS 담당 (실무 운영자)",
        "avatar": "avatar_park_ja.png",
        "dialogue": "결산 백업의 부하가 셧다운을 직접 유도한 원인이 아니라는 정황이 WAS 로그에서 실증됩니다.\n\n단말기 명령어 히스토리를 뜯어보니 셧다운 직전에 타인의 무단 침투 정황이 관측됩니다. 02시 13분경, 누군가 WAS 계정을 불법 도용해 특정 데이터베이스 커널 접속 유틸리티를 기동했습니다.\n침입자가 DB 전체를 오프라인 상태로 전환하여 동기화 장애를 유발하고 인프라를 깨뜨리기 위해 실행한 이 데이터베이스 전용 질의 클라이언트 명령어(영문 소문자)를 파악하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>💻 INCIDENT COMMAND HISTORY DUMP</div>\n    <p style='font-family: var(--font-mono); color: var(--text-primary); font-size: 0.95rem; line-height: 1.6;'>\n        $ cd /u01/app/oracle/product/12.1.0/dbhome_1/bin<br>\n        $ ./sqlplus / as sysdba<br>\n        &gt; SHUTDOWN IMMEDIATE;<br>\n        <span style='color: var(--accent-red);'>[02:13:21] DISCONNECTED FROM DATABASE.</span>\n    </p>\n</div>"
    },
    {
        "stage": 12,
        "title": "The Network Lie (김진혁 차장)",
        "filename": "16417f5b.html",
        "verify_hash": "debdc6fdb6c19c94ff78b653767bfac108d84ed51a54a58a72866dc635b15729",
        "speaker": "김진혁 차장",
        "role": "네트워크 담당",
        "avatar": "avatar_kim_jh.png",
        "dialogue": "김진혁 차장은 당시 본인의 모니터링 접속 환경이 철저하게 보장되었음을 강변합니다.\n\n장애가 터진 시각, 자신은 휴게실에서 노트북을 가동하고 기계실 랙에 적재된 라우터 허브 장비의 무선 신호를 수신해 부하 상태를 안전하게 확인 중이었다고 설명합니다. 통신 끊김은 없었다는 주장입니다.\n하지만 기계실 하드웨어 장치 상세 매뉴얼을 검토하던 중, 김 차장의 알리바이 진술에서 심각한 모순이 탐지됩니다. 장치 도면을 분석하여 그가 주장한 거짓 무선 접속 기술 명칭(영문 소문자 4자)을 식별하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🌐 T5004 ROUTER HARDWARE SPECIFICATION</div>\n    <div class='ascii-diagram'>\n+------------------------------------------------+\n|  T5004 INTERNET RACK HUB                      |\n|                                                |\n|  [LAN1]   [LAN2]   [LAN3]   [LAN4]   [WAN]     |\n|  [ [O] ]  [ [O] ]  [ [X] ]  [ [X] ]  [ [O] ]   |\n|   |  |     |  |                         |  |   |\n|    유선     유선                         인터넷  |\n|                                                |\n|  * WARNING: NO WIRELESS ANTENNA MODULE *       |\n|  * ONLY WIRED ETHERNET CONNECTION SUPPORTED *  |\n+------------------------------------------------+\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.6;'>\n        김진혁 차장의 주장: '공유기의 무선 전파 안테나 신호를 잡아 노트북으로 모니터링했다.'<br>\n        장비 매뉴얼: 무선 모듈 없음, 오직 유선 포트만 존재.<br>\n        김 차장이 접속 기술이라고 주장한 이 거짓말 속의 무선 인터넷 명칭(영문 소문자 4자)을 기입하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 13,
        "title": "The Server Lie (이재헌 과장)",
        "filename": "94e06050.html",
        "verify_hash": "692e4e5decffcf5eac86471ba27ac56a861268d060e4a53a0c768617f4d3a56f",
        "speaker": "이재헌 과장",
        "role": "서버 담당",
        "avatar": "avatar_lee_jh.png",
        "dialogue": "김 차장의 장비 묘사 거짓말이 탄로 난 가운데, 이재헌 과장의 자원 할당 진술을 검토합니다.\n\n물리 서버 자원은 평소에 아주 풍부하게 할당해 두어 넉넉한 상태였다고 강변합니다. 자원 부족으로 죽은 게 절대 아니라는 주장입니다.\n그러나 실제 자원 모니터링 명세를 보면 CPU 자원 소모율이 99.6%에 육박하며 한계점에 도달해 있었습니다.\n이 과장의 실무 태만과 안일한 설정을 실증하기 위해, 자원 할당 여유가 극도로 제한되어 물리 장비의 기본 동작만 간신히 보장하는 한계 튜닝 상태를 지칭하는 IT 업계 전문 용어(영문 소문자 7자)를 기입하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⚙️ VM INSTANCE SPECIFICATION OVERVIEW</div>\n    <div class='cpu-widget'>\n        <div>INSTANCE_NAME: Core-WAS-01</div>\n        <div class='cpu-bar'>CPU USAGE: [██████████] 99.6% (Overload)</div>\n        <div style='color: var(--accent-magenta); margin-top: 5px;'>AVAILABLE_MARGIN: 0.4%</div>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.6;'>\n        CPU 여유 마진이 0.4%밖에 되지 않는 위태로운 상태입니다.<br>\n        서버 튜닝이 충분히 넉넉한 상태가 아니라, 자원이 고갈 직전이어서 물리 장비의 숨통만 겨우 붙여놓은 한계 튜닝 상태를 의미하는 IT 영단어(영문 소문자 7자)를 기입하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 14,
        "title": "The Motivation (박용철 총괄)",
        "filename": "c70ec350.html",
        "verify_hash": "838940b6f1deea2e9aca2c69a4df9a484139e1d8ab954a1b2366df3777ae416b",
        "speaker": "박용철 파트장",
        "role": "품질총괄 (예민한 리더)",
        "avatar": "avatar_park_yc.png",
        "dialogue": "서버 자원 불균형과 김 차장의 이상 진술이 발견된 와중에, 박용철 파트장이 수사 방향을 다시 재조정합니다.\n\n일시적 포트 통신 실패에 따른 데이터베이스 파손 정황을 정확하게 짚고 가야 합니다. 스토리지 단절 당시 연쇄적으로 발생한 디스크 물리 무결성 실패 로그부터 해독하십시오.\n제시된 정규표현식(Regex) 검출 필터를 로그 덤프에 매칭해, 디스크 파손을 나타내는 오라클 내부 치명적 에러 코드를 소문자로 기입하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔍 CORRUPTION PATTERN DETECTION FILTER</div>\n    <ul style='list-style-type: square; padding-left: 20px; font-size: 0.85rem; line-height: 1.6; color: var(--accent-blue); font-family: var(--font-mono);'>\n        <li>정규식 필터 패턴: ^[A-Za-z]+-[0-9]{5}$ (영문 단어 + 붙임표 + 정확히 5자리 숫자)</li>\n        <li>[DB ERROR LOG DUMP]:</li>\n        <li style='color: var(--text-muted);'>- sys-info-10023</li>\n        <li style='color: var(--text-primary); font-weight: bold;'>- ORA-00600 (internal error)</li>\n        <li style='color: var(--text-muted);'>- DB-CONN-5020</li>\n    </ul>\n</div>"
    },
    {
        "stage": 15,
        "title": "The VDI Rule (권남훈 총괄)",
        "filename": "aac380d4.html",
        "verify_hash": "6f89bddf8582a8d223e132d10c9436e788687f159fbbf5ac36a6eb14d307a3fa",
        "speaker": "권남훈 파트장",
        "role": "운영총괄",
        "avatar": "avatar_kwon_nh.png",
        "dialogue": "데이터베이스 단절 에러가 특정되었음에도, 권남훈 파트장은 외부 침입 가능성을 철저히 일축합니다.\n\nVDI 보안 규정상 외부 침입자가 타인의 IP 주소를 도용하는 행위는 논리적으로 차단되어 있습니다. 사용자가 세션을 종료하는 즉시 할당되어 있던 사설 IP 주소는 풀(Pool)로 회수되며, 이후 새로 로그인하는 다른 사람에게 즉각 순차 재배포되기 때문입니다.\n보안망 회수 규칙의 한계를 검증하기 위해, 사설 IP 주소의 동적 자동 배분을 관장하는 이 네트워크 표준 규약 약어(H C P D)의 아나그램을 풀어 기입하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🧩 ANAGRAM SOLVER: H C P D</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;'>\n        IP 주소를 동적으로 할당해 주는 대표적인 네트워크 표준 규약의 영어 약어로 재정렬하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 16,
        "title": "Subnet Mistake (김진혁의 실수 1)",
        "filename": "ef5ad16e.html",
        "verify_hash": "8527a891e224136950ff32ca212b45bc93f69fbb801c3b1ebedac52775f99e61",
        "speaker": "스토리지 스위치 라우팅 로그",
        "role": "SYSTEM SYSTEM",
        "avatar": "NET",
        "dialogue": "권남훈 파트장이 제시한 DHCP 유동 IP 재배포 규칙이 오히려 새로운 수사 실마리를 던져줍니다.\n네트워크 스위치 콘솔 로그를 상세 조회하던 중, 스토리지 관리 권한에서 중대한 작업 조작 실수의 흔적이 발견됩니다.\n\n김진혁 차장이 장애 발생 30분 전, 백업 보강용 라우팅 대역 테이블을 조작하다가 실수로 CIDR 마스크 대역 폭을 `/28` 로 잘못 격리한 내역이 입증됩니다. 이로 인해 스토리지 통신 연결이 차단된 것입니다.\n서브넷 마스크 `/28` 등급 대역에서 시스템 예약 주소 2개를 제외하고 실제 내부 장비들에 유효하게 분배해 줄 수 있는 최대 IP(호스트) 개수를 계산하여 입력하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔢 CIDR SUBMETMASK SUITE: /28</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; line-height: 1.6;'>\n        - 전체 IP 주소 표현 비트: 32비트<br>\n        - 호스트 할당 비트수: 32비트 - 28비트 = 4비트 (2^4 = 총 16개 주소)<br>\n        - 사용 불가 특수한 주소: 2개 (네트워크 ID 주소 & 브로드캐스트 IP)<br>\n        - <strong style='color: var(--accent-magenta);'>계산 공식: 2^(32 - 28) - 2</strong>\n    </p>\n</div>"
    },
    {
        "stage": 17,
        "title": "SAN Storage (김진혁의 실수 2)",
        "filename": "0e3d9fd2.html",
        "verify_hash": "2fac394011e7d326f9c7ff5e532316be43ce2e7d88b4f1377f585e8c8c083672",
        "speaker": "박재욱 차장",
        "role": "DBA",
        "avatar": "avatar_park_jw.png",
        "dialogue": "김 차장의 서브넷 라우팅 오설정이 스토리지 통신 단절을 일으키고, 그로 인해 결산 DB 데이터가 연쇄 파손되었음이 물리적으로 실증된 국면.\n\n이 사실이 밝혀지자 박용철 파트장이 김 차장을 향해 해명을 요구하며 크게 분개합니다. 이에 대해 김 차장은 일시적인 복구 테스트 중 발생한 설정 편차라며 얼버무립니다.\n끊겨버린 스토리지 연결 경로의 즉각적인 수동 복구가 요구됩니다. iSCSI 프로토콜 통신 채널 복구를 위해, 해당 스토리지 장치 결선에 기본적으로 할당되어 가동되는 TCP 표준 포트 번호 4자리를 기입하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔌 PROTOCOL PORT CHECK: iSCSI TARGET</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;'>\n        힌트: 인터넷 소형 컴퓨터 시스템 인터페이스(iSCSI) 통신 프로토콜이 표준으로 점유하여 사용하는 포트 번호입니다.\n    </p>\n</div>"
    },
    {
        "stage": 18,
        "title": "Time Drift (이재헌의 실수)",
        "filename": "58addc3e.html",
        "verify_hash": "f020272c938ba0a213d31613fd5a1a8b053c693d489551f8b24e900db43d6873",
        "speaker": "이재헌 과장",
        "role": "서버 담당 (죄인 모드)",
        "avatar": "avatar_lee_jh.png",
        "dialogue": "스토리지 연결 복구 작업이 수립된 가운데, 서버 담당 이재헌 과장이 추가적인 설정 결함을 보고해 옵니다.\n\n인프라 증설 단계에서 시간 동기화 데몬(NTP) 동작 설정을 수동으로 누락한 결과, WAS 물리 서버의 시스템 내부 시간이 실제 세상 표준시보다 정확히 '15분 느리게' 흘러가고 있음이 파악되었습니다.\nWAS의 감사 기록 상 강제 중단 명령어(`sqlplus`)가 구동된 서버 타임 스탬프는 '01:58'로 확인됩니다.\n이 15분의 오차를 물리적으로 정상 환산하여 보정한, 실제 세상의 실제 셧다운 구동 표준 시각(24시간 형식 4자리 HHMM)을 도출하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⏳ TIME SYNC DRIFT LOGS</div>\n    <ul style='list-style-type: square; padding-left: 20px; font-size: 0.85rem; line-height: 1.6; color: var(--text-primary);'>\n        <li>WAS 서버 기록 시각: 01:58 (서버 시계가 15분 느린 상태)</li>\n        <li>물리적 실제 표준 시각 = 서버 기록 시각 + 15분 오차 보정</li>\n        <li><strong style='color: var(--accent-magenta);'>요구 포맷: 4자리 디지털 형식 (예: 01시 10분 -> 0110)</strong></li>\n    </ul>\n</div>"
    },
    {
        "stage": 19,
        "title": "The Culprit (진범 도출)",
        "filename": "60268820.html",
        "verify_hash": "3a693a0e2772b93bc89e4ba6167e17118923d7bdae9e10f1857a89d30540d85f",
        "speaker": "사건 합동 수사반",
        "role": "INVESTIGATION",
        "avatar": "avatar_park_yc.png",
        "dialogue": "모든 물리 단서 조각이 일치하며 실마리가 드러납니다.\n서버의 느린 클럭 오차를 보정한 진짜 셧다운 명령 구동 시간은 실제 시간 기준으로 정확히 '02:13'이었습니다.\n\n사건 당일 사용자 망 세션 회수 타임라인을 검토하면, DBA 박재욱 차장은 백업 업무를 마치고 '02:05'에 공식 로그아웃하여 세션을 해제하고 사용하던 IP를 반납했습니다.\n권 파트장이 증명한 DHCP 회수 및 순차 재분배 원칙에 따라, 02:05에 반납된 무결한 사설 IP를 02:13에 즉각 할당받아 악용한 인물이 좁혀집니다.\n당일 무선(wifi) 신호로 접속 상태를 모니터링했다는 치명적인 기술적 거짓말을 늘어놓은 진짜 범인의 이름을 기입하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔎 REAL-TIME TIMELINE COMPARISON</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;'>\n        누군가가 DHCP의 규약 허점을 이용하여 DBA 박 차장이 사용하다가 반납한 IP 주소를 곧바로 할당받아 악용한 물증을 확보했습니다.<br>\n        조직도 상의 진범 이름 3글자를 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 20,
        "title": "Ticket Closed (최종 결재)",
        "filename": "6c46331e.html",
        "verify_hash": "a4c3ed04a95a3da14a9d235c83d868bed7c0f45cf7f3faa751ee8f50598d2211",
        "speaker": "박용철 파트장",
        "role": "품질총괄 (예민한 리더)",
        "avatar": "avatar_park_yc.png",
        "dialogue": "진범의 정체가 최종 확인되었습니다.\n네트워크 담당 김진혁 차장이 라우터 CIDR 설정 작업 실수를 은폐하기 위해, 일부러 백업 중이던 코어 DB 결선 스토리지를 분리하고, 나아가 책임을 DBA에게 전가하기 위해 WAS 서버 강제 셧다운 공작까지 감행한 전말이 드러납니다.\n\n결국 공격자가 내세운 무선 모니터링이라는 하드웨어적 모순이 자가당착을 유발했습니다.\n성공적인 장애 대응 및 음모 규명이 완료되었습니다. 최종 승인 확인 키 [ done ]를 기입하여 이 새벽의 장애 인시던트 티켓을 공식 클리어하고 종결 처리하십시오.",
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
                    <!-- Dialogue representation -->
                    <div class="dialogue-card speaker-suspect">
                        <div class="avatar-container">
                            {avatar_html}
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
    # Build avatar html element
    if s["avatar"].endswith(".png"):
        avatar_html = f'<img src="{s["avatar"]}" alt="Suspect Avatar" style="width: 100%; height: 100%; object-fit: cover; border-radius: 4px; border: 1px solid var(--border-color); box-shadow: 0 0 10px rgba(0,229,255,0.2);">'
    else:
        avatar_html = f'<div class="avatar-placeholder" style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; background: rgba(0,229,255,0.1); border: 1px solid var(--border-color); border-radius: 4px; font-family: var(--font-mono); font-weight: bold; color: var(--accent-blue);">{s["avatar"]}</div>'

    content = html_template.format(
        stage_num=s["stage"],
        stage_title=s["title"],
        verify_hash=s["verify_hash"],
        avatar_html=avatar_html,
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
