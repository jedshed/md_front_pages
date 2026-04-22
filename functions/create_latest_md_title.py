import functions as func
from config import Config as conf
from pathlib import Path


def create_latest_md_title(meta_publish_date, meta_title, meta_sitename, do_func, do_display):

    ##### func_text
    func_text = ("CREATE LATEST MD TITLE")
    print(f"{func_text:<{conf.fpad}} ...")
    func.debug_delay_long()
    
    ##### do_func_check
    if not do_func:
        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... FUNC SKIPPED")
        func.debug_delay_long()
        return

    try:
        latest_md_title = f"{meta_publish_date} {meta_title} - {meta_sitename}"

        func.helper_update_remote_line(
            1, f"{func_text:<{conf.fpad}} ... DONE")
        func.debug_delay_long()
    except Exception as e:
        print(f"Failed to: {func_text:<{conf.fpad}} {e}")

    ##### display_process_latest_md_title
    display_text = f"--- DISPLAY {func_text}"
    if do_display:
        print(f"--- {latest_md_title}")
        func.debug_delay_long()
    else:
        print(f"{display_text:<{conf.fpad}} ... DISPLAY SKIPPED")
        func.debug_delay_long()
    return latest_md_title
