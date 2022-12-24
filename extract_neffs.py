import csv
import json
import os
from pathlib import Path

NEFF_DIR = os.getenv('neff_dir')


def read_neffs(hhm_file: Path) -> list[int]:
    neff_list = []
    with hhm_file.open() as f:
        reader = csv.reader(f, delimiter='\t')

        # Skip all entries until 'HMM' field is found and then three more
        for l in reader:
            if l and l[0].startswith('HMM'):
                next(reader)
                next(reader)
                next(reader)
                break

        # Read entry from 8th column of every third line
        for l in reader:
            neff_list.append(int(l[7]))
            next(reader)
            next(reader)
    return neff_list


if __name__ == '__main__':
    file_list = [f for f in Path('/tmp').iterdir() if f.is_file() and f.suffix == '.hhm']

    for file in file_list:
        neff_list = read_neffs(file)

        # Write results to json file
        neff_dir = Path(NEFF_DIR)
        neff_dir.mkdir(exist_ok=True)
        neff_file = neff_dir / f'{file.stem}.json'
        with neff_file.open('w') as f:
            json.dump(neff_list, f)
