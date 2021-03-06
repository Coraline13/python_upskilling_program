import pytest
import string
from io import StringIO
import ex11_tee


@pytest.fixture
def some_text():
    return string.ascii_lowercase


def test_write_1(some_text):
    outfile = StringIO()
    t = ex11_tee.Tee(outfile)
    t.write(some_text)

    outfile.seek(0)
    assert (outfile.read() == some_text)


def test_write_2(some_text):
    outfile1 = StringIO()
    outfile2 = StringIO()

    t = ex11_tee.Tee(outfile1, outfile2)
    t.write(some_text)

    for output in [outfile1, outfile2]:
        output.seek(0)
        assert (output.read() == some_text)


def test_writelines(some_text):
    outfile1 = StringIO()
    outfile2 = StringIO()

    t = ex11_tee.Tee(outfile1, outfile2)
    t.writelines([some_text, some_text])

    for output in [outfile1, outfile2]:
        output.seek(0)
        assert (output.read() == '\n'.join([some_text] * 2))


def test_with(some_text):
    outfile = StringIO()

    with ex11_tee.Tee(outfile) as t:
        t.write(some_text)

    assert outfile.closed


def test_with_check_output(some_text, tmp_path):
    f = tmp_path / 'outfile.txt'
    outfile = open(f, 'w')

    with ex11_tee.Tee(outfile) as t:
        t.write(some_text)

    assert outfile.closed
    assert open(f).read() == some_text
