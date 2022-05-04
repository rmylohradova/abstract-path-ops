from mypathlib import Path


def test_path1():
    assert Path('folder').nest('images').nest('image.jpeg').showpath() == 'folder/images/image.jpeg'


def test_path2():
    assert Path('modified').showpath() == 'modified'


def test_name1():
    p = Path('movies').nest('shows').nest('horrors').nest('review.txt')
    assert p.name() == 'review.txt'
    assert p.parent() == 'movies/shows/horrors'


def test_dirs1():
    p = Path('movies').nest('shows').nest('horrors').nest('review.txt')
    p.write_str('this movie flopped')
    assert p.read_str() == 'this movie flopped'




