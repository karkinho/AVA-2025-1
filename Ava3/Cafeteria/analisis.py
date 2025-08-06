import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = pd.read_csv( "result.csv" )
    data.columns=["RunTime" , "Média Chegada Cliente", "Média Tempo Atendimento","Clientes Atendidos", "Média de Espera", "Média Total" , "Utilização" ]
    data.drop('RunTime', axis=1, inplace=True)
    

    
    data1 = data[data["Média Chegada Cliente"] == 5].groupby( "Média Tempo Atendimento" ).mean().reset_index()
    data2 = data[data["Média Chegada Cliente"] == 10].groupby( "Média Tempo Atendimento" ).mean().reset_index()
    data3 = data[data["Média Chegada Cliente"] == 20].groupby( "Média Tempo Atendimento" ).mean().reset_index()
    data4 = data[data["Média Chegada Cliente"] == 40].groupby( "Média Tempo Atendimento" ).mean().reset_index()
    
    result = pd.concat([data1, data2, data3, data4], axis=0, ignore_index=True)

    DoPdf(result)

def DoPdf( data ) :
    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=data.values, colLabels=data.columns, loc='center')
    plt.savefig("table_output.pdf")
    
main()