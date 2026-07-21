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
        "avatar": "PARK_YC",
        "dialogue": "조사관님! 지금 새벽 2시에 메인 금융 코어 WAS 서버가 알 수 없는 명령어로 강제 종료됐습니다!\n부서장님에 본부장님까지 비상대기 걸려서 제 목줄이 날아가기 직전이라고요!\n\n부팅 아직 안 끝났습니까? 서두르세요!\n\n보안 인가 코드 입력창이 막혔다고요? 권남훈 파트장이 조사관님 부팅 키를 잠가둔 모양인데,\n언제 정식 결재 올리고 승인받습니까! 당장 F12(개발자 도구) 열어서 소스코드 주석 뒤지세요.\n거기에 권 파트장이 백업용으로 남겨둔 3자리 보안 키(KEY) 찾아서 즉시 로그인 승인하세요!",
        "gimmick_html": "<!-- KEY: 179 -->\n<div class='puzzle-container'>\n    <div class='puzzle-title'>🔒 ACCESS PROTECTION KEY</div>\n    <p style='color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;'>\n        인가 토큰이 보안 커널에 의해 물리 차단되었습니다.<br>\n        F12(개발자 도구)를 통해 HTML 소스코드의 주석을 분석하고 백업 마스터 키를 찾아 터미널에 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 2,
        "title": "Encrypted Packet (Base64)",
        "filename": "b4bcdd0d.html",
        "verify_hash": "f5334f59cc820a5c99fd2a5b5527884c821c19f1daa7c825368603aba61d6178",
        "speaker": "권남훈 파트장",
        "role": "운영총괄 (규정 맹신자)",
        "avatar": "KWON_NH",
        "dialogue": "부팅하자마자 시스템을 불법 조작하려 하십니까? 조사관님.\n우리 본부의 모든 VDI망 세션은 완벽하게 격리 통제되고 있습니다.\n\n제가 정식 절차에 따라 제 개인 단말기에 기록된 패킷 덤프 페이로드를 전달해 드리지요.\n데이터는 규정상 Base64로 인코딩되어 있습니다.\n\n이 암호 텍스트를 디코딩하여, 당시 WAS 서버가 백그라운드 통신에 사용한 사설 포트 번호 4자리를 정확히 입력해 규정상 정식 승인 절차를 밟으십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>📡 PACKET PAYLOAD DUMP</div>\n    <div style='display: flex; gap: 15px; align-items: center; justify-content: center; background: rgba(0,0,0,0.5); padding: 15px; border-radius: 4px;'>\n        <p style='font-family: var(--font-mono); color: var(--accent-magenta); font-size: 1.25rem; letter-spacing: 1px;'>UG9ydCAyMzIx</p>\n        <button class='copy-btn' onclick=\"copyToClipboard('UG9ydCAyMzIx', this)\">COPY</button>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.5;'>\n        힌트: Base64 형식으로 변환된 포트 정보 페이로드입니다.<br>\n        디코딩 시 문자 뒤에 기재된 숫자 4자리를 찾아 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 3,
        "title": "Log Flood (권한 검색)",
        "filename": "83e5e934.html",
        "verify_hash": "4099ed5ba70aebc5a9dc26bc2093d4b45839f99b306bd12f68cedfd351e6ab7a",
        "speaker": "박용철 파트장",
        "role": "품질총괄 (예민한 리더)",
        "avatar": "PARK_YC",
        "dialogue": "권 파트장! 그 잘난 규정 맹신하다가 백업 파일 권한까지 털린 거 아닙니까?\n\n[권남훈]: 표준 rwxr-xr-x(755) 권한으로 배포했으니 완벽합니다.\n\n[박용철]: 말만 믿지 말고, 조사관님! 당장 감사 로그 덤프 스캔하세요.\n분명히 관리 부주의로 권한 다 열린 비정상 파일(rwxr-xr--)이 섞여 있을 겁니다.\n찾아내서 변환 수치 뽑아주세요. 바로 권 파트장 입을 막아버리자고요!",
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
        "dialogue": "[위이이이잉- 삐- 삐-]\n\n서버실 내부의 전압 경보 장치가 작동하며 갑작스럽게 단말기 모니터 화면의 신호가 끊어집니다!\n모든 텍스트가 사라지고 눈앞이 새카만 어둠으로 물들었습니다.\n\n[박주암 과장]: 헉! 조사관님! 누군가가 강제로 단말기 모니터 신호를 차단해 분석을 방해하려는 것 같습니다!\n\n하지만 당황하지 마십시오. 조사관 단말기의 비상 복구 안전 장치에 의해, 화면 중앙 캔버스 어딘가에 보이지 않는 검은색 글씨로 긴급 시스템 기동 비밀코드가 렌더링되어 있습니다.\n마우스를 휘저어 화면을 크게 드래그(Ctrl+A)해 숨겨진 코드를 읽어내십시오!",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>💡 VISIBILITY RESTORATION OVERLAY</div>\n    <div class='hidden-text-container'>\n        <span class='hidden-error-text'>404500</span>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px;'>\n        드래그하여 숨겨진 에러 코드를 찾아 터미널에 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 5,
        "title": "Zalgo Text (글자 깨짐)",
        "filename": "48b42551.html",
        "verify_hash": "af4883c99558a3f6ef589d7e9a69585135ebac48f6b55c12e5e96849dc3707ee",
        "speaker": "이재헌 과장",
        "role": "서버 담당 (식은땀 흘리는 실무자)",
        "avatar": "LEE_JH",
        "dialogue": "죄송합니다 조사관님! 정전의 여파로 서버 콘솔 메모리 버퍼 영역 전체가 완전히 깨진 특수문자 노이즈로 덮여 데이터 복구가 불가능해 보입니다.\n\n하지만 보안 커널은 복구 세션 수립을 위해 '현재 시스템의 작동 불량 상태'를 지칭하는 영문 대문자 3글자 상태 플래그 입력을 요구하고 있습니다.\n\n시스템이 다운되어 작동이 '나쁜(불량)' 상태에 직면했음을 지칭하는 대표적인 영어 대문자 3글자 단어(B _ _)를 연상해 보십시오.\n그 단어의 각 알파벳에 해당하는 10진수 아스키(ASCII) 값을 하단의 코드표에서 찾아 차례대로 합쳐 입력해 주십시오. 제발 저 좀 살려주십시오!",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⚠️ CORRUPTED STRING BUFFER</div>\n    <div class='zalgo-box' style='font-family: var(--font-mono); font-size: 1.25rem; letter-spacing: 2px; color: var(--accent-magenta); text-align: center; padding: 20px;'>\n        #$@%&amp;* #$@%&amp;* SYSTEM_LOCKED *&amp;%@$# *&amp;%@$#\n    </div>\n    <div style='margin-top: 15px; text-align: center;'>\n        <p style='color: var(--accent-blue); font-size: 0.85rem; margin-bottom: 8px; font-family: var(--font-title);'>📖 ASCII REFERENCE CHART</p>\n        <img src='ascii_table.png' alt='ASCII Code Table' style='max-width: 100%; border: 1px solid var(--border-color); border-radius: 6px; box-shadow: 0 0 15px rgba(0,229,255,0.15);'>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.5;'>\n        힌트: 시스템의 오작동 및 불량 상태를 의미하는 영문 대문자 3글자 단어(B _ _)의 아스키 10진수 코드값을 표에서 순서대로 찾아 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 6,
        "title": "System Halt Signal (시스템 종료 명령어)",
        "filename": "db590ac0.html",
        "verify_hash": "08434ba9cdf55a02284e2913400586cd289878e0f055f7bb0b07ce392caeb989",
        "speaker": "박용철 파트장",
        "role": "품질총괄 (예민한 리더)",
        "avatar": "PARK_YC",
        "dialogue": "조사관님! 셧다운 원인 로그를 커널 레벨부터 정밀 검토하던 중, OS Syslog에서 결정적인 공격 흔적을 포착했습니다.\n\n시스템이 완전히 암전되기 직전인 02시 13분, 누군가가 root 권한 세션을 획득해 프로세스 기동을 강제로 중단시키고 커널을 Halt시키는 시스템 제어 바이너리를 구동한 흔적이 남아 있습니다.\n\n이 공격자가 서버를 물리적으로 꺼버려 증거를 인멸하고 우리 복구를 지연시키기 위해 실행한 UNIX/Linux 표준 시스템 종료 명령어(영문 소문자 8자)를 터미널에 입력해 당시 가동된 바이너리 파일을 실증하십시오!",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⚙️ UNIX/Linux SYSTEM LOG DUMP</div>\n    <div style='background: rgba(0,0,0,0.6); padding: 15px; border-radius: 6px; border: 1px solid var(--border-color); font-family: var(--font-mono); font-size: 0.9rem; line-height: 1.6; color: var(--text-primary); text-align: left;'>\n        <span style='color: var(--text-muted);'>[Jul 21 02:13:05] authpriv.info sudo: root : TTY=pts/0 ; PWD=/ ; USER=root ; COMMAND=/sbin/XXXXXXXX</span><br>\n        <span style='color: var(--accent-magenta);'>[Jul 21 02:13:08] kern.info kernel: System is going down for halt NOW!</span><br>\n        <span style='color: var(--accent-red);'>[Jul 21 02:13:10] systemd[1]: Sent signal SIGTERM to all processes...</span>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.5;'>\n        힌트: `/sbin/` 경로 하위에서 호출되어 운영체제를 강제 종료시키는 대표적인 8글자 Linux 표준 명령어(영문 소문자)를 식별하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 7,
        "title": "CPU Overload PID (악성 프로세스 PID 추적)",
        "filename": "4ae9c668.html",
        "verify_hash": "2841dad7e57a80b5a9fdc7cd5799e7108f394e1c6157a8feb8e83db0808d3432",
        "speaker": "박용철 파트장",
        "role": "품질총괄 (예민한 리더)",
        "avatar": "PARK_YC",
        "dialogue": "조사관님! WAS 서버가 강제 종료되기 직전에 전체 시스템의 CPU를 98% 이상 과독점하며 서버를 마비시킨 의심스러운 불법 백그라운드 프로세스가 가동 중이었습니다!\n\n이것 때문에 인프라 전체에 연쇄적인 병목이 걸려 SLA 임계치가 깨질 뻔했던 겁니다. 이재헌 서버 과장 녀석은 평소에 프로세스 모니터링도 안 하고 뭐 한 겁니까!\n\n당장 셧다운 직전의 OS 프로세스 활성 상태 감사 로그(top/ps)를 분석해 주십시오. CPU 점유율을 비정상적으로 과점하며 서버를 혼란에 빠뜨린 이 악성 프로세스의 PID(프로세스 ID) 4자리를 정확히 식별해 주십시오. 즉시 강제 킬(kill) 처리해서 흔적을 차단해야 합니다!",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🖥️ OS ACTIVE PROCESS MONITOR (TOP/PS DUMP)</div>\n    <div style='max-height: 200px; overflow-y: auto; border: 1px solid var(--border-color); border-radius: 4px; background: rgba(0,0,0,0.45); text-align: left;'>\n        <table style='width: 100%; border-collapse: collapse; font-family: var(--font-mono); font-size: 0.8rem; color: var(--text-primary);'>\n            <tr style='position: sticky; top: 0; background: #080b11; color: var(--accent-blue); border-bottom: 1px solid var(--border-color); font-weight: bold;'>\n                <th style='padding: 6px;'>PID</th>\n                <th style='padding: 6px;'>USER</th>\n                <th style='padding: 6px;'>%CPU</th>\n                <th style='padding: 6px;'>%MEM</th>\n                <th style='padding: 6px;'>COMMAND</th>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1024</td>\n                <td style='padding: 5px 6px;'>systemd</td>\n                <td style='padding: 5px 6px;'>0.1%</td>\n                <td style='padding: 5px 6px;'>0.2%</td>\n                <td style='padding: 5px 6px;'>/usr/lib/systemd/systemd</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1028</td>\n                <td style='padding: 5px 6px;'>kthreadd</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>[kthreadd]</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1035</td>\n                <td style='padding: 5px 6px;'>kworker/0</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>[kworker/0:1H]</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1124</td>\n                <td style='padding: 5px 6px;'>journald</td>\n                <td style='padding: 5px 6px;'>0.2%</td>\n                <td style='padding: 5px 6px;'>1.5%</td>\n                <td style='padding: 5px 6px;'>/usr/lib/systemd/systemd-journald</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1180</td>\n                <td style='padding: 5px 6px;'>dbus</td>\n                <td style='padding: 5px 6px;'>0.1%</td>\n                <td style='padding: 5px 6px;'>0.4%</td>\n                <td style='padding: 5px 6px;'>/usr/bin/dbus-daemon --system</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1202</td>\n                <td style='padding: 5px 6px;'>rsyslogd</td>\n                <td style='padding: 5px 6px;'>0.1%</td>\n                <td style='padding: 5px 6px;'>0.8%</td>\n                <td style='padding: 5px 6px;'>/usr/sbin/rsyslogd -n</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>1240</td>\n                <td style='padding: 5px 6px;'>sshd</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>0.6%</td>\n                <td style='padding: 5px 6px;'>/usr/sbin/sshd -D</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>2109</td>\n                <td style='padding: 5px 6px;'>oracle</td>\n                <td style='padding: 5px 6px;'>0.5%</td>\n                <td style='padding: 5px 6px;'>12.4%</td>\n                <td style='padding: 5px 6px;'>oracleHIS (LOCAL=NO)</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>2120</td>\n                <td style='padding: 5px 6px;'>oracle</td>\n                <td style='padding: 5px 6px;'>0.2%</td>\n                <td style='padding: 5px 6px;'>8.5%</td>\n                <td style='padding: 5px 6px;'>ora_pmon_HIS</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>3120</td>\n                <td style='padding: 5px 6px;'>tqo_ops</td>\n                <td style='padding: 5px 6px;'>1.2%</td>\n                <td style='padding: 5px 6px;'>2.1%</td>\n                <td style='padding: 5px 6px;'>python3 diagnostics.py</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>3211</td>\n                <td style='padding: 5px 6px;'>nginx</td>\n                <td style='padding: 5px 6px;'>0.1%</td>\n                <td style='padding: 5px 6px;'>1.2%</td>\n                <td style='padding: 5px 6px;'>nginx: worker process</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>3212</td>\n                <td style='padding: 5px 6px;'>nginx</td>\n                <td style='padding: 5px 6px;'>0.1%</td>\n                <td style='padding: 5px 6px;'>1.2%</td>\n                <td style='padding: 5px 6px;'>nginx: worker process</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>4081</td>\n                <td style='padding: 5px 6px;'>root</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>0.3%</td>\n                <td style='padding: 5px 6px;'>/usr/sbin/crond -n</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>5102</td>\n                <td style='padding: 5px 6px;'>postfix</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>0.5%</td>\n                <td style='padding: 5px 6px;'>/usr/libexec/postfix/master</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>5250</td>\n                <td style='padding: 5px 6px;'>unknown</td>\n                <td style='padding: 5px 6px;'>98.7%</td>\n                <td style='padding: 5px 6px;'>84.2%</td>\n                <td style='padding: 5px 6px;'>/tmp/dummy_exploit_daemon</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>5301</td>\n                <td style='padding: 5px 6px;'>root</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>0.0%</td>\n                <td style='padding: 5px 6px;'>[kworker/u2:2]</td>\n            </tr>\n            <tr>\n                <td style='padding: 5px 6px;'>5420</td>\n                <td style='padding: 5px 6px;'>tqo_ops</td>\n                <td style='padding: 5px 6px;'>0.3%</td>\n                <td style='padding: 5px 6px;'>1.0%</td>\n                <td style='padding: 5px 6px;'>bash</td>\n            </tr>\n        </table>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 12px; line-height: 1.5;'>\n        힌트: CPU 자원을 비정상적으로 98% 이상 독점 점유하고 있는 범인 프로세스의 PID 4자리를 표에서 찾아 입력하십시오. (필요 시 테이블 스크롤 가능)\n    </p>\n</div>"
    },
    {
        "stage": 8,
        "title": "Governance (IT 거버넌스 규정)",
        "filename": "e3ad4d0a.html",
        "verify_hash": "0b483f69c9eaed1e8f96259917fd826bc27d8cc20f8a5715880fb0b8a011def2",
        "speaker": "권남훈 파트장",
        "role": "운영총괄",
        "avatar": "KWON_NH",
        "dialogue": "박용철 파트장님은 본인 인사고과와 위약금 걱정에 눈이 멀어 절차를 무시하고 계십니다.\n장애 수사 과정일수록 조사관님은 평정심을 유지하고 표준 대응 프로세스(ITIL)를 따라야 합니다.\n\n단순히 눈앞의 장애 현상(Incident)만 땜질 조치하는 게 아니라,\n근본적인 내부 인프라 문제 원인(Problem)을 체계적으로 식별하고 품질 지식 데이터베이스로 관리하는 국제 서비스 관리 모범 표준 명칭이 있습니다.\n\n정식 절차 이수를 위해 이 프레임워크의 영문 소문자 4글자 약어를 터미널에 기재하여 수사 규정을 성립하십시오.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>📚 IT SERVICE GOVERNANCE FRAMEWORK</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;'>\n        힌트: 정보 기술 인프라 라이브러리(IT Infrastructure Library)의 영문 앞글자들을 딴 4글자 약어로, 전 세계 IT 부서의 표준 운영 가이드라인입니다.\n    </p>\n</div>"
    },
    {
        "stage": 9,
        "title": "Knowledgebase (지식 정보 조회)",
        "filename": "cee89b5e.html",
        "verify_hash": "27dce682e1ad2f2106be21d27e8025de5de7ee65cecc737d4f27a33af4c29a8a",
        "speaker": "권남훈 & 박재욱",
        "role": "파트장 vs DBA (대립 관계)",
        "avatar": "PARK_JW",
        "dialogue": "VDI 로그상 박 차장의 백업 기동과 DB 블록 파손 시각이 겹친다며 권남훈 파트장이 압박을 해오기 시작합니다.\n\n[권남훈]: VDI 보안 로그는 완벽합니다. 본인이 백업 명령 수동으로 날려 과부하로 디스크 깬 것이니 징계 절차 밟으시죠.\n\n[박재욱]: 권 파트장님! 억울합니다! VDI 접속도 전에 하부 스토리지 물리 볼륨 복제가 먼저 깨져서 DB 데이터가 파손된 겁니다!\n\n[권남훈]: 그럼 지식 관리 포털(KB)에서 그 주장을 증명할 정식 장애 대응 매뉴얼 코드를 대십시오. 못 대면 독박입니다.\n\n[박재욱]: 조사관님! 지식 포털에서 '스토리지 동기화 실패로 인한 DB 파손 대응 매뉴얼'의 문서 코드 4자리를 찾아 저들의 주장을 꺾어주십시오!",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔍 KNOWLEDGEBASE DOCUMENT LIST</div>\n    <div style='max-height: 200px; overflow-y: auto; border: 1px solid var(--border-color); border-radius: 4px; background: rgba(0,0,0,0.45); text-align: left;'>\n        <table style='width: 100%; border-collapse: collapse; font-size: 0.8rem; color: var(--text-primary);'>\n            <tr style='position: sticky; top: 0; background: #080b11; color: var(--accent-blue); border-bottom: 1px solid var(--border-color); font-weight: bold;'>\n                <th style='padding: 6px;'>문서코드</th>\n                <th style='padding: 6px;'>기술 문서 주제</th>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>KB-1042</td>\n                <td style='padding: 5px 6px;'>L4 로드밸런싱 가용성 튜닝 규격</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>KB-3129</td>\n                <td style='padding: 5px 6px;'>코어 WAS JVM 가비지 컬렉터(GC) 상세 파라미터</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>KB-4021</td>\n                <td style='padding: 5px 6px;'>방화벽 포트 접근제어 규칙 설계지침</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>KB-5509</td>\n                <td style='padding: 5px 6px;'>내부망 VDI 세션 세그먼테이션 규정집</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>KB-6102</td>\n                <td style='padding: 5px 6px;'>리눅스 커널 패닉 인터럽트 시그널 복구 프로세스</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>KB-7108</td>\n                <td style='padding: 5px 6px;'>웹 애플리케이션 서버 커널 시스템 세팅 규격</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px; color: var(--text-primary); font-weight: normal;'>KB-8204</td>\n                <td style='padding: 5px 6px;'>스토리지 동기화 실패로 인한 DB 파손 대응 매뉴얼</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>KB-8890</td>\n                <td style='padding: 5px 6px;'>도커 컨테이너 라이프사이클 관리 표준 가이드</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>KB-9112</td>\n                <td style='padding: 5px 6px;'>액티브-액티브 DB 이중화 동기화 복구 표준</td>\n            </tr>\n            <tr style='border-bottom: 1px solid rgba(0,229,255,0.05);'>\n                <td style='padding: 5px 6px;'>KB-9321</td>\n                <td style='padding: 5px 6px;'>L4 네트워크 로드밸런서 VIP 이중화 스키마</td>\n            </tr>\n            <tr>\n                <td style='padding: 5px 6px;'>KB-9854</td>\n                <td style='padding: 5px 6px;'>외부 침입 차단 시그니처 룰셋 설계서</td>\n            </tr>\n        </table>\n    </div>\n</div>"
    },
    {
        "stage": 10,
        "title": "The Cronjob (Crontab 스케줄링)",
        "filename": "524cfb66.html",
        "verify_hash": "318fb6b0fd6eb7ef86613797123429db40159a50c0b443197c3a229ecefc07fb",
        "speaker": "김진혁 차장",
        "role": "네트워크 담당",
        "avatar": "KIM_JH",
        "dialogue": "흥, 박재욱 차장님도 참 핑계가 좋으시네요. 스토리지 핑계를 대다니요?\n장애 로그를 보면 본인이 새벽에 백업 스크립트를 수동으로 임의 가동해서 과부하로 디스크를 깨트린 게 뻔히 보입니다.\n\n[박재욱]: 아닙니다! 전 수동으로 명령어를 친 적이 없습니다! 스케줄러가 돌았을 뿐입니다!\n\n[김진혁]: 그래요? 그럼 조사관님, 저기 박 차장의 서버에 설정된 예약 작업 스케줄(Crontab) 설정을 읽어보십시오.\n이 배치 작업이 매일 구동되는 시각(24시간 형식 4자리 HHMM)을 분석해서 보고하십시오. 수동 구동인지 스케줄 기동인지 검증해 봅시다.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⏰ TARGET CRONTAB CONFIGURATION</div>\n    <div style='background: #020306; font-family: var(--font-mono); padding: 15px; border-radius: 6px; border: 1px solid var(--border-color); text-align: center; font-size: 1.1rem; color: var(--accent-blue);'>\n        45 1 * * * /usr/sbin/backup.sh\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.5;'>\n        힌트: 크론탭 시간 설정 구조는 [분] [시] [일] [월] [요일] 순서입니다.\n        위 설정은 매일 '1시 45분'에 구동됨을 의미합니다. 포맷에 맞춰 4자리 숫자로 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 11,
        "title": "The Command (박주암 과장)",
        "filename": "e3307ab7.html",
        "verify_hash": "53c148b793bd0c621b03b40afe93b7c39bce8b4d00157bc10142b8a848af32ac",
        "speaker": "박주암 과장",
        "role": "WAS 담당 (눈물겨운 현장 담당자)",
        "avatar": "PARK_JA",
        "dialogue": "과부하 때문에 서버가 죽은 게 아닙니다! 제발 제 WAS 서버 콘솔 역사 기록을 봐주십시오!\n\n상사분들은 자꾸 제 관리 소홀이라며 경위서부터 쓰라고 하시는데, 로그 히스토리를 뜯어보니 셧다운 직전에 누군가가 제 ID를 도용해 WAS 터미널에 침투했습니다.\n\n그리고 오라클 데이터베이스에 수동 접속하기 위해 전용 질의 클라이언트를 실행해 강제 DB 중단 명령을 날렸습니다!\n\n이 침입자가 WAS 서버에서 데이터베이스 관리자 계정 접속을 위해 실행한 유틸리티 명령어(영어 소문자)가 무엇인지 조사관님이 터미널에 입력해 입증해 주십시오!",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>💻 INCIDENT COMMAND HISTORY DUMP</div>\n    <p style='font-family: var(--font-mono); color: var(--text-primary); font-size: 0.95rem; line-height: 1.6;'>\n        $ cd /u01/app/oracle/product/12.1.0/dbhome_1/bin<br>\n        $ ./sqlplus / as sysdba<br>\n        &gt; SHUTDOWN IMMEDIATE;<br>\n        <span style='color: var(--accent-red);'>[02:13:21] DISCONNECTED FROM DATABASE.</span>\n    </p>\n</div>"
    },
    {
        "stage": 12,
        "title": "The Network Lie (김진혁 차장)",
        "filename": "16417f5b.html",
        "verify_hash": "debdc6fdb6c19c94ff78b653767bfac108d84ed51a54a58a72866dc635b15729",
        "speaker": "김진혁 차장",
        "role": "네트워크 담당 (여유만만한 목격자)",
        "avatar": "KIM_JH",
        "dialogue": "하하, 박 과장님. 원격으로 침입했다니요? 우리 네트워크망은 철저하게 통제되어 있었습니다.\n\n장애 당시 저는 외부 휴게실 소파에 편하게 앉아, 노트북 무선 안테나를 이용해 T5004 라우터 허브 장비의 무선 신호를 안정적으로 잡고 망 상태를 지속적으로 모니터링하고 있었습니다.\n망 부하 수치는 완전히 정상 범위였습니다. 즉, 외부 네트워크 장애가 아닙니다!\n\n[박주암]: 김 차장님... 분명 무선 신호를 수신해 모니터링하셨다고 했습니까?\n\n[이재헌 과장]: 어라... 조사관님, 기계실 랙에 꽂힌 T5004 장치 하드웨어 매뉴얼을 보니 이상한 점이 있습니다. 아스키 도면을 분석해서 김 차장 진술의 물리적 거짓말 요소를 밝혀내십시오!",
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
        "dialogue": "와, 김진혁 차장님! 무선 기능이 아예 없는 깡통 유선 장비를 무선으로 잡고 일했다고 거짓말을 하신 겁니까?\n점점 수상해지는군요...\n\n[이재헌]: 아, 그리고 파트장님. 저는 물리 서버 자원을 평소에 아주 풍부하게 할당해 두어 넉넉한 튜닝 상태를 유지했다고 장담합니다. 자원 부족으로 죽은 게 절대 아닙니다!\n\n[박용철]: 이재헌 과장! 자네의 그 넉넉하다는 튜닝 세팅을 보게! CPU 자원 사용률이 99.6%에 육박하고 남은 마진이 단 0.4%뿐이네! 숨이 깔딱깔딱 넘어가고 있었다고!\n\n조사관님, 이 과장의 허술한 주장을 반박하기 위해, 시스템의 목숨만 간신히 붙여놓은 임계 자원 할당 상태를 의미하는 IT 용어(영문 소문자 7자)를 기입하십시오!",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>⚙️ VM INSTANCE SPECIFICATION OVERVIEW</div>\n    <div class='cpu-widget'>\n        <div>INSTANCE_NAME: Core-WAS-01</div>\n        <div class='cpu-bar'>CPU USAGE: [██████████] 99.6% (Overload)</div>\n        <div style='color: var(--accent-magenta); margin-top: 5px;'>AVAILABLE_MARGIN: 0.4%</div>\n    </div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; margin-top: 10px; line-height: 1.6;'>\n        CPU 여유 마진이 0.4%밖에 되지 않는 위태로운 상태입니다.<br>\n        서버 튜닝이 충분히 넉넉한 상태가 아니라, 자원이 고갈 직전이어서 물리 장비의 숨통만 겨우 붙여놓은 한계 튜닝 상태를 의미하는 IT 영단어(영문 소문자 7자)를 기입하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 14,
        "title": "The Motivation (박용철 총괄)",
        "filename": "c70ec350.html",
        "verify_hash": "838940b6f1deea2e9aca2c69a4df9a484139e1d8ab954a1b2366df3777ae416b",
        "speaker": "박용철 파트장",
        "role": "품질총괄 (예민한 리더)",
        "avatar": "PARK_YC",
        "dialogue": "김 차장의 무선 신호 진술도 거짓이고, 이 과장의 넉넉하다는 서버 세팅도 개판이었군요!\n엉망진창입니다!\n\n자네들 다 비켜서세요! 조사관님, 데이터베이스가 파손되기 직전에 발생한 치명적인 디스크 논리 파손 오류 덤프를 가져왔습니다.\n이 디스크 블록 무결성 실패와 하부 스토리지 단절을 증명하는 고유 패턴(정규식)을 실행시켜 오류 코드를 특정해 내야 합니다.\n\n정규표현식 매칭을 통해 검출한 오라클 고유 내부 에러 코드를 소문자로 기입하여 사건 보고서에 등록해 주세요. 어서요!",
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
        "dialogue": "흠, 스토리지 파손 에러 코드가 검출되었군요. 하지만 여전히 외부 원격 침입의 혐의점은 성립하지 않습니다.\n\n우리 센터의 엄격한 VDI 망 관리 규칙에 따르면, 사용자가 접속을 종료하는 즉시 할당되어 있던 사설 IP 주소는 풀(Pool)로 회수되며, 이후 새로 로그인하는 다른 사람에게 즉각 순차적으로 자동 재배포됩니다.\n\n즉, 특정 타인의 고정 IP를 악의적으로 강제 도용해 접속하는 행위는 논리적으로 차단되어 있습니다.\n\n이 사설 IP 동적 자동 분배 관리를 담당하는 네트워크 표준 프로토콜 약어(H C P D)의 아나그램을 풀어 입력하십시오. 조사관님, 우리 규칙의 신뢰성을 재확인해야 합니다.",
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
        "dialogue": "[SYSTEM LOG DUMP]:\n\n권남훈 파트장의 DHCP 규약 주장이 오히려 실마리를 던졌습니다.\n네트워크 스위치 콘솔 로그를 파헤쳐보던 중 결정적인 흔적이 나왔습니다.\n\n김진혁 차장이 장애 발생 30분 전, 스토리지 서브넷 라우팅 테이블 설정을 조작하면서 실수로 CIDR 마스크 대역 폭을 `/28` 로 아주 좁게 한정해 버린 작업 실수가 발견되었습니다.\n이로 인해 데이터베이스와 스토리지 간 물리 통신 대역이 갑자기 분리되어 단절된 것입니다!\n\n서브넷 마스크 `/28` 대역폭 등급에서 네트워크 대표 주소(ID)와 브로드캐스트를 차감하고, 실제 하드웨어 장비들에 정상 분배해 줄 수 있는 최대 유효 호스트 IP 개수를 구하십시오. 조사관님, 김 차장의 실수 규모를 파악해야 합니다.",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔢 CIDR SUBMETMASK SUITE: /28</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; line-height: 1.6;'>\n        - 전체 IP 주소 표현 비트: 32비트<br>\n        - 호스트 할당 비트수: 32비트 - 28비트 = 4비트 (2^4 = 총 16개 주소)<br>\n        - 사용 불가 특수한 주소: 2개 (네트워크 ID 주소 & 브로드캐스트 IP)<br>\n        - <strong style='color: var(--accent-magenta);'>계산 공식: 2^(32 - 28) - 2</strong>\n    </p>\n</div>"
    },
    {
        "stage": 17,
        "title": "SAN Storage (김진혁의 실수 2)",
        "filename": "0e3d9fd2.html",
        "verify_hash": "2fac394011e7d326f9c7ff5e532316be43ce2e7d88b4f1377f585e8c8c083672",
        "speaker": "박재욱 차장",
        "role": "DBA",
        "avatar": "PARK_JW",
        "dialogue": "역시! 제 잘못이 아니었습니다! 김진혁 차장이 라우팅 설정을 `/28` 로 잘못 건드리는 바람에 SAN 스토리지 스위치 통신 링크가 사망해서 제 배치가 깨진 거였어요!\n\n[박용철 파트장]: 김진혁! 자네 미쳤어? 라우팅을 `/28` 로 마음대로 조작해 놔서 스토리지가 끊긴 거잖아! 당장 해명해!\n\n[김진혁 차장]: 앗... 그건 단순한 일시적 라우팅 설정 변경 실수였습니다. 그 정도로 DB가 깨지지는...\n\n[박용철]: 시끄러워! 조사관님, 당장 끊겨버린 블록 저장소 연결 링크를 재수립해야 합니다. iSCSI 프로토콜 통신 채널을 강제 복구하기 위해, 해당 장치 포트 바인딩에 기본적으로 사용되는 표준 통신 TCP 포트 4자리를 기입해 주세요. 속도를 올려야 합니다!",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔌 PROTOCOL PORT CHECK: iSCSI TARGET</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;'>\n        힌트: 인터넷 소형 컴퓨터 시스템 인터페이스(iSCSI) 통신 프로토콜이 표준으로 점유하여 사용하는 포트 번호입니다.\n    </p>\n</div>"
    },
    {
        "stage": 18,
        "title": "Time Drift (이재헌의 실수)",
        "filename": "58addc3e.html",
        "verify_hash": "f020272c938ba0a213d31613fd5a1a8b053c693d489551f8b24e900db43d6873",
        "speaker": "이재헌 과장",
        "role": "서버 담당 (죄인 모드)",
        "avatar": "LEE_JH",
        "dialogue": "어휴... 면목 없습니다. 그리고 또 한 가지 고백할 게 있습니다.\n\n제가 서버 증설 당시 수동 시간 동기화(NTP) 작업을 하다가 스케줄을 꺼두는 중대한 실수를 범했습니다. 그 바람에 WAS 물리 서버의 시계 클럭이 실제 한국 표준시(VDI 시간)보다 정확히 '15분 느리게' 가고 있는 것을 확인했습니다...\n\nWAS의 감사 시스템 덤프 상 강제 중단 명령어(`sqlplus`)가 실행된 기록 시각은 '01:58'입니다.\n\n그렇다면 이 느려터진 서버 클럭 오차 15분을 정상적으로 보정한, 실제 세상의 진짜 셧다운 발생 표준 시각(HHMM)은 몇 시 몇 분이었겠습니까? 계산해서 터미널에 입력하십시오. 실제 침입 시간을 정확히 알아내야 합니다!",
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
        "dialogue": "모든 조각이 완벽하게 맞춰졌습니다!\n실제 세계 시간 기준으로 코어 WAS 서버 강제 다운 명령어(`sqlplus`)가 실행된 시각은 정확히 '02:13'이었습니다.\n\n사건 당일의 표준 VDI 사용자 망 타임라인을 보십시오.\nDBA 박재욱 차장은 백업을 마친 뒤 '02:05'에 공식 로그아웃하고 세션을 완전히 해제해 사용하던 사설 IP를 반납했습니다.\n\n권남훈 파트장의 완벽한 DHCP 규약에 따라, 당시 박 차장이 반납하고 비어 버린 IP 주소를 02:13 시점에 순차적으로 자동 재할당받아 접속한 흔적이 기계실 외부 휴게실 공유기로 잡혀 있습니다.\n\n당시 외부 무선(wifi) 신호를 수신해 모니터링을 진행했다며 치명적인 하드웨어적 모순의 거짓말을 늘어놓은 진짜 범인의 이름을 터미널에 입력하십시오!",
        "gimmick_html": "<div class='puzzle-container'>\n    <div class='puzzle-title'>🔎 REAL-TIME TIMELINE COMPARISON</div>\n    <p style='color: var(--text-muted); font-size: 0.85rem; line-height: 1.5;'>\n        누군가가 DHCP의 규약 허점을 이용하여 DBA 박 차장이 사용하다가 반납한 IP 주소를 곧바로 할당받아 악용한 물증을 확보했습니다.<br>\n        조직도 상의 진범 이름 3글자를 입력하십시오.\n    </p>\n</div>"
    },
    {
        "stage": 20,
        "title": "Ticket Closed (최종 결재)",
        "filename": "6c46331e.html",
        "verify_hash": "a4c3ed04a95a3da14a9d235c83d868bed7c0f45cf7f3faa751ee8f50598d2211",
        "speaker": "박용철 파트장",
        "role": "품질총괄 (예민한 리더)",
        "avatar": "PARK_YC",
        "dialogue": "진범이 드디어 잡혔군요! 김진혁 차장, 자네가 본인의 스위치 설정 실수를 은폐하려고 백업 중인 결산 DB를 망가뜨리고 WAS 서버 강제 셧다운 공작까지 꾸민 거였어!\n\n자네가 던진 거짓말(wifi 모니터링)이 자네의 발목을 완전히 낚아챘네!\n\n조사관님 덕분에 회사 전체를 집어삼킬 뻔한 음모와 장애를 완벽하게 해결했습니다. 진짜 최고의 활약이었습니다!\n\n장애 관제 티켓 최종 승인 서명을 하고 이 긴박했던 장애 티켓을 종결하기 위해, 확인 키 [ done ]를 기입해 결재를 마무리해 주십시오!",
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
