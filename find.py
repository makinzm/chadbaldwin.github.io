import os
parents = ["."]
ans = []
keyword="favicon.ico" #input()
while(len(parents)!=0):
    for parent in parents:
        parents.remove(parent)
        lst = os.listdir(parent)
        for file in lst:
            file_path = os.path.join(parent,file)
            if ".ico" in file_path or ".DS_Store" in file_path or ".git" in file_path or ".pdf" in file_path or ".gif" in file_path:
                continue
            if ".png" in file_path or "jpg" in file_path:
                continue
            # print(file_path)
            if os.path.isdir(file_path):
                parents.append(file_path)
            else:
                f = open(file_path, 'r')
                file_content = f.read()
                f.close()
                if keyword in str(file_content):
                    ans.append(file_path)
print()
[print(a) for a in ans]