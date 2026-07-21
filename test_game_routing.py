import os
import hashlib

# Target answer verification list
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
    "sqlplus",
    "wifi",
    "minimum",
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

print("Starting game integrity and routing verification...")

errors = 0
current_file = "a7f93b2c"  # Stage 1

for idx, ans in enumerate(answers):
    stage_num = idx + 1
    normalized_ans = "".join(ans.split()).lower()
    
    # 1. Calculate expected hashes
    expected_verify_hash = get_sha256(normalized_ans)
    next_file_hash = get_sha256(current_file + normalized_ans)[:8]
    
    html_filename = f"{current_file}.html"
    next_html_filename = f"{next_file_hash}.html"
    
    # 2. Check if current stage file exists
    if not os.path.exists(html_filename):
        print(f"[ERROR] Stage {stage_num:02d} file missing: {html_filename}")
        errors += 1
        continue
    
    # 3. Read and check verify hash inside HTML
    with open(html_filename, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check data-verify attribute
    search_str = f'data-verify="{expected_verify_hash}"'
    if search_str not in content:
        print(f"[ERROR] Stage {stage_num:02d} ({html_filename}) verify hash mismatch or missing!")
        errors += 1
    else:
        print(f"[OK] Stage {stage_num:02d} ({html_filename}) verify hash matching: {expected_verify_hash[:10]}...")
        
    # 4. Check if the NEXT stage file exists
    if not os.path.exists(next_html_filename):
        print(f"[ERROR] Stage {stage_num:02d} target next file {next_html_filename} is missing on disk!")
        errors += 1
    else:
        print(f"[OK] Stage {stage_num:02d} link connection target exists: {next_html_filename}")
        
    current_file = next_file_hash

# Check clear page specifically
clear_page = f"{current_file}.html"
if not os.path.exists(clear_page):
    print(f"[ERROR] Clear page file missing: {clear_page}")
    errors += 1
else:
    print(f"[OK] Clear page exists: {clear_page}")

if errors == 0:
    print("\nSUCCESS: All game stages, hashes, and files are 100% verified. No dead ends or hash mismatches detected!")
else:
    print(f"\nFAILURE: Detected {errors} error(s) during verification. Please inspect build script.")
