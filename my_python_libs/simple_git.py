from pathlib import Path



def check_for_git(path):
    if str(path.parent) == '/':
        return False, None
    git_path = [p for p in path.iterdir() if p.name == '.git']
    if len(git_path) == 1:
        return True, Path(git_path[0]) 
    else:
        return check_for_git(Path(path.parent))
def main():
    is_git, path = check_for_git(Path('.').cwd())
    if is_git:
        branches = Path(str(path) + '/refs/heads').iterdir()
        for branch in branches:
            print(branch.name)
        return
    print("[ERROR] no .git found.")

if __name__ == '__main__':
    main()
