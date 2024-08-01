# Initialize an empty list to store table names and a dictionary to record errors
table_list = []
errors = {}

# Retrieve a DataFrame containing the list of databases
database_df = spark.sql("SHOW DATABASES")

# Loop through each database and retrieve the list of tables in that database
for database in database_df.collect():
    table_df = spark.sql("SHOW TABLES FROM {}".format(database[0]))
    table_list.extend([database[0] + '.' + row['tableName'] for row in table_df.select('tableName').collect()])

def get_table_count(table_name):
    """
    Retrieve the count of rows in a table.

    Parameters:
    table_name (str): The fully qualified name of the table.

    Returns:
    str: The table name and its row count.
    """
    count_df = spark.sql("SELECT COUNT(*) FROM {}".format(table_name))
    return f"{table_name}:{count_df.collect()[0][0]}"

# Code to fetch table counts sequentially
for table_name in table_list:
    try:
        print(get_table_count(table_name))
    except Exception as e:
        print(f"Failed: {table_name}")


# Code to fetch table counts using ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor, as_completed

if table_list:
    # Use ThreadPoolExecutor to parallelize the retrieval of table row counts
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Submit tasks to the executor for each table in the list
        futures = {executor.submit(get_table_count, table_name): table_name for table_name in table_list}
        # As each future completes, process the result
        for future in as_completed(futures):
            table_details = futures[future]
            try:
                # Retrieve the result from the future and print it or you can write to files
                result = future.result()
                print(result)
            except Exception as e:
                errors[table_details] = str(e)

    # In case of errors, print failed tables and their error details
    if errors:
        print(f"Failed to retrieve count for {len(errors)} tables. Error details given below:")
        for error, message in errors.items():
            print(f"Table Name: {error} | Details: {message}")
    else:
        print("Task completed successfully")
