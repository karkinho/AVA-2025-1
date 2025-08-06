import pandas as pd
import matplotlib.pyplot as plt
import sys 

avgMy = pd
avgProf = pd
My = pd
Prof = pd

def main():
    temp = ReadFile( "./res.csv" )
    My = temp[0]
    avgMy = temp[1]
    print(My)
    temp = ReadFile( "./resProf.csv" )
    Prof = temp[0]
    avgProf = temp[1]
    
    Avg( avgMy , avgProf )
    BoxPlot( My.groupby( "Size" ).agg(list) , Prof.groupby( "Size" ).agg(list)  )
    
def ReadFile( nameCSV ):
    var = pd.read_csv( nameCSV, names=["Matricula","Size","Time(ms)"])
    varAvg = var.groupby( "Size" ).mean()
    return [ var , varAvg ]

def BoxPlot( dataMy , dataProf ):
    for index , row in dataMy.iterrows(): 
        plt.boxplot( [ row["Time(ms)"] , dataProf.loc[index]["Time(ms)"] ] , tick_labels=[ "23200357" , "1313" ] )
        plt.title( "BoxPlot Of Entry Size %d" % index )
        plt.ylabel( "Execution Time(ms)" )
        plt.xlabel( "Matricula" )
        plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
        plt.savefig( "pdfs/boxplot-%d.pdf" % index )
        plt.close()
    
    
def Avg( dataMy , dataProf ):
    plt.style.use('default')
    plt.plot( dataMy.index , dataMy["Time(ms)"] , color='red' , label = "23200357"  )
    plt.plot( dataProf.index , dataProf["Time(ms)"] , color='blue' , label = "1313" )
    plt.scatter( dataMy.index , dataMy["Time(ms)"] , color='red' , marker = 'o',s=10 )
    plt.scatter( dataProf.index , dataProf["Time(ms)"] , color='blue' , marker = 'o',s=10 )
    plt.xscale( "log", base=2 )
    #plt.xticks( x , xTick )
    plt.title( "Average Of The Two Implementations" )
    plt.ylabel( "Execution Time(ms)" )
    plt.xlabel( "Entry Size" )
    plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
    plt.legend()
    plt.savefig( "pdfs/avg.pdf")
    
    plt.close()


main()