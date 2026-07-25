import subprocess, os, shutil

project_dir = r'C:\Users\IN\.gemini\antigravity\scratch\jeonnam_maritime_curriculum'
temp_dir = r'C:\Users\IN\.gemini\antigravity\scratch\temp_kiamotors'

def run_cmd(cmd, cwd=project_dir):
    res = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    print(f"RUN {' '.join(cmd)} -> Code: {res.returncode}")
    if res.stdout: print("STDOUT:", res.stdout.strip())
    if res.stderr: print("STDERR:", res.stderr.strip())
    return res

# 1. kiamotors-excel 브랜치 생성 및 이동 (새 브랜치 orphan)
run_cmd(['git', 'checkout', '--orphan', 'kiamotors-excel'])

# 2. 현재 트래킹 파일 모두 제거
run_cmd(['git', 'rm', '-rf', '.'])

# 3. temp_kiamotors 에서 파일 복사 (.git 제외)
for item in os.listdir(temp_dir):
    if item == '.git':
        continue
    s = os.path.join(temp_dir, item)
    d = os.path.join(project_dir, item)
    if os.path.isdir(s):
        shutil.copytree(s, d, dirs_exist_ok=True)
    else:
        shutil.copy2(s, d)

# 4. Git add & commit & push
run_cmd(['git', 'add', '-A'])
run_cmd(['git', 'commit', '-m', 'Import kiamotors-excel curriculum into kiamotors-excel branch'])
run_cmd(['git', 'push', '-u', 'origin', 'kiamotors-excel'])

# 5. 다시 main 브랜치로 복귀
run_cmd(['git', 'checkout', 'main'])

# 6. 임시 폴더 삭제
if os.path.exists(temp_dir):
    shutil.rmtree(temp_dir)

print("ALL DONE SUCCESSFULLY!")
