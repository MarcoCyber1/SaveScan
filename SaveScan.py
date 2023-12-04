from colorama import Fore
import nmap 

print(Fore.LIGHTCYAN_EX + """                                    ....xxxxx...,  '. '   
     ; . ` .  . : . .' :  . ..XXXXXXXXXXXXXXXXXXXXx.    `     .
.    .  .  .    . .   .  ..XXXXXXXXWWWWWWWWWWWWWWWWXXXX.  .     .     
        ' :  : . : .  ...XXXXXWWW   W88N88@888888WWWWWXX.   .   .       . .
   . ' .    . :   ...XXXXXXWWW    M88N88GGGGGG888^8M  WMBX.          .   ..  :
         :     ..XXXXXXXXWWW     M88888WWRWWWMW8oo88M   WWMX.     .    :    .
            XXXXXXXXXXXXWW       WN8888WWWWW  W8@@@8M    BMBRX.         .  : :
  .       XXXXXXXX=MMWW":  .      W8N888WWWWWWWW88888W      XRBRXX.  .       .
     ....    XXXXXMM::::. .        W8@889WWWWWM8@8N8W      . . :RRXx.    .
         ``...'''  MMM::.:.  .      W888N89999888@8W      . . :::: RXV    .  :
 .       ..'''''      MMMm::.  .      WW888N88888WW     .  . mmMMMMMRXx
      ..' .              MMmm .  .       WWWWWWW   . :. :,miMM    : `    .
   .                .         MMMMmm . .  .  .   ._,mMMMM     :  ' .  :
               .                    MMMMMMMMMMMMM .  : . '  MAID WITH < MARCO > """)  
print("Simple Scan Network, enter (help)\n")                                               
scanner = nmap.PortScanner()   
                                                                                                                                                                                           
target = input(Fore.LIGHTMAGENTA_EX + "=====> ")  

if target == "help":

   print("Usage: 192.168.1.1/24")
        
else:
   print("error!")
        

target = input(Fore.LIGHTMAGENTA_EX + "ip terget: ")

scanner.scan(target, arguments='-p 1-6553')
scanner.scan(target, arguments='-sV')                                                                                  
                                                                                                                                                                                                                                             
for host in scanner.all_hosts():                                                                                                   
    print(Fore.LIGHTGREEN_EX + 'Host: %s (%s)' % (host, scanner[host].hostname()))                                                                     
    print(Fore.CYAN + 'State: %s' % scanner[host].state())                                                                                    
    for proto in scanner[host].all_protocols():                                                                                    
        print(Fore.MAGENTA + 'Protocol: %s' % proto)                                                                                             
        ports = scanner[host][proto].keys()                                                                                        
        for port in ports:                                                                                                         
            print(Fore.RESET + 'Port: %s\tState : %s' % (port, scanner[host][proto][port]['state']))
            lport = scanner[host][proto].keys()                                                                                        
            for port in lport:                                            
                print(Fore.RED + "Service : %s" % scanner[host][proto][port]['name'])                                                             
                print("Version : %s" % scanner[host][proto][port]['version'])  
                print()
                
            
    print("""===================""")

