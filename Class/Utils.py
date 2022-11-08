from .Configuration import Configuration

TITLE = '''
   _____        __ _                           
  / ____|      / _| |                          
 | (___   ___ | |_| |___      ____ _ _ __ ___  
  \___ \ / _ \|  _| __\ \ /\ / / _` | '__/ _ \ 
  ____) | (_) | | | |_ \ V  V / (_| | | |  __/ 
 |_____/ \___/|_|  \__| \_/\_/ \__,_|_|  \___| 

 |  \/  |                                      
 | \  / | __ _ _ __   __ _  __ _  ___ _ __     
 | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|    
 | |  | | (_| | | | | (_| | (_| |  __/ |       
 |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|       
                            __/ |              
                           |___/                                            
'''

DESCRIPTION = '''
COMMAND LIST

  [W] = Up
  [S] = Down
  [ENTER] = Select Option
  Click Enter on the Run Option
'''

MENU: dict = {
    '- Settings': None,
    'Gnome Tweaks & Extensions': Configuration.gnome,
    'Alacritty': Configuration.alacritty,
    '- Software': None,
    'Neovim': Configuration.nvim,
    'Visual Studio Code': Configuration.vscode,
    'Discord': Configuration.discord,
    'Spotify': Configuration.spotify,
    'Chrome': Configuration.chrome,
    '- Programming Languages': None,
    'C++': Configuration.cpp,
    'Rust': Configuration.rust_lang,
    'Pascal': Configuration.pascal,
    '- Option': None,
    'Exit': exit,
    'Run': exit,
}
