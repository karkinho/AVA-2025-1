import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = pd.read_csv( "result.csv" )
    data.columns=["RunTime" , "Media Chegada Cliente", "Media Tempo Atendimento","Clientes Atendidos", "Media de Espera", "Media Total" , "Utilizacao" ]
    data.drop('RunTime', axis=1, inplace=True)
    

    
    data1 = data[data["Media Chegada Cliente"] == 5].groupby( "Media Tempo Atendimento" ).mean().reset_index()
    data2 = data[data["Media Chegada Cliente"] == 10].groupby( "Media Tempo Atendimento" ).mean().reset_index()
    data3 = data[data["Media Chegada Cliente"] == 20].groupby( "Media Tempo Atendimento" ).mean().reset_index()
    data4 = data[data["Media Chegada Cliente"] == 40].groupby( "Media Tempo Atendimento" ).mean().reset_index()
    
    result = pd.concat([data1, data2, data3, data4], axis=0, ignore_index=True)

    DoPdf(result)

def DoPdf( data ) :
    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=data.values, colLabels=data.columns, loc='center')
    plt.savefig("table_output.pdf")
    
main()