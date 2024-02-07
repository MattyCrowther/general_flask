import os
from datetime import datetime
from werkzeug.utils import secure_filename

def handle_upload(form,sess_dir):
    file_data = form.upload.data
    filename = file_data.filename
    filename = secure_filename(filename)
    secure_fn = os.path.join(sess_dir,filename)
    file_data.save(secure_fn)
    gn = filename.split(".")[0]
    return secure_fn,gn

def handle_paste(form,sess_dir):
    suffix = ".txt"
    if form.graph_name.data != "":
        gn = form.graph_name.data 
    else: 
        gn = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = os.path.join(sess_dir,f'{gn}{suffix}')
    with open(filename,"a+") as f:
        f.write(form.paste.data)
    return filename,gn