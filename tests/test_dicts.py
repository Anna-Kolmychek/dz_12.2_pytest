from utils import dicts


def test_get_val():
    assert dicts.get_val({'vcs': 'mercurial'}, 'vcs') == 'mercurial'
    assert dicts.get_val({'vcs': 'mercurial'}, 'vcs', 'git') == 'mercurial'
    assert dicts.get_val({'vcs': 'mercurial'}, 'not_key') == 'git'
    assert dicts.get_val({}, 'vcs', 'git') == 'git'
    assert dicts.get_val({}, 'vcs', 'bazaar') == 'bazaar'


def test_get_val__wrong_type():
    assert dicts.get_val([1, 2, 3], 'vcs') == 'git'

