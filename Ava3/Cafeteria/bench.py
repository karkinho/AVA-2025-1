import subprocess as sb
import sys

def main():
    run_time = sys.argv[1]
    configs = [ "5 5" , "10 10", "5 10", "10 5", "40 40", "20 40", "40 20", "20 20" ]
    file = open( "result.csv", "w" )
    
    for config in configs:
        for i in range( 0 , 30 ):
            file.write( sb.run( [ "python", "cafeteria.py", config.split( " " )[0], config.split( " " )[1], run_time ] , capture_output=True, text=True).stdout)


main()