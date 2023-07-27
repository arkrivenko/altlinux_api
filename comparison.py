from packaging.version import Version, InvalidVersion


class Comparator:

    def compare_archs(self, arh_list1, arch_list2):
        final_archs_list = list(set(arh_list1 + arch_list2))

        return final_archs_list

    def compare_packages(self, package1, package2):
        package1_dict = {}
        package2_dict = {}

        if package1:
            for package in package1:
                key = (package['name'], package['arch'])
                package1_dict[key] = package

        if package2:
            for package in package2:
                key = (package['name'], package['arch'])
                package2_dict[key] = package

        only_in_package1 = []
        if package1_dict:
            for key, package in package1_dict.items():
                if key not in package2_dict:
                    only_in_package1.append(package)

        only_in_package2 = []
        if package2_dict:
            for key, package in package2_dict.items():
                if key not in package1_dict:
                    only_in_package2.append(package)

        higher_in_package1 = []
        if package1_dict and package2_dict:
            for key, package in package1_dict.items():
                if key in package2_dict:
                    try:
                        version1 = Version(package['version'])
                        version2 = Version(package2_dict[key]['version'])
                        if version1 > version2:
                            higher_in_package1.append(package)
                    except InvalidVersion:
                        pass

        result = {
            'only_in_package1': only_in_package1,
            'only_in_package2': only_in_package2,
            'higher_in_package1': higher_in_package1
        }

        return result
