import os

def get_save_path():

    project_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    conf_file_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/'+'data_save_dir'
    conf_file = open(conf_file_path)
    target_path = project_path + '/' + conf_file.readline()

    if os.path.exists(target_path):
        conf_file.close()
        return target_path
    else:
        conf_file.close()
        return False