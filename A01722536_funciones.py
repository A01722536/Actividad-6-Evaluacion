def funcion_1(archivo):
    import pandas as pd
    import os

    extension=os.path.splitext(archivo)[1].lower()
    if extension == ".csv":
        df = pd.read_csv(archivo)
        df = df.drop(columns="Unnamed: 0", errors="ignore")
        return(df)
    elif extension == ".xlsx":
        df = pd.read_excel(archivo)
        df = df.drop(columns="Unnamed: 0", errors="ignore")
        return(df)
    else:
        raise ValueError (f"Formato de archivo no soportado: {archivo}")

def funcion_2(df):
    import pandas as pd
    import os

    cuantitativas=df.select_dtypes(include=["float64","int64","float","int"])
    cualitativas=df.select_dtypes(include=["object","datetime","category"])

    cuantitativas_pares=cuantitativas[::2]
    cuantitativas_impares=cuantitativas[1::2]

    cuantitativas_mean=cuantitativas_pares.fillna(round(cuantitativas.mean(),1))
    cuantitativas_99=cuantitativas_impares.fillna(99)
    cualitativas_str=cualitativas.fillna("Este_es_un_valor_nulo")

    cuantis = pd.concat([cuantitativas_mean,cuantitativas_99],axis=1)
    concatenado = pd.concat([cuantis,cualitativas_str],axis=1)
    print(concatenado)

def funcion_3(df):
    import pandas as pd
    import os

    valores_nulos=df.isnull().sum()
    print("""Por Columna:
          """,valores_nulos)
    valores_nulos2=df.isnull().sum().sum()
    print("""Por DataFrame:
          """,valores_nulos2)
    
def funcion_4(df):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    cuantitativas=df.select_dtypes(include=["float64","int64","float","int"])
    cualitativas=df.select_dtypes(include=["object","datetime","category"])
    y=cuantitativas

    percentile25=y.quantile(0.25)
    percentile75=y.quantile(0.75)
    iqr= percentile75-percentile25

    Limite_Superior_iqr= percentile75+1.5*iqr
    Limite_Inferior_iqr= percentile25-1.5*iqr
    iqr=cuantitativas[(y<=Limite_Superior_iqr)&y>=(Limite_Inferior_iqr)]
    iqr2=iqr.fillna(round(iqr.mean(),1))
    iqr3=pd.concat([cualitativas,iqr2],axis=1)
    return(iqr3)