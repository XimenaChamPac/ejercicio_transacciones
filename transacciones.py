import pandas as pd
#Este ejercicio es para comprender como se realiza algunas operaciones detransacciones bancarias
'''
Este codigo lee un archivo csv "transacciones_bancarias" para luego realizar un reporte
con la siguiente información:
- Balance final = [sumatoriade montos de Trans. de Credito]-[sumatoriade montos de Trans. de Dévito]
- Transacción de Mayor Monto = Id y monto de la transacción con mayor valor
- Total de transacciones = Número total de trans. de Crédito 
                           Número total de trans. de Dévito 
'''
def procesar_transacciones(archivo_csv):
    #df = pd.read_csv(archivo_csv)
    df = pd.read_csv(archivo_csv, encoding='latin1')  # o cp1252


    credito_total = df[df["tipo"] == "Crédito"]["monto"].sum()
    debito_total = df[df["tipo"] == "Débito"]["monto"].sum()
    balance_final = credito_total - debito_total

    transaccion_mayor = df.loc[df["monto"].idxmax()]
    id_mayor = transaccion_mayor["id"]
    monto_mayor = transaccion_mayor["monto"]

    conteo_credito = (df["tipo"] == "Crédito").sum()
    conteo_debito = (df["tipo"] == "Débito").sum()

    print("\nReporte de Transacciones")
    print("---------------------------------------------")
    print(f"Balance Final: {balance_final:.2f}")
    print(f"Transacción de Mayor Monto: ID {id_mayor} - {monto_mayor:.2f}")
    print(f"Total de Transacciones:")
    print(f"  - Número total de trans. de Crédito: {conteo_credito} ")
    print(f"  - Número total de trans. de Débito: {conteo_debito}")

# Cambia el nombre del archivo CSV si es necesario
procesar_transacciones("ejercicioTransacciones.csv")