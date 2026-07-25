import subprocess, os, shutil, sys

project_dir = r'C:\Users\IN\.gemini\antigravity\scratch\jeonnam_maritime_curriculum'

def git(args):
    res = subprocess.run(['git'] + args, cwd=project_dir, capture_output=True, text=True)
    print(f"git {' '.join(args)} -> {res.returncode}")
    if res.stderr and res.returncode != 0:
        print("ERR:", res.stderr.strip())
    return res

branches = ['jeonnam-goheung', 'kiamotors-excel', 'nambu-univ']
subfolder_temp = r'C:\Users\IN\.gemini\antigravity\scratch\temp_branches'

if os.path.exists(subfolder_temp):
    shutil.rmtree(subfolder_temp, ignore_errors=True)
os.makedirs(subfolder_temp, exist_ok=True)

# 각 브랜치의 파일들을 temp_branches/[branch_name] 에 다 뽑아두기
for b in branches:
    git(['checkout', b])
    target_b_dir = os.path.join(subfolder_temp, b)
    os.makedirs(target_b_dir, exist_ok=True)
    
    for item in os.listdir(project_dir):
        if item in ['.git', '.gitignore']:
            continue
        src = os.path.join(project_dir, item)
        dst = os.path.join(target_b_dir, item)
        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dst)

# 다시 main 브랜치로 복귀
git(['checkout', 'main'])

# main 브랜치 하위에 서브폴더로 3개 배치
for b in branches:
    src_dir = os.path.join(subfolder_temp, b)
    dst_dir = os.path.join(project_dir, b)
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir, ignore_errors=True)
    shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)

# temp_branches 임시 폴더 삭제
shutil.rmtree(subfolder_temp, ignore_errors=True)

print("Subfolders consolidation done! Ready to commit and push to main.")
