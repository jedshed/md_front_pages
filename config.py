''' CONFIG '''

from pathlib import Path
from datetime import datetime
import sys
import tomllib

class Config:

    ### Project Config
    ### project_name from toml file
    with open("pyproject.toml", "rb") as f: project_name = tomllib.load(f)["project"]["name"]
    ### project_version from toml file
    with open("pyproject.toml", "rb") as f: project_version = tomllib.load(f)["project"]["version"]
    ### Sys
    sys_executable = sys.executable
    sys_platform = sys.platform


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
    limit = 50

    # base_url = 'https://www.bbc.co.uk/news/topics/cpml2v678pxt'
    base_url_site = 'https://www.bbc.co.uk'

    file_ext = '.md'
    
    out_folder_name = '.md_front_pages'
    out_folder_path = Path.home() / out_folder_name

    out_folder_log_path = out_folder_path / 'log'
    out_folder_tmp_path = out_folder_path / 'tmp'
    out_folder_complete_path = out_folder_path / 'complete'


    log_file_name = 'log_url'

    tranx_path = '/mnt/POLITICS_VAULT/___INBOX/FRONT_PAGES/'

    yaml_frontmatter_path = ROOT_DIR / 'yaml_frontmatter'



