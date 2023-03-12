from sqlalchemy import create_engine, MetaData

engine = create_engine('mssql+pyodbc://localhost:1433/ga_dev?Trusted_Connection=yes&driver=ODBC+Driver+17+for+SQL+Server')
meta = MetaData()

# variable de conexion
conect = engine.connect()