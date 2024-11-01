def get_subfiles(a_dir):
    '''
    Return the names of the files inside the input folder,
    and the full path of each file.
    '''
    import os
    return [[name, os.path.join(a_dir, name)] for name in os.listdir(a_dir)
            if os.path.isfile(os.path.join(a_dir, name))]