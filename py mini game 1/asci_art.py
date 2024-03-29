import time
import os
    
art1="""                     (            
     (                )\ )  *   )     
   ( )\      (   (   (()/(` )  /(  
   )((_)     )\  )\   /(_))( )(_)) 
  ((_)_   _ ((_)((_) (_)) (_(_())  
   / _ \ | | | || __|/ __||_   _|  
  | (_) || |_| || _| \__ \  | |    
   \__\_\ \___/ |___||___/  |_|    
                                  """
  
art2="""game over"""

art3="""                              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄
                  ⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠤⠤⠴⢶⣶⡶⠶⠤⠤⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⠁
                  ⠀⠻⣯⡗⢶⣶⣶⣶⣶⢶⣤⣄⣀⣀⡤⠒⠋⠁⠀⠀⠀⠀⠚⢯⠟⠂⠀⠀⠀⠀⠉⠙⠲⣤⣠⡴⠖⣲⣶⡶⣶⣿⡟⢩⡴⠃⠀
                  ⠀⠀⠈⠻⠾⣿⣿⣬⣿⣾⡏⢹⣏⠉⠢⣄⣀⣀⠤⠔⠒⠊⠉⠉⠉⠉⠑⠒⠀⠤⣀⡠⠚⠉⣹⣧⣝⣿⣿⣷⠿⠿⠛⠉⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⠀⠈⣹⠟⠛⠿⣿⣤⡀⣸⠿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠾⣇⢰⣶⣿⠟⠋⠉⠳⡄⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⢠⡞⠁⠀⠀⡠⢾⣿⣿⣯⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⢀⣿⣿⣯⢼⠓⢄⠀⢀⡘⣦⡀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⣰⣟⣟⣿⣀⠎⠀⠀⢳⠘⣿⣷⡀⢸⣿⣶⣤⣄⣀⣤⢤⣶⣿⡇⢀⣾⣿⠋⢀⡎⠀⠀⠱⣤⢿⠿⢷⡀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⣰⠋⠀⠘⣡⠃⠀⠀⠀⠈⢇⢹⣿⣿⡾⣿⣻⣖⠛⠉⠁⣠⠏⣿⡿⣿⣿⡏⠀⡼⠀⠀⠀⠀⠘⢆⠀⠀⢹⡄⠀⠀⠀
                  ⠀⠀⠀⢰⠇⠀⠀⣰⠃⠀⠀⣀⣀⣀⣼⢿⣿⡏⡰⠋⠉⢻⠳⣤⠞⡟⠀⠈⢣⡘⣿⡿⠶⡧⠤⠄⣀⣀⠀⠈⢆⠀⠀⢳⠀⠀⠀
                  ⠀⠀⠀⡟⠀⠀⢠⣧⣴⣊⣩⢔⣠⠞⢁⣾⡿⢹⣷⠋⠀⣸⡞⠉⢹⣧⡀⠐⢃⢡⢹⣿⣆⠈⠢⣔⣦⣬⣽⣶⣼⣄⠀⠈⣇⠀⠀
                  ⠀⠀⢸⠃⠀⠘⡿⢿⣿⣿⣿⣛⣳⣶⣿⡟⣵⠸⣿⢠⡾⠥⢿⡤⣼⠶⠿⡶⢺⡟⣸⢹⣿⣿⣾⣯⢭⣽⣿⠿⠛⠏⠀⠀⢹⠀⠀
                  ⠀⠀⢸⠀⠀⠀⡇⠀⠈⠙⠻⠿⣿⣿⣿⣇⣸⣧⣿⣦⡀⠀⣘⣷⠇⠀⠄⣠⣾⣿⣯⣜⣿⣿⡿⠿⠛⠉⠀⠀⠀⢸⠀⠀⢸⡆⠀
                  ⠀⠀⢸⠀⠀⠀⡇⠀⠀⠀⠀⣀⠼⠋⢹⣿⣿⣿⡿⣿⣿⣧⡴⠛⠀⢴⣿⢿⡟⣿⣿⣿⣿⠀⠙⠲⢤⡀⠀⠀⠀⢸⡀⠀⢸⡇⠀
                  ⠀⠀⢸⣀⣷⣾⣇⠀⣠⠴⠋⠁⠀⠀⣿⣿⡛⣿⡇⢻⡿⢟⠁⠀⠀⢸⠿⣼⡃⣿⣿⣿⡿⣇⣀⣀⣀⣉⣓⣦⣀⣸⣿⣿⣼⠁⠀
                  ⠀⠀⠸⡏⠙⠁⢹⠋⠉⠉⠉⠉⠉⠙⢿⣿⣅⠀⢿⡿⠦⠀⠁⠀⢰⡃⠰⠺⣿⠏⢀⣽⣿⡟⠉⠉⠉⠀⠈⠁⢈⡇⠈⠇⣼⠀⠀
                  ⠀⠀⠀⢳⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠈⢿⣿⣷⣌⠧⡀⢲⠄⠀⠀⢴⠃⢠⢋⣴⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⢠⠇⠀⠀
                  ⠀⠀⠀⠈⢧⠀⠀⠈⢦⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣧⠐⠸⡄⢠⠀⢸⠀⢠⣿⣟⡿⠋⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀⢀⡟⠀⠀⠀
                  ⠀⠀⠀⠀⠈⢧⠀⠀⠀⠣⡀⠀⠀⠀⠀⠀⠀⠈⠛⢿⡇⢰⠁⠸⠄⢸⠀⣾⠟⠉⠀⠀⠀⠀⠀⠀⠀⢀⠜⠁⠀⢀⡞⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠙⢄⠀⠀⠀⠀⠀⠀⠀⢨⡷⣜⠀⠀⠀⠘⣆⢻⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⣠⠎⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠑⠦⣀⠀⠀⠀⠀⠈⣷⣿⣦⣤⣤⣾⣿⢾⠀⠀⠀⠀⠀⣀⠴⠋⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢄⡀⢸⣶⣿⡑⠂⠤⣀⡀⠱⣉⠻⣏⣹⠛⣡⠏⢀⣀⠤⠔⢺⡧⣆⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢽⡁⠀⠀⠀⠀⠈⠉⠙⣿⠿⢿⢿⠍⠉⠀⠀⠀⠀⠉⣻⡯⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠲⠤⣀⣀⡀⠀⠈⣽⡟⣼⠀⣀⣀⣠⠤⠒⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⢻⡏⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
               


art4="""     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⣠⣤⡀⠀⠀⡀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢸⣧⠞⠁⡷⢿⣦⡀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣼⢪⡇⠀⠀⣷⣶⢹⡇⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⢹⠘⣷⣄⢳⣿⣿⣾⣗⡿⠀⠀⠀⠀⢀⣟⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠿⡄⠀⠀⠀⢸⠆⣿⣿⡏⣿⣿⣿⡗⣧⠀⠀⠀⠀⢸⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣄⢧⡀⣀⡴⠋⢀⣿⣿⣷⣿⣿⣿⡇⢩⡳⢤⣀⢠⣿⣟⣿⣿⠀⢀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⢫⠿⠟⢳⡇⠀⣼⣿⣿⣿⣿⣿⣿⣷⡀⢸⣷⡿⠟⠛⠛⢿⣿⣦⠓⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠑⠉⠀⠀⣾⡴⣾⡿⢹⠙⢿⡭⠭⠽⢿⣿⣿⡿⣅⣀⣀⣀⣰⣿⡟⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
             ⠀⠀⠀⠀⠀⠀⠀⢹⠋⠙⠛⢻⡿⣡⣿⠃⣸⡇⠈⠓⢤⣀⠈⠁⣿⡤⢤⣤⣬⠟⢻⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
               ⠀⠀⠀⠀⠀⡼⢀⣠⣴⣿⡟⠛⠁⠀⡏⠀⠀⠀⠂⢹⣷⣤⣾⣧⣶⣾⡍⢛⣿⣿⣿⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⣼⡵⠋⢹⣿⣿⣧⠀⠀⠀⡷⠀⠸⡷⣤⣴⡿⣿⣿⣿⣿⣵⣿⣶⣿⣿⡛⠒⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠂⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⡼⠛⢻⣿⡀⠀⠀⣇⣀⡆⣀⣼⣟⡂⣹⣿⣿⠻⣧⠀⠈⠉⣻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠊⠀⢀⡌⠀⠀⠀⠀
             ⠀⠀⠀⠀⠀⠀⠀⢀⣼⣧⣤⣼⣿⡇⠀⠀⣿⢿⣼⠟⠋⠹⣿⣿⣿⡏⠀⠹⣦⣤⣾⡿⣻⣟⣛⣦⡄⠀⠀⠀⠀⢠⠞⠁⠀⢠⠞⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⢹⣿⣿⣿⣿⡟⠳⡄⣿⣾⣿⠾⠿⠿⣿⡿⢿⠁⠀⠀⠹⣿⡿⠾⣿⣿⡅⢸⠃⠀⠀⢀⡴⠋⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠙⣿⣿⣿⡇⢄⠈⢿⡿⢁⣴⡾⢿⢿⣿⣿⣇⠀⠀⠘⣿⡁⠠⣿⣿⠳⡾⠀⢀⡴⠋⠀⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⢀⣼⠟⣿⣟⡀⠈⠑⣿⣿⣿⣭⣷⢾⣿⣿⣿⠿⣦⠀⠀⠹⣷⠈⢹⣿⣦⣵⡴⠋⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠡⠀⣴⢿⡾⠛⠀⣹⣆⠀⣸⣿⣿⣭⣾⡟⠻⣥⣐⣦⠈⡇⠀⠀⢹⡄⢸⣿⡇⡏⠀⠀⢀⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣧⢟⣿⣿⠟⢠⢃⡼⣿⡟⢷⣸⣿⣿⣿⣿⣿⣦⡈⠻⠛⠉⢳⠀⢐⣿⣧⠈⣿⡋⠁⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⢛⣾⣿⠋⢀⡼⠋⠀⣿⡇⠈⢻⢟⡟⣿⣿⣿⠙⣿⣦⣶⡖⠒⣷⣾⣿⡟⢳⣿⡗⢶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⣼⣿⣧⣤⡾⠁⠀⣀⣿⡇⠇⢀⡾⡇⣿⣧⣿⠀⠸⣿⣿⣿⠲⣼⠻⢿⣇⣺⣿⣧⣼⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⠃⢠⡾⠁⢹⡇⠀⠚⠁⣷⣿⠷⠘⢷⡄⠀⠀⢹⡆⢸⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⣀⣤⣿⣿⣿⡿⢸⣿⠁⠀⢸⣷⠀⠀⢸⢹⣿⣗⠂⠀⠹⣆⠀⠈⣿⢸⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢬⣹⣿⢿⣿⣿⡿⠋⠀⣾⡇⣠⣴⣿⣿⢦⡀⣼⣸⣿⣿⣦⡀⠀⢹⡆⠂⣿⣿⣿⣿⣿⣿⠛⢦⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠟⣻⢿⣿⣯⣀⡀⣼⣿⠋⠁⣈⣿⣿⣷⣻⣿⣿⣿⣿⣿⣁⣀⢸⣿⣶⣿⣿⣿⣿⣿⣿⣷⡈⢧⡘⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣯⠞⠁⣠⠿⠛⠻⢱⣿⡇⠠⠾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⣿⡻⣿⣿⣿⣆⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢞⣿⠏⠀⣰⠋⠀⠀⠀⢀⣿⡟⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣬⣭⣿⣿⣿⣦⣝⢷⣄⠙⢿⣿⣷⣌⠃⢀⠀⠀⠀⠏⠉⠛⠳⠄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⡴⢫⠞⠁⢀⡾⠁⠀⠀⠀⠀⣼⣿⣠⡶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡟⢿⣿⣿⣯⡳⣝⠷⣿⣿⣟⠿⠻⢦⣄⡀⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⠋⡴⠃⢀⡴⠋⠀⠀⠀⠀⣠⢰⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⢸⣿⣿⣿⣿⣾⣿⣿⠿⡟⠶⣤⣄⡙⠙⢦⣝⠷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡴⠃⠈⢀⣴⠋⠀⠀⠀⠀⠀⢠⢧⣿⣿⣿⢣⡿⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣍⠙⠳⢶⣌⠁⠈⢳⡄⠀⠀⠀⠀
⠀⠀⠀⠀⣸⠁⣀⡴⠛⠁⠀⠀⠀⠀⠀⢠⢏⣿⣿⣿⠹⡟⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣙⠓⠈⠀⠁⠀⠀⠀⠀
"""

art5="""             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
             ⠀⠀⠀⠀⠀⠀⠀⠀⠤⢴⣾⣿⣿⣿⣯⠘⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
             ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡟⣾⣿⣿⣠⢠⣀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
             ⠀⠀⠀⠀⠀⠀⠀⠒⢫⣿⣿⣿⣿⣿⣿⢸⡗⣾⣙⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
             ⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣧⢮⡯⣷⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
             ⠀⠀⠀⠀⠀⡐⣚⣛⡛⠛⠉⢹⣽⣿⣽⠮⠓⣫⣏⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀
             ⠀⠀⢀⣴⠟⠋⠩⠉⢩⣷⣾⣿⣽⣷⣿⠤⢋⡥⠚⠳⣾⡏⠉⠉⠙⠻⢦⡀⠀⠀
             ⠀⢀⡿⢁⠈⢀⡠⢔⣣⠟⠿⣿⣿⣿⣗⡪⠇⠀⣢⡾⠛⣮⡢⢄⡀⠐⡈⢻⡄⠀
             ⢰⣾⠷⠥⠉⠑⡪⣽⠧⠀⠀⠨⡻⣟⣿⠀⣠⠞⡁⠀⠀⠚⣯⣇⡊⠉⠬⠾⣻⡆
             ⢨⡿⠤⣆⣒⡬⠞⣿⡑⠀⠀⠀⠀⠈⢳⣞⠁⠀⠀⠀⠀⢁⣿⠳⢥⣒⣨⠤⢿⣅
             ⢻⣿⣿⢋⠁⠀⢰⡇⠀⠀⠀⢠⢞⢿⣭⡍⢻⢦⡀⠀⠀⠀⢼⡇⠀⠈⠝⣿⣿⡟
             ⠀⣹⡏⢀⣀⣀⣸⣇⣀⣀⣀⣘⣛⣾⢶⠿⠿⣷⣽⡟⠓⢲⠶⠧⢤⣀⡠⢸⣏⠀
             ⢠⣿⡟⡿⡝⠀⠐⠀⠁⠈⠈⡽⠁⠀⢸⣓⣚⣿⣿⠧⣤⣄⡀⠀⠀⠈⣽⣧⣿⡀
             ⠘⢷⣧⣿⢷⣤⣤⣴⡶⣶⣾⣷⢤⣤⢾⠭⢭⣿⣿⣿⣶⣭⣝⡛⠶⠶⣳⣼⣿⡇
             ⠀⠀⠙⠛⠛⠚⠛⠛⣿⣿⣿⣿⣟⣷⡿⠓⠛⠻⠿⢿⠟⢿⠉⠛⠻⠯⠴⠶⠛⠁
             ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣽⡯⢿⣿⡟⠷⠶⢲⡖⠶⢼⣴⣾⣔⠀⠀⠀⠀⠀⠀⠀
             ⠀⠀⠀⠀⠀⠀⢀⡾⠁⠈⠛⠷⣾⣧⠀⠀⢸⣶⢾⠛⠉⠔⢿⣂⠀⠀⠀⠀⠀⠀
             ⠀⠀⠀⠀⠀⠀⣼⠍⠂⠀⢠⢣⣿⣷⠀⠄⢸⣿⡞⡄⠀⠀⡨⢷⠆⠀⠀⠀⠀⠀
             ⠀⠀⠀⠀⠀⢸⡣⣄⡀⠀⣎⣿⣿⣿⠀⡀⢺⣿⣿⡸⡀⢀⡰⢝⡧⠀⠀⠀⠀⠀
             ⠀⠀⠀⠀⠀⠀⠉⠓⠮⠽⣼⠛⠿⠿⠤⠤⠿⠿⠛⢷⠯⠵⠚⠋⠀⠀⠀⠀⠀⠀"""
             
art6="""⠀⣀⣤⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀
⣴⡟⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣶⠿⠟⢿⣆⠀⢀⣼⠿⠿⣷⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⢷⣄⠀
⣿⣰⣧⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠛⠉⠉⠁⠀⠀⠘⢿⣶⣿⠏⠀⠀⠈⠛⠋⠛⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣇⣌⣿⡄
⠻⣿⡏⣠⣿⣿⣦⣤⣀⠀⠀⣀⣀⣀⣀⢀⣴⣾⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣯⢿⣿⣼⠇
⠀⢿⣷⣿⡄⠘⣡⡾⢛⡿⣿⠿⣿⠟⢻⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⡿⢿⣿⣷⣶⣶⡾⣿⡛⢿⣁⢷⣬⣿⠏⠀
⠀⠈⠻⣿⣇⣸⣧⣿⢩⡴⢇⠐⠁⠀⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⠀⠘⢦⡹⣦⡳⢦⡓⣆⢸⣾⣿⠟⠀⠀
⠀⠀⠀⠈⢙⣿⠿⣿⣿⣧⣸⠀⢰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⣇⢡⣿⣾⣿⣿⣾⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠻⣦⣌⡛⠿⣷⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣷⣠⣿⡿⢟⣉⣵⡿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢷⣭⣛⢿⡄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠿⣟⣥⡶⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠈⢻⣧⡇⣟⠉⣉⡅⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠛⢿⣾⣡⡾⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣆⡀⢠⣿⢀⣼⣏⣷⠶⣦⣤⣤⣀⠀⠀⠀⢠⡘⠿⣿⠿⠇⡄⠀⠀⠀⢀⣀⣀⣤⣾⣯⡳⣌⣸⣿⡁⠀⢀⣼⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⣙⠿⢿⡟⠘⣿⡿⠀⣀⣀⣀⠰⣌⠁⠀⠀⠀⢱⡄⠀⢠⡞⠀⠀⠀⠘⣹⠉⢉⣁⠀⠘⣿⡿⠇⣻⣷⣶⠟⠹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⣿⠆⡟⠙⣻⠗⡶⢛⣡⣾⣿⢿⣿⣿⣿⣆⠀⠀⠀⠈⣿⠀⣿⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣦⡘⠷⣤⢹⡿⠖⣷⢠⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⢸⣇⠀⠁⠀⣿⡘⣿⡿⣯⠸⣧⠛⢛⣿⣷⡀⠀⢰⣿⠀⣿⡆⠀⢀⣾⣿⠻⠟⣽⠇⣿⣿⣿⠇⣾⠀⠑⠀⢸⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⢻⣆⠀⠀⠈⠙⢻⣷⣜⠦⠈⠁⠀⠀⣹⡿⣿⣿⠿⠿⠿⣿⣿⣿⣋⠈⠀⠈⢁⣰⢏⣿⡿⠟⠁⠀⠀⢀⡿⢠⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣆⡙⢇⣀⣀⣀⠀⠙⠛⠳⠶⠒⠂⢀⣀⣼⠇⠀⠀⠀⠀⠀⠹⣦⣉⡀⠢⠤⠤⠶⠿⠛⠀⠀⠀⠀⢰⠛⣡⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠛⢉⣭⣭⣤⣤⣀⠀⠀⠀⣴⠟⢉⠻⣄⠀⠀⠀⠀⠀⣠⠟⠙⢿⡆⠀⠀⠀⠀⣀⣨⣝⡒⠒⢷⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣠⣿⡿⠿⣿⣮⣍⠉⠉⠁⠘⢦⠙⠿⠷⠦⠄⠀⠤⠴⠶⡿⠗⠼⠃⠙⠓⠛⣉⣽⣿⣿⣿⣦⡈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠠⣄⣀⣤⣴⣿⡟⠁⠀⠀⠈⢻⣿⣿⣶⣤⣤⣤⣴⣶⣶⣧⣀⣀⣠⣶⣦⣤⣤⣄⣤⣤⣴⣾⣿⡟⠁⠀⠈⠻⣿⣯⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣧⣤⣤⠴⠂⢸⡟⢹⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⠙⣿⠓⠶⣤⣀⣀⣽⣿⣿⣿⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠘⠀⢸⡇⠀⣿⡟⢁⠹⣿⡟⠉⠛⠙⣿⣿⢉⠙⣿⡇⠀⢻⡇⠘⠇⠀⠈⠉⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⠏⣶⢿⡁⠀⠀⠀⢸⢿⡏⢷⣿⣷⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠴⠿⠟⠁⠀⢻⡀⠁⠀⠀⠀⠉⢸⠃⠈⠻⠿⢷⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⢀⡄⠀⡄⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣦⣾⢁⠀⣸⣦⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣾⣾⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⢿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""             

art7="""
██╗░░██╗███╗░░██╗██╗░██████╗░██╗░░██╗████████╗░██████╗  ░█████╗░███████╗
██║░██╔╝████╗░██║██║██╔════╝░██║░░██║╚══██╔══╝██╔════╝  ██╔══██╗██╔════╝
█████═╝░██╔██╗██║██║██║░░██╗░███████║░░░██║░░░╚█████╗░  ██║░░██║█████╗░░
██╔═██╗░██║╚████║██║██║░░╚██╗██╔══██║░░░██║░░░░╚═══██╗  ██║░░██║██╔══╝░░
██║░╚██╗██║░╚███║██║╚██████╔╝██║░░██║░░░██║░░░██████╔╝  ╚█████╔╝██║░░░░░
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░  ░╚════╝░╚═╝░░░░░

            ██╗░░░██╗░█████╗░██╗░░░░░░█████╗░██████╗░
            ██║░░░██║██╔══██╗██║░░░░░██╔══██╗██╔══██╗
            ╚██╗░██╔╝███████║██║░░░░░██║░░██║██████╔╝
            ░╚████╔╝░██╔══██║██║░░░░░██║░░██║██╔══██╗
            ░░╚██╔╝░░██║░░██║███████╗╚█████╔╝██║░░██║
            ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝"""

art71="""██╗░░██╗███╗░░██╗██╗░██████╗░██╗░░██╗████████╗░██████╗  ░█████╗░███████╗
██║░██╔╝████╗░██║██║██╔════╝░██║░░██║╚══██╔══╝██╔════╝  ██╔══██╗██╔════╝
█████═╝░██╔██╗██║██║██║░░██╗░███████║░░░██║░░░╚█████╗░  ██║░░██║█████╗░░"""

art72="""██╔═██╗░██║╚████║██║██║░░╚██╗██╔══██║░░░██║░░░░╚═══██╗  ██║░░██║██╔══╝░░
██║░╚██╗██║░╚███║██║╚██████╔╝██║░░██║░░░██║░░░██████╔╝  ╚█████╔╝██║░░░░░
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░  ░╚════╝░╚═╝░░░░░"""

art73="""            ██╗░░░██╗░█████╗░██╗░░░░░░█████╗░██████╗░
            ██║░░░██║██╔══██╗██║░░░░░██╔══██╗██╔══██╗
            ╚██╗░██╔╝███████║██║░░░░░██║░░██║██████╔╝"""

art74="""            ░╚████╔╝░██╔══██║██║░░░░░██║░░██║██╔══██╗
            ░░╚██╔╝░░██║░░██║███████╗╚█████╔╝██║░░██║
            ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝"""

def draw():
  print("Xx-----------------------------------xX")

if __name__ =="__main__":

 list=[art71,art72,art73,art74]
 for j in range(4):
  for i in list:
    print(i)
    time.sleep(0.5)
  os.system('cls') 
  time.sleep(0.5)

