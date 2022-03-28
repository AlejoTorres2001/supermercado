def select(cursor,fields_to_select,table,condition="TRUE"):
    q = f"SELECT {fields_to_select} FROM {table} WHERE {condition}"
    cursor.execute(q)
    return cursor.fetchall()