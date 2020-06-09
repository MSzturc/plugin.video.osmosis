import os
import bolt
import glob
import shutil

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
_src_dir = os.path.join(PROJECT_ROOT, 'src')
_tests_dir = os.path.join(PROJECT_ROOT, 'tests')

def dist_task(**kwargs):
    #Prepare directories urls
    _dist_dir = os.path.join(PROJECT_ROOT, 'dist')
    _dist_dir = os.path.join(_dist_dir, os.path.basename(PROJECT_ROOT))
    _res_dir = os.path.join(PROJECT_ROOT, 'resources')
    
    #Cleanup
    shutil.rmtree(_dist_dir, ignore_errors=True)
    
    #Copy ressources directory
    copy(_res_dir,_dist_dir,'*.*')

    #Copy single files
    shutil.copy(os.path.join(PROJECT_ROOT, 'addon.xml'), _dist_dir)
    shutil.copy(os.path.join(PROJECT_ROOT, 'changelog.txt'), _dist_dir)
    shutil.copy(os.path.join(PROJECT_ROOT, 'default.py'), _dist_dir)
    shutil.copy(os.path.join(PROJECT_ROOT, 'service.py'), _dist_dir)
    shutil.copy(os.path.join(PROJECT_ROOT, 'LICENSE'), _dist_dir)

    #Distribute to Kodi
    _kodi_dir = '/Users/matt/Library/Application Support/Kodi/addons/plugin.video.osmosis/'
    shutil.rmtree(_kodi_dir, ignore_errors=True)
    shutil.copytree(_dist_dir, _kodi_dir)
    os.system("open /Applications/Kodi.app")
    

bolt.register_task('dist', dist_task)

def copy(src, dest,ext):
    for file_path in glob.glob(os.path.join(src, '**',  ext), recursive=True):
        new_path = os.path.join(dest, os.path.relpath(file_path))
        if os.path.isdir(file_path) != True:    
            os.makedirs(os.path.dirname(new_path), exist_ok=True)
            shutil.copy(file_path, new_path)


config = {
    'pip': {
        'command': 'install',
        'options': {
            'r': 'requirements.txt'
        }
    }
}