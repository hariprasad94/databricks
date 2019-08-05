#create spark dataframe with data
source_df = spark.createDataFrame(
    [
        ("C53001", "Alex Samuel", "Data Engineer", "alex@nldatabricks.com", "New Jersey"),
        ("C53002", "Mary John", "Data Engineer", "mary@nldatabricks.com", "Manhattan"),
        ("C53003", "Benny Joseph", "Data Scientist", "benny@nldatabricks.com", "Ohio"),
        ("C53004", "Richard Parker", "Data Scientist", "richard@nldatabricks.com", "Chicago"),
        ("C53005", "Loslia Fernandez", "Data Engineer", "loslia@nldatabricks.com", "New York")
    ],
    ["EMP_ID", "EMP_NAME", "EMP_DESIGNATION", "EMP_CONTACT", "EMP_STATE"]
)

#resister the dataframe and create SQL table
source_df.registerTempTable('temp')
spark.sql('DROP TABLE IF EXISTS EMPLOYEE')
spark.sql('CREATE TABLE EMPLOYEE select * from temp')

#apply transformation and display the results
df = spark.sql('SELECT COUNT(1) as CNT, EMP_STATE FROM EMPLOYEE GROUP BY EMP_STATE ORDER BY CNT DESC')
df.show()