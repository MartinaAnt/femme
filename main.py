import pandas as pd
import json


class MenteesReport:

    def __init__(self):
        #   - load mentees from specified csv file
        self.data = pd.read_csv('mentees.csv')

        #    - get the number of mentees
        self.num_mentees = len(self.data.index)

        #    - get set of all languages mentees know
        self.languages = set(self.data.language.unique())

        #    - get an average length of mentees full names
        self.data['full_names'] = self.data['first_name'] + ' ' + self.data['last_name']
        name_len = self.data.full_names.str.len()
        self.avg_name_len = name_len.mean()

        #    - find mentee with longest full name
        longest_name_idx = name_len.idxmax()
        self.longest_name = self.data.loc[longest_name_idx, 'full_names']

        #    - find mentee with shortest full name
        shortest_name_idx = name_len.idxmin()
        self.shortest_name = self.data.loc[shortest_name_idx, 'full_names']

    #    - save report into .json file containing all the information above
    def report(self):
        data_report = {
            'num_mentees': self.num_mentees,
            'languages': list(self.languages),
            'full_names': {
                'avg_len': self.avg_name_len,
                'longest': self.longest_name,
                'shortest': self.shortest_name,
            }
        }

        return json.dumps(data_report, indent=2, ensure_ascii=False)


# if __name__ == '__main__':
#     with open('report.json', 'w') as f:
#         f.write(MenteesReport().report())
