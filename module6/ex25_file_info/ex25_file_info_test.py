import os.path
from glob import glob
from ex25_file_info import get_file_info


def test_nothing(tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()

    assert len(list(d.iterdir())) == 0
    assert get_file_info(d) == []


def test_three_good_files(tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()

    for i in [1, 500, 1000]:
        with open(d / f'file{i}', 'w') as f:
            f.write('abcd\n' * i)

    assert len(list(d.iterdir())) == 3

    file_info = get_file_info(d)
    assert type(file_info) == list
    assert len(file_info) == 3

    assert {'file1', 'file500', 'file1000'} == {os.path.basename(one_item['filename'])
                                                for one_item in file_info}

    assert file_info[0]['sha1'] == '819abca7eabfd860df0d96b850cd43d64fce35c4'
    assert file_info[1]['sha1'] == 'e31780bcdeb62dfd8b939fa9b77dc7412cc83399'
    assert file_info[2]['sha1'] == '3330b4373640f9e4604991e73c7e86bfd8da2dc3'
