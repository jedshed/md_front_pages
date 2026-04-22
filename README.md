# md_front_pages

## Description:
Gets latest bbc front pages url
Creates md file inc yaml frontmatter and
Moves md file to Obsidian Vault on network share

## IMPORTANT
- Use meta_filedate NOT meta_date for correct date

### To Do
- Create Path objects in config insread of in individual
  functions.  Def ouput folders, likely tranx folder too

- md final is currentlyt overwriting a file in tmp if
  it already exists.  This is mostly fine as the script
  is not run if the url is in the log.  However, if the
  script runs into problems it's possible that the tmp file
  should be explicilty deleted if it aleady exists in complete.

### Plans
- Download images to folder and update links to point to folder

### 1.3
- Functions and Main aligened with md_playbook as much as possible
- Main highlighted with FUNCS MATCH or UNIQUE for further development
- meta_publishdate var created and used to ensure date is always
  correct across projects 

### 1.2
- Complete redo of functions to incorporate do_func
- atexit added
- debug_functions added
- Fixed - Output folder creation now explicitly creates
  dot folder and child folders to avoid potental errors
  if any folders not present
- config project_name and project_version now pull from toml file 
- config url changed to base_url
- f-string padding added to print statement - width set in config
- get_url_latest modified adding curl-cffi
  to impersonte 'human' browser - web page had started bot-blocking