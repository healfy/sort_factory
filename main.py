import os
import json
import argparse
import typing
from sorts import AbstractSortFactory, BaseSort


def path_validate(fp: str):
    if not os.path.exists(fp) or os.path.isdir(fp):
        raise ValueError(f'invalid source file path {fp}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--f1', help='source file', type=str)
    parser.add_argument('--f2', help='target file', type=str)
    parser.add_argument('--sort', help='sorting type', type=str)

    args = parser.parse_args()
    path_validate(args.f1)
    with open(args.f1, 'r') as file:
        data = file.read()
        array = json.loads(data)

    sorter: typing.Type[BaseSort] = AbstractSortFactory.get_sorter(args.sort)

    result = sorter().sort(array)

    with open(args.f2, 'w') as file:
        file.write(f'Sorted with {args.sort} sort\n')
        file.write(json.dumps(result))

    print(f'Sorting is finished. Pls open {args.f2} and check result')
    print(f'Result is {result}')
