import jobboss.models
import inspect
import pickle


def create_database_snapshot(snapshot_file_path):
    snapshot = {}
    models = inspect.getmembers(jobboss.models, lambda member: inspect.isclass(member) and member.__module__ == 'jobboss.models')
    for model_name, model in models:
        try:
            column_names = tuple(field.name for field in model._meta.get_fields())
            rows = list(model.objects.all().values_list())
            snapshot[model_name] = {'columns': column_names, 'rows': rows}
        except:
            print(f'Problem with table: {model_name}. Skipping.')
            continue
    with open(snapshot_file_path, 'wb') as f:
        pickle.dump(snapshot, f)


def compare_database_snapshots(old_snapshot_file_path, new_snapshot_file_path):
    with open(old_snapshot_file_path, 'rb') as old_f, open(new_snapshot_file_path, 'rb') as new_f:
        old_snapshot = pickle.load(old_f)
        new_snapshot = pickle.load(new_f)
    for table_name in old_snapshot:
        try:
            table_columns = old_snapshot[table_name]['columns']
            old_table_rows = old_snapshot[table_name]['rows']
            new_table_rows = new_snapshot[table_name]['rows']
            table_diff(table_name, table_columns, old_table_rows, new_table_rows)
        except KeyError:
            continue


def table_diff(table_name, table_columns, old_table_rows, new_table_rows):
    print('-----------')
    print(f'Table name: {table_name}')
    print('-----------')
    # Hash the rows from the old and new tables
    old_table_row_hashes = {hash(row): i for i, row in enumerate(old_table_rows)}
    new_table_row_hashes = {hash(row): i for i, row in enumerate(new_table_rows)}
    if len(old_table_rows) != len(new_table_rows):
        print(f'Old table has {len(old_table_rows)} rows. New table has {len(new_table_rows)} rows.')
        print()

    # Check the differences between old table and new table in both directions, based on hash.
    # These include rows that were deleted, rows that were added, and rows that were updated.
    # Updated rows will show up in both of these sets, and we'll identify them in the next step.
    in_old_but_not_new = set(old_table_row_hashes.keys()).difference(set(new_table_row_hashes.keys()))
    in_new_but_not_old = set(new_table_row_hashes.keys()).difference(set(old_table_row_hashes.keys()))

    # Check if any modified rows have the same index in the old table and new table. If so, this is likely an update to an
    # existing row
    in_old_but_not_new_indexes = set([old_table_row_hashes[row_hash] for row_hash in in_old_but_not_new])
    in_new_but_not_old_indexes = set([new_table_row_hashes[row_hash] for row_hash in in_new_but_not_old])
    shared_indexes = in_old_but_not_new_indexes.intersection(in_new_but_not_old_indexes)
    for row_index in shared_indexes:
        print(f'Row {row_index} was updated:')
        print(f'Old row: {old_table_rows[row_index]}')
        print(f'New row: {new_table_rows[row_index]}')
        row_diff(table_columns, old_table_rows[row_index], new_table_rows[row_index])
        print()

    # Determine which rows were deleted from the old table, or added to the new table
    deleted_from_old_indexes = in_old_but_not_new_indexes.difference(shared_indexes)
    added_to_new_indexes = in_new_but_not_old_indexes.difference(shared_indexes)

    if deleted_from_old_indexes:
        print(f'The following rows were deleted from the old table:')
        for row_index in deleted_from_old_indexes:
            row = old_table_rows[row_index]
            row_dict = {table_columns[i]: val for i, val in enumerate(row)}
            print()
            print(f'{row_index}: {row_dict}')
        print()

    if added_to_new_indexes:
        print(f'The following rows were added to the new table:')
        for row_index in added_to_new_indexes:
            row = new_table_rows[row_index]
            row_dict = {table_columns[i]: val for i, val in enumerate(row)}
            print()
            print(f'{row_index}: {row_dict}')
    print('-----------')


def row_diff(table_columns, old_row, new_row):
    for i, old_val in enumerate(old_row):
        new_val = new_row[i]
        if old_val != new_val:
            print(f'Rows differ at column {i} ({table_columns[i]}): {old_val} != {new_val}')
