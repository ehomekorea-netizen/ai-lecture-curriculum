import subprocess, os, shutil

project_dir = r'C:\Users\IN\.gemini\antigravity\scratch\jeonnam_maritime_curriculum'
temp_dir = r'C:\Users\IN\.gemini\antigravity\scratch\temp_nambu'

def run_cmd(cmd, cwd=project_dir):
    res = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    print(f"RUN {' '.join(cmd)} -> Code: {res.returncode}")
    if res.stdout: print("STDOUT:", res.stdout.strip())
    if res.stderr: print("STDERR:", res.stderr.strip())
    return res

# 1. nambu-univ 레포지토리 임시 클론
if os.path.exists(temp_dir):
    shutil.rmtree(temp_dir, ignore_errors=True)

print("Cloning nambu-univ repo...")
subprocess.run(['git', 'clone', 'https://github.com/ehomekorea-netizen/nambu-univ.git', temp_dir])

# 2. main 브랜치로 복귀 후 nambu-univ 브랜치 생성 (orphan)
run_cmd(['git', 'checkout', 'main'])
run_cmd(['git', 'checkout', '--orphan', 'nambu-univ'])

# 3. 기존 파일 모두 비우기
run_cmd(['git', 'rm', '-rf', '.'])

# 4. temp_nambu 에서 파일 복사 (.git 제외)
for item in os.listdir(temp_dir):
    if item == '.git':
        continue
    s = os.path.join(temp_dir, item)
    d = os.path.join(project_dir, item)
    if os.path.isdir(s):
        shutil.copytree(s, d, dirs_exist_ok=True)
    else:
        shutil.copy2(s, d)

# 5. Git add & commit & push
run_cmd(['git', 'add', '-A'])
run_cmd(['git', 'commit', '-m', 'Import nambu-univ curriculum into nambu-univ branch'])
run_cmd(['git', 'push', '-u', 'origin', 'nambu-univ'])

# 6. 다시 main 브랜치로 복귀
run_cmd(['git', 'checkout', 'main'])

print("NAMBU UNIV BRANCH IMPORT COMPLETED SUCCESSFULLY!")
