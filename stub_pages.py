import csv
from pathlib import Path

with open('../_data/schedule.csv') as f :
    f = csv.DictReader(f)

    for r in f :
        if r['Topic Tag'] != '' :
            path = Path('../_lectures/{}.md'.format(r['Topic Tag']))

            if not path.exists() :
                with open(path,'wt') as f_out :
                    f_out.write('''---\n---\n\n''')

        if r['Assignment Tag'] != '' :
            path = Path('../_assignments/{}.md'.format(r['Assignment Tag']))

            if not path.exists() :
                with open(path,'wt') as f_out :
                    f_out.write('''---\n---\n\n''')

