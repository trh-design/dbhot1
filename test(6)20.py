import zipfile
import os

def zip_dir(dirname, zipname):
    filelist = []
    if os.path.isfile(dirname): 
        filelist.append(dirname)
    else:
        for root, dirs, files in os.walk(dirname) :
            for name in files:
                filelist.append(os.path.join(root,name))
                
    zf = zipfile.ZipFile(zipname, "w", zipfile.zlib.DEFLATED)
    
    for tar in filelist:
        arcname = tar[len(dirname):]
        zf.write(tar, arcname)
        
    zf.close()
    
zip_dir("/path/to/directory", "output.zip")