def byte_converter(bytes:int):
    
    kb = round(bytes / 1024, 1)
    mb = round(kb / 1024, 1)
    gb = round(mb / 1024, 1)
    
    return f"""{bytes} B\n{kb} KB\n{mb} MB\n{gb} GB"""

def solution_6():
    
    units = ("B", "KB", "MB", "GB")
    
    return byte_converter(537395200)
    
    

print(solution_6())