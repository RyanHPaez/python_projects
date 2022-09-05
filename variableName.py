def solution(name):
    if name[0].isnumeric() or ' ' in name:
        return False
    return name.isalnum() or "_" in name
