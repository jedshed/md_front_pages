''' CONFIG '''

from pathlib import Path
from datetime import datetime
import sys
import tomllib

class Config:
    def __init__(self,
                start_time,
                sys_executable,
                sys_platform,
                base_url,
                base_url_site,
                limit,
                project_name,out_folder_name,
                file_ext,
                out_folder_path,
                fpad,
                seperator1,
                seperator2,
                sleep_time,
                out_folder_subfolders,
                ROOT_DIR,
                yaml_frontmatter_path,
                version,
                log_file_name,
                tranx_path):

        self.start_time = start_time
        self.sys_executable = sys_executable
        self.sys_platform = sys_platform
        self.base_url = base_url
        self.base_url_site = base_url_site
        self.limit = limit
        self.project_name = project_name
        self.file_ext = file_ext
        self.out_folder_path = out_folder_path
        self.fpad = fpad
        self.seperator1 = seperator1
        self.seperator2 = seperator2
        self.sleep_time = sleep_time
        self.out_folder_name = out_folder_name
        self.out_folder_subfolders = out_folder_subfolders
        self.ROOT_DIR = ROOT_DIR
        self.yaml_frontmatter_path = yaml_frontmatter_path
        self.log_file_name = log_file_name
        self.version = version
        self.tranx_path = tranx_path



    ### Project Config
    ### project_name from toml file
    with open("pyproject.toml", "rb") as f: project_name = tomllib.load(f)["project"]["name"]
    ### project_version from toml file
    with open("pyproject.toml", "rb") as f: project_version = tomllib.load(f)["project"]["version"]
    ### Sys
    sys_executable = sys.executable
    sys_platform = sys.platform

    # ### Project Config
    # project_name = 'md_front_pages'
    # version = '_1.2'
    # sys_executable = sys.executable
    # sys_platform = sys.platform

    ### start_time for atexit
    start_time = f"{datetime.now():%Y-%m-%d--%H:%M:%S}"

    # Get the absolute path to the directory containing this file
    ROOT_DIR = Path(__file__).resolve().parent

    ### f-string padding
    fpad = 40

    ### sepertators
    seperator1 = '-' * 80
    seperator2 = '- ' * 38

    ### debug sleep durations (seconds)
    # sleep_duration_long = 1.0
    sleep_duration_long = 0
    sleep_duration_short = 0.05

    ### BS Config
    base_url = 'https://www.bbc.co.uk/news/topics/cpml2v678pxt'
    limit = 51

    # base_url = 'https://www.bbc.co.uk/news/topics/cpml2v678pxt'
    base_url_site = 'https://www.bbc.co.uk'

    file_ext = '.md'
    
    out_folder_name = '.md_front_pages'
    out_folder_path = Path.home() / out_folder_name

    out_folder_log_path = out_folder_path / 'log'
    out_folder_tmp_path = out_folder_path / 'tmp'
    out_folder_complete_path = out_folder_path / 'complete'


    # out_folder_subfolders = [out_folder_log_path,
    #                          out_folder_tmp_path,
    #                          out_folder_complete_path]


    log_file_name = 'log_url'

    tranx_path = '/mnt/POLITICS_VAULT/___INBOX/FRONT_PAGES/'

    yaml_frontmatter_path = ROOT_DIR / 'yaml_frontmatter'



