import subprocess, os, shutil

project_dir = r'C:\Users\IN\.gemini\antigravity\scratch\jeonnam_maritime_curriculum'

def run_cmd(cmd, cwd=project_dir):
    res = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    print(f"RUN {' '.join(cmd)} -> Code: {res.returncode}")
    return res

# 1. main 브랜치로 이동
run_cmd(['git', 'checkout', 'main'])

# 2. 각 서브 폴더 생성 및 브랜치별 파일 가져오기
branches = ['jeonnam-goheung', 'kiamotors-excel', 'nambu-univ']

for b in branches:
    folder_path = os.path.join(project_dir, b)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Copying content from branch {b} into folder {b}...")
    
    # 해당 브랜치로 임시 이동
    run_cmd(['git', 'checkout', b])
    
    # 파일들을 subfolder에 복사
    for item in os.listdir(project_dir):
        if item in [b, '.git', '.gitignore']:
            continue
        src = os.path.join(project_dir, item)
        dst = os.path.join(folder_path, item)
        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(src, item=dst)

# 다시 main 브랜치로 복귀
run_cmd(['git', 'checkout', 'main'])

print("All branch files copied into subfolders successfully!")
