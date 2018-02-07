'''module for working with data shell'''
import main
import sys

# Project id from DB.
project_id = int(sys.argv[1])

# Method received shell.
method = sys.argv[2]

# Test on method.
if method == 'auto':
    '''Collects semantics from domain.'''

    main.auto_sem(project_id)

elif method == 'query':
    '''Collects semantics from query word'''

    query = sys.argv[3]

    # This magic number, limits the max result.
    main.query_sem(project_id, query, 300)

elif method == 'cr':
    '''Collects semantics from competitors in yandex'''

    query = sys.argv[3]

    main.cr_sem(project_id, query)

elif method == 'form':
    '''Can work with large amounts of data and minus words'''

    minus_id_array = sys.argv[3:]
    main.form_sem(project_id, minus_id_array)
