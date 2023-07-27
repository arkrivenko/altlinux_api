import argparse
import json

from api import AltLinuxAPI


def main():
    parser = argparse.ArgumentParser(description='AltLinux API CLI')
    parser.add_argument('--branch1', type=str, required=True, help='First branch')
    parser.add_argument('--branch2', type=str, required=True, help='Second branch')
    parser.add_argument('-o', '--output', type=str, help='Output file')
    args = parser.parse_args()

    api = AltLinuxAPI()

    branch1 = args.branch1
    branch2 = args.branch2

    arch_list1 = api.get_all_pkgset_archs(branch1)
    arch_list2 = api.get_all_pkgset_archs(branch2)

    file_name = args.output

    result = 'some result data'

    if file_name:
        if file_name.endswith('.json'):
            with open(file_name, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=4)
        else:
            print(f'Data must be written to a json document!')
            with open('packages_result.json', 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=4)
            print('Data is written to the packages_result.json')

    else:
        print(json.dumps(result, indent=4))


if __name__ == '__main__':
    main()
